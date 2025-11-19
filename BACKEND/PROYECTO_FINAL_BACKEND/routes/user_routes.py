from flask import request,jsonify,Blueprint
from repositories.user_repository import UserRepository


users_repo=UserRepository()
users_bp=Blueprint("users",__name__)


@users_bp.route("/users", methods=["GET"])
def get_all_users():
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/users/<id>", methods=["GET"])
def get_user_by_id(user_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/users", methods=["POST"])
def create_user():
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/users/<id>", methods=["PUT"])
def update_user(user_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/users/<id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500