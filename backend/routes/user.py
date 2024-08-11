from flask import Blueprint, jsonify, session
from flask_cors import cross_origin
from model import Users


user_bp = Blueprint('user', __name__)


@user_bp.route("/currentUser", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_current_user():
    try:
        res = Users.query.get(session["user"]["preferred_username"])
        return res.json(), 200
    except Exception:
        return jsonify(None), 200
