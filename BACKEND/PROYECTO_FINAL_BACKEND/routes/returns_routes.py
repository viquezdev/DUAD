from flask import request,jsonify,Blueprint
from repositories.returns_repository import ReturnsRepository


returns_repo=ReturnsRepository()
returns_bp=Blueprint("returns",__name__)


@returns_bp.route("/returns", methods=["GET"])
def get_all_returns():
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@returns_bp.route("/returns/<id>", methods=["GET"])
def get_return_by_id(return_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@returns_bp.route("/returns", methods=["POST"])
def create_return():
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@returns_bp.route("/returns/<id>", methods=["PUT"])
def update_return(return_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@returns_bp.route("/returns/<id>", methods=["DELETE"])
def delete_return(return_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500