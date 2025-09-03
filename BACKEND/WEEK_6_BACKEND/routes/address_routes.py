from flask import request, g, jsonify, Blueprint
from repositories.address_repository import AddressRepository

addresses_bp=Blueprint("addresses",__name__)

@addresses_bp.route("/", methods=["POST"])
def create_address():
    try:
        addresses_data=request.get_json()
        required_fields = ["street", "city", "user_id"]
        missing_fields = [field for field in required_fields if field not in addresses_data]

        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        addresses_repo = AddressRepository(g.db)
        new_addres=addresses_repo.create(**addresses_data)
        if new_addres:
            return jsonify({"message":"Address created succesfully"}),201
        return jsonify({"error":"error creating addres"}),400
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@addresses_bp.route("/", methods=["GET"])
def get_all_addresses():
    try:
        addresses_repo = AddressRepository(g.db)
        data_addresses=addresses_repo.get_all()
        
        if not data_addresses:
            return jsonify({"data": [], "message": "No addresess found"}), 404
        
        return jsonify({"data": data_addresses}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@addresses_bp.route("/<identifier>", methods=["GET"])
def get_by_id(identifier):
    try:
        addresses_repo = AddressRepository(g.db)
        data_addresses=addresses_repo.get_by_id(identifier)
        
        if not data_addresses:
            return jsonify({"data": [], "message": "No address found"}), 404
        
        return jsonify({"data": data_addresses}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@addresses_bp.route("/<identifier>", methods=["DELETE"])
def delete_address(identifier):
    try:
        adresses_repo = AddressRepository(g.db)
        data_addresses=adresses_repo.delete(identifier)

        if data_addresses is None:
            return jsonify({"data": [], "message": "No address found"}), 404

        return jsonify({
            "message": f"Address with ID {identifier} was deleted successfully"
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error while deleting an address."}), 500
    
@addresses_bp.route("/<identifier>", methods=["PUT"])
def update_address(identifier):
    try:
        data_address=request.get_json()
        addresses_repo = AddressRepository(g.db)
        updated_address=addresses_repo.update(
            address_id=identifier,
            street=data_address.get("street"),
            city=data_address.get("city"),
            postal_code=data_address.get("postal_code"),
            country=data_address.get("country")
        )
        if not updated_address:
            return jsonify({"error": "Address not found"}), 404
        return jsonify({
            "message": f"Address with ID {identifier} was updated successfully"
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error updating address."}), 500