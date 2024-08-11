from flask import Blueprint, jsonify, session
from flask_cors import cross_origin
from model import Filaments


filament_bp = Blueprint('filament', __name__)


@filament_bp.route("/filaments", methods=["GET"])
@cross_origin(supports_credentials=True)
def filaments():
    try:
        res = Filaments.query.all()
        return jsonify([filament.json() for filament in res]), 200
    except Exception:
        return jsonify(None), 200
