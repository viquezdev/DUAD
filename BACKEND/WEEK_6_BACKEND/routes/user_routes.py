
from flask import request, jsonify, Blueprint
from repositories.user_repository import UserRepository


users_bp=Blueprint("users",__name__)

@users_bp.route("/", methods=["POST"])
def create_user():
    try:
        user_data=request.get_json()
        required_fields = ["name", "email", "username", "password"]
        missing_fields = [field for field in required_fields if field not in user_data]

        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
    
        new_user=UserRepository.create(**user_data)
        if new_user:
            return jsonify({"message":"User created succesfully"}),201
        return jsonify({"error":"username or email already exists"}),409 
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@users_bp.route("/", methods=["GET"])
def get_all_users():
    try:
        
        data_users=UserRepository.get_all()
        
        if not data_users:
            return jsonify({"data": [], "message": "No users found"}), 404
        
        return jsonify({"data": data_users}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/<identifier>", methods=["GET"])
def get_by_id(identifier):
    try:
        
        data_users=UserRepository.get_by_id(identifier)
        
        if not data_users:
            return jsonify({"data": [], "message": "No user found"}), 404
        
        return jsonify({"data": data_users}), 200
        
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/<identifier>", methods=["DELETE"])
def delete_user(identifier):
    try:
        
        data_users=UserRepository.delete(identifier)

        if data_users is None:
            return jsonify({"data": [], "message": "No user found"}), 404

        return jsonify({
            "message": f"User with ID {identifier} was deleted successfully"
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error while deleting an user."}), 500
    

@users_bp.route("/<identifier>", methods=["PUT"])
def update_user(identifier):
    try:
        
        data_user=request.get_json()
    
        updated_user=UserRepository.update(
            user_id=identifier,
            name=data_user.get("name"),
            email=data_user.get("email"),
            username=data_user.get("username"),
            password=data_user.get("password")
        )
        if not updated_user:
            return jsonify({"error": "username or email already exists"}), 400
        return jsonify({
            "message": f"User with ID {identifier} was updated successfully"
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error updating user."}), 500


@users_bp.route("/multiple-cars", methods=["GET"])
def get_multiple_cars():
    try:
        
        data_users=UserRepository.get_users_with_multiple_cars()
        
        if not data_users:
            return jsonify({"data": [], "message": "No users found"}), 404
        
        return jsonify({"data": data_users}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@users_bp.route("/<identifier>/relations", methods=["GET"])
def get_cars_addresses_from_user(identifier):
    try:
        
        data_users=UserRepository.get_cars_addresses_from_user(identifier)
        
        if not data_users:
            return jsonify({"data": [], "message": "No users found"}), 404
        
        return jsonify({"data": data_users}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500