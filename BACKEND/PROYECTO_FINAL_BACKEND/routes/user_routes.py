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
@roles_required(0,1)
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