
from flask import request, jsonify, Blueprint
from repositories.product_repository import ContactRepository
from services.jwt_manager import JwtManager
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent
with open(base_path / "keys" / "private.pem", "rb") as f:
    private_key = f.read()

with open(base_path / "keys" / "public.pem", "rb") as f:
    public_key = f.read()

jwt_manager=JwtManager(private_key=private_key,public_key=public_key)

contact_repo = ContactRepository()
contacts_bp=Blueprint("contacts",__name__)



@contacts_bp.route("/", methods=["POST"])
def create_contact():
    try:
        contact_data=request.get_json()
        required_fields = ["user_id", "name","phone","email"]
        missing_fields = [field for field in required_fields if field not in contact_data]

        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        
        
        new_contact=contact_repo.create(**contact_data)

        if new_contact:
            return jsonify({"message":"Contact created succesfully"}),201
        return jsonify({"error":"error creating contact"}),400
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@contacts_bp.route("/", methods=["GET"])
def get_all_contacts():
    try:
        
        data_contacts=contact_repo.get_all()
        
        if not data_contacts:
            return jsonify({"data": [], "message": "No contacts found"}), 404
        
        return jsonify([contact.to_dict() for contact in data_contacts]), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@contacts_bp.route("/<identifier>", methods=["GET"])
def get_by_id(identifier):
    try:
        
        data_contact=contact_repo.get_by_id(identifier)
        
        if not data_contact:
            return jsonify({"data": [], "message": "No contact found"}), 404
        
        return jsonify({"data": data_contact.to_dict()}), 200
        
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@contacts_bp.route("/<identifier>", methods=["DELETE"])
def delete_product(identifier):
    try:
        
        data_contact=contact_repo.delete(identifier)

        if data_contact is None:
            return jsonify({"data": [], "message": "No contact found"}), 404

        return jsonify({
            "message": f"Contact with ID {identifier} was deleted successfully"
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error while deleting a contact."}), 500
    

@contacts_bp.route("/<identifier>", methods=["PUT"])
def update_contact(identifier):
    try:
        
        data_contact=request.get_json()
    
        updated_contact=contact_repo.update(
            contact_id=identifier,
            name=data_contact.get("name"),
            phone=data_contact.get("phone"),
            email=data_contact.get("email")
        )
        if not updated_contact:
            return jsonify({"error": "Contact not found"}), 404
        return jsonify({
            "message": f"Contact with ID {identifier} was updated successfully"
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error updating contact."}), 500


# @users_bp.route("/multiple-cars", methods=["GET"])
# def get_multiple_cars():
#     try:
        
#         data_users=UserRepository.get_users_with_multiple_cars()
        
#         if not data_users:
#             return jsonify({"data": [], "message": "No users found"}), 404
        
#         return jsonify({"data": data_users}), 200
#     except Exception as e:
#         return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

# @users_bp.route("/<identifier>/relations", methods=["GET"])
# def get_cars_addresses_from_user(identifier):
#     try:
        
#         data_users=UserRepository.get_cars_addresses_from_user(identifier)
        
#         if not data_users:
#             return jsonify({"data": [], "message": "No users found"}), 404
        
#         return jsonify({"data": data_users}), 200
#     except Exception as e:
#         return jsonify({"error": "Unexpected error", "details": str(e)}), 500