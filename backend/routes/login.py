from flask import Blueprint, session, jsonify, redirect, request, current_app as app
from flask_cors import cross_origin
from model import db, Users
import contextlib
import time
import msal
import jwt
import re

login_bp = Blueprint('login', __name__)


@login_bp.route("/login")
@cross_origin(supports_credentials=True)
def login():
    config = app.config
    session["flow"] = _build_auth_code_flow(scopes=config["SCOPE"])
    return jsonify({"status": "success", "auth_url": session["flow"]["auth_uri"]})


@login_bp.route("/getAToken")
@cross_origin(supports_credentials=True)
def authorized():
    config = app.config
    with contextlib.suppress(ValueError):
        cache = _load_cache()
        result = _build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
            session.get("flow", {}), request.args
        )
        session["user"] = result.get("id_token_claims")
        session['user']['preferred_username'] = session['user']['preferred_username'].split("@")[0]
        session["user"]["department"] = re.findall(r'\((.*?)\)', session['user']['name'])[0]
        _save_cache(cache)

    user_data = {
        "firstname": session["user"]["given_name"],
        "surname": session["user"]["family_name"],
        "mail": session["user"]["email"],
        "department": session["user"]["department"],
        "admin": session['user']['preferred_username'] in config['ADMIN_LIST']
    }

    # Check if the user exists
    user = (db.session.query(Users).filter_by(id=session["user"]["preferred_username"]).first())

    if user:
        # Update the existing user's information
        for key, value in user_data.items():
            setattr(user, key, value)
    else:
        # Create a new user
        user = Users(id=session["user"]["preferred_username"], **user_data)
        db.session.add(user)
    db.session.commit()

    # redirect user to start
    return redirect(config["MAIN_URL"])


@login_bp.route("/logout")
@cross_origin(supports_credentials=True)
def logout():
    config = app.config
    session.clear()
    return_dict = {
        "logout_url": config["AUTHORITY"]
                      + "/oauth2/v2.0/logout"
                      + f"?post_logout_redirect_uri={config['MAIN_URL']}login"
    }
    return jsonify(return_dict)


@login_bp.route("/loggedIn")
@cross_origin(supports_credentials=True)
def logged_in():
    user = session.get("user")

    if not user:
        # If user is not in session
        return jsonify(False)

    token = user.get("token")

    try:
        # Decode the token without verifying the signature
        decoded_token = jwt.decode(token, options={"verify_signature": False})

        # Get current time
        current_time = time.time()

        # Check if the token is expired
        return jsonify(False) if current_time > decoded_token["exp"] else jsonify(True)
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        # If the token is expired or invalid
        return jsonify(False)


def _load_cache():
    cache = msal.SerializableTokenCache()
    if session.get("token_cache"):
        cache.deserialize(session["token_cache"])
    return cache


def _save_cache(cache):
    if cache.has_state_changed:
        session["token_cache"] = cache.serialize()


def _build_msal_app(cache=None):
    config = app.config
    return msal.ConfidentialClientApplication(
        config["CLIENT_ID"],
        authority=config["AUTHORITY"],
        client_credential=config["CLIENT_SECRET"],
        token_cache=cache,
        verify=False,
    )


def _build_auth_code_flow(scopes=None):
    config = app.config
    return _build_msal_app().initiate_auth_code_flow(
        scopes or [], redirect_uri=f"{config['VITE_APP_BACKEND_URL']}getAToken"
    )
