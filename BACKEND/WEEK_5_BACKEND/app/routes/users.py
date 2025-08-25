from flask import request, Response, jsonify, Blueprint
from app.db.pg_manager import PgManager
from app.repositories.user_repository import UserRepository

users_bp=Blueprint("users",__name__)

@users_bp.route("/", methods=["POST"])
def create_user():
    try:
        user_data=request.get_json()
        required_fields = ["name", "email", "username", "password","birth_date","account_status"]
        missing_fields = [field for field in required_fields if field not in user_data]

        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )

        users_repo = UserRepository(db_manager)
        users_repo.create(**user_data)
        db_manager.close_connection()
        return jsonify({"message":"User created succesfully"}),201
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

@users_bp.route("/<int:user_id>/status", methods=["PUT"])
def update_user_status(user_id):
    try:   
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )
        user_data=request.get_json()
        if not user_data or "account_status" not in user_data:
            return jsonify({"error": "Missing 'account_status' field"}), 400
        
        new_status=user_data.get("account_status")
        
        users_repo = UserRepository(db_manager)
        users_repo.update_status(user_id,new_status)

        db_manager.close_connection()
        return jsonify({"message":"User status updated succesfully"}),200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

@users_bp.route("/<int:user_id>/moroso", methods=["PUT"])
def flag_user(user_id):
    try:
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )
        users_repo = UserRepository(db_manager)
        updated=users_repo.flag_user_as_moroso(user_id)
        
        if not updated:  
            return jsonify({"message": f"User with id {user_id} not found"}), 404

        db_manager.close_connection()
        return jsonify({"message":"User flagged as moroso"}),200
    
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

@users_bp.route("/", methods=["GET"])
def get_all_users():
    try:
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )
        users_repo = UserRepository(db_manager)
        data_users=None
        filters = {
            "id": users_repo.get_by_id,
            "name": users_repo.get_by_name,
            "email": users_repo.get_by_email,
            "username": users_repo.get_by_username,
            "birth_date": users_repo.get_by_birth_date,
            "account_status": users_repo.get_by_account_status
        }

        data_users = None
        for key, func in filters.items():
            if key in request.args:
                data_users = func(request.args[key])
                break

        if data_users is None:    
            data_users=users_repo.get_all()
        
        if not data_users:
            return jsonify({"data": [], "message": "No users found"}), 404
        db_manager.close_connection()
        return jsonify({"data": data_users}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500










