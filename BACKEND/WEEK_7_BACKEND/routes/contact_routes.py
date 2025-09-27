
from flask import request, jsonify, Blueprint
from repositories.contact_repository import ContactRepository
from services.decorators import roles_required,get_jwt_identity
from pathlib import Path

contact_repo = ContactRepository()
contacts_bp=Blueprint("contacts",__name__)


@contacts_bp.route("/", methods=["POST"])
@roles_required("administrator","user")
def create_contact():
    try:
        user_data=get_jwt_identity()
        contact_data=request.get_json()

        required_fields = ["user_id", "name","phone","email"]
        missing_fields = [field for field in required_fields if field not in contact_data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        
        if user_data["role"]=="user" and user_data["sub"]!=str(contact_data["user_id"] ):
            return jsonify({"error": "Access denied"}), 403
            
        new_contact=contact_repo.create(**contact_data)

        if new_contact:
            return jsonify({"message":"Contact created succesfully"}),201
        return jsonify({"error":"error creating contact"}),400
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@contacts_bp.route("/", methods=["GET"])
@roles_required("administrator","user")
def get_all_contacts():
    try:
        user_data=get_jwt_identity()
        if user_data["role"]=="user":
            data_contacts=contact_repo.get_by_user(user_data["sub"])
        else:
            data_contacts=contact_repo.get_all()
        
        if not data_contacts:
            return jsonify({"data": [], "message": "No contacts found"}), 404
        
        return jsonify([contact.to_dict() for contact in data_contacts]), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@contacts_bp.route("/<identifier>", methods=["GET"])
@roles_required("administrator")
def get_by_id(identifier):
    try:
        
        data_contact=contact_repo.get_by_id(identifier)
        
        if not data_contact:
            return jsonify({"data": [], "message": "No contact found"}), 404
        
        return jsonify({"data": data_contact.to_dict()}), 200
        
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@contacts_bp.route("/<identifier>", methods=["DELETE"])
@roles_required("administrator","user")
def delete_contact(identifier):
    try:
        user_data=get_jwt_identity()
        user_id=contact_repo.get_user_id(identifier)
        if user_id is None:
            return jsonify({"data": [], "message": "No contact found"}), 404
        if user_data["role"]=="user" and user_data["sub"]!=str(user_id) :
            return jsonify({"error": "Access denied"}), 403

        deleted_contact=contact_repo.delete(identifier)

        return jsonify({
            "message": f"Contact with ID {identifier} was deleted successfully"
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error while deleting a contact."}), 500
    

@contacts_bp.route("/<identifier>", methods=["PUT"])
@roles_required("administrator","user")
def update_contact(identifier):
    try:
        user_data = get_jwt_identity()
        data_contact = request.get_json()


        contact_owner_id = contact_repo.get_user_id(identifier)
        if contact_owner_id is None:
            return jsonify({"error": "Contact not found"}), 404

        
        if user_data["role"] == "user" and user_data["sub"] !=str( contact_owner_id):
            return jsonify({"error": "Access denied"}), 403

        updated_contact = contact_repo.update(
            contact_id=identifier,
            name=data_contact.get("name"),
            phone=data_contact.get("phone"),
            email=data_contact.get("email")
        )

        return jsonify({
            "message": f"Contact with ID {identifier} was updated successfully",
            "contact": updated_contact.to_dict()
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error updating contact."}), 500


