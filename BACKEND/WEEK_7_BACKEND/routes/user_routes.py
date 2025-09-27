
from flask import request, jsonify, Blueprint
from datetime import datetime, timedelta,timezone
from repositories.user_repository import UserRepository
from services.password_manager import PasswordManager
from services.decorators import roles_required
from services.jwt_manager import jwt_manager 

password_manager = PasswordManager()

user_repo = UserRepository(password_manager=password_manager)
users_bp=Blueprint("users",__name__)


@users_bp.route("/login",methods=["POST"])
def login():
    try:
        user_data=request.get_json()
        username=user_data.get("username")
        password=user_data.get("password")
        user=user_repo.get_by_username(username)
        if not user or not password_manager.verify_password(password,user.password):
            return jsonify({"error": "Invalid credentials"}), 401
        token_payload = {
            "sub": str(user.id),
            "role": user.role,
            "exp":  datetime.now(timezone.utc)  + timedelta(minutes=15)

        }
        token=jwt_manager.encode(token_payload)
        return jsonify({"access_token": token}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

@users_bp.route("/", methods=["POST"])
@roles_required("administrator")
def create_user():
    try:
        user_data=request.get_json()
        required_fields = ["username", "password","role"]
        missing_fields = [field for field in required_fields if field not in user_data]

        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        
        
        new_user=user_repo.create(**user_data)

        if new_user:
            return jsonify({"message":"User created succesfully"}),201
        return jsonify({"error":"username already exists"}),409 
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@users_bp.route("/", methods=["GET"])
@roles_required("administrator")
def get_all_users():
    try:
        
        data_users=user_repo.get_all()
        
        if not data_users:
            return jsonify({"data": [], "message": "No users found"}), 404
        
        return jsonify([user.to_dict() for user in data_users]), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/<identifier>", methods=["GET"])
@roles_required("administrator")
def get_by_id(identifier):
    try:
        
        data_users=user_repo.get_by_id(identifier)
        
        if not data_users:
            return jsonify({"data": [], "message": "No user found"}), 404
        
        return jsonify({"data": data_users.to_dict()}), 200
        
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/<identifier>", methods=["DELETE"])
@roles_required("administrator")
def delete_user(identifier):
    try:
        
        data_users=user_repo.delete(identifier)

        if data_users is None:
            return jsonify({"data": [], "message": "No user found"}), 404

        return jsonify({
            "message": f"User with ID {identifier} was deleted successfully"
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error while deleting an user."}), 500
    

@users_bp.route("/<identifier>", methods=["PUT"])
@roles_required("administrator")
def update_user(identifier):
    try:
        
        data_user=request.get_json()
    
        updated_user=user_repo.update(
            user_id=identifier,
            username=data_user.get("username"),
            role=data_user.get("role")
        )
        if not updated_user:
            return jsonify({"error": "username already exists"}), 400
        return jsonify({
            "message": f"User with ID {identifier} was updated successfully"
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error updating user."}), 500


