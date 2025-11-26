from flask import request,jsonify,Blueprint
from datetime import datetime,timedelta,timezone
from repositories.user_repository import UserRepository
from repositories.login_history_repository import LoginHistoryRepository
from services.password_manager import PasswordManager
from services.decorators import roles_required
from services.jwt_manager import jwt_manager

password_manager=PasswordManager()
users_repo=UserRepository(password_manager=password_manager)
login_history_repo=LoginHistoryRepository()
users_bp=Blueprint("users",__name__)


@users_bp.route("/login",methods=["POST"])
def login():
    try:
        user_data=request.get_json()
        username=user_data.get("username")
        password=user_data.get("password")
        user=users_repo.get_by_username(username)
        if not user or not password_manager.verify_password(password,user.password):
            if user:
                login_history_repo.create(user.id,datetime.utcnow(),request.remote_addr,False)
            return jsonify({"error": "Invalid credentials"}), 401
        access_payload = {
            "sub": str(user.id),
            "is_admin": user.is_admin,
            "exp":  datetime.now(timezone.utc)  + timedelta(minutes=15),
            "type":"access"
        }
        access_token=jwt_manager.encode(access_payload)
        refresh_payload={
            "sub": str(user.id),
            "is_admin": user.is_admin,
            "exp":  datetime.now(timezone.utc)  + timedelta(days=7),
            "type":"refresh"
        }
        refresh_token=jwt_manager.encode(refresh_payload)
        login_history_repo.create(user.id,datetime.utcnow(),request.remote_addr,True)
        return jsonify({
            "access_token": access_token,
            "refresh_token": refresh_token
        }), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}),500


@users_bp.route("/refresh-token",methods=["POST"])
def refresh_token():
    try:
        auth_header=request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error":"Refresh token requerido"}),401        
        refresh_token=auth_header.split(" ")[1]
        payload=jwt_manager.decode(refresh_token)
        if payload.get("type")!="refresh":
            return jsonify({"error":"Invalid token"}),403       
        new_access_payload={
            "sub": payload["sub"],
            "is_admin": payload["is_admin"],
            "exp":  datetime.now(timezone.utc)  + timedelta(minutes=15),
            "type":"access"
        }
        new_access_token=jwt_manager.encode(new_access_payload)        
        return jsonify({"access_token": new_access_token}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@users_bp.route("/users", methods=["GET"])
@roles_required(True)
def get_all_users():
    try:
        data_users=users_repo.get_all()
        if not data_users:
            return jsonify({"data": [], "message": "No users found"}), 404
        return jsonify([user.to_dict() for user in data_users]), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/users/<id>", methods=["GET"])
@roles_required(True)
def get_user_by_id(id):
    try:
        data_user=users_repo.get_by_id(id)
        if not data_user:
            return jsonify({"data": [], "message": "No user found"}), 404
        return jsonify({"data": data_user.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/users", methods=["POST"])
@roles_required(True)
def create_user():
    try:
        user_data=request.get_json()
        required_fields = ["username","password","email","is_admin","created_at","updated_at"]
        missing_fields = [field for field in required_fields if field not in user_data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        new_user=users_repo.create(**user_data)
        if new_user:
            return jsonify({"message":"User created succesfully"}),201
        return jsonify({"error":"username already exists"}),409 
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/users/<id>", methods=["PUT"])
@roles_required(True)
def update_user(id):
    try:
        data_user=request.get_json()
        updated_user=users_repo.update(
            id=id,
            username=data_user.get("username"),
            email=data_user.get("email"),
            is_admin=data_user.get("is_admin"),
            created_at=data_user.get("created_at"),
            updated_at=data_user.get("updated_at")
        )
        if not updated_user:
            return jsonify({"error": "username already exists"}), 400
        return jsonify({
            "message": f"User with ID {id} was updated successfully"
        }), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/users/<int:id>", methods=["DELETE"])
@roles_required(True)
def delete_user(id):
    try:
        data_users=users_repo.delete(id)
        if data_users is None:
            return jsonify({"data": [], "message": "No user found"}), 404
        return jsonify({"message": f"User with ID {id} was deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500