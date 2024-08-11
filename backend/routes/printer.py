from flask import Blueprint, jsonify, session
from flask_cors import cross_origin
from model import Printers


printer_bp = Blueprint('printer', __name__)


@printer_bp.route("/printers", methods=["GET"])
@cross_origin(supports_credentials=True)
def printers():
    try:
        res = Printers.query.all()
        return jsonify([printer.json() for printer in res]), 200
    except Exception:
        return jsonify(None), 200
