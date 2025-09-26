
from flask import request, jsonify, Blueprint
from repositories.product_repository import ProductRepository
from services.jwt_manager import JwtManager
from services.decorators import roles_required
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent
with open(base_path / "keys" / "private.pem", "rb") as f:
    private_key = f.read()

with open(base_path / "keys" / "public.pem", "rb") as f:
    public_key = f.read()

jwt_manager=JwtManager(private_key=private_key,public_key=public_key)

product_repo = ProductRepository()
products_bp=Blueprint("products",__name__)



@products_bp.route("/", methods=["POST"])
@roles_required("administrator")
def create_product():
    try:
        product_data=request.get_json()
        required_fields = ["name", "price","entry_date","quantity"]
        missing_fields = [field for field in required_fields if field not in product_data]

        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        
        
        new_product=product_repo.create(**product_data)

        if new_product:
            return jsonify({"message":"Product created succesfully"}),201
        return jsonify({"error":"error creating product"}),400 
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@products_bp.route("/", methods=["GET"])
@roles_required("administrator","user")
def get_all_products():
    try:
        
        data_products=product_repo.get_all()
        
        if not data_products:
            return jsonify({"data": [], "message": "No products found"}), 404
        
        return jsonify([product.to_dict() for product in data_products]), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@products_bp.route("/<identifier>", methods=["GET"])
@roles_required("administrator","user")
def get_by_id(identifier):
    try:
        
        data_product=product_repo.get_by_id(identifier)
        
        if not data_product:
            return jsonify({"data": [], "message": "No product found"}), 404
        
        return jsonify({"data": data_product.to_dict()}), 200
        
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@products_bp.route("/<identifier>", methods=["DELETE"])
@roles_required("administrator")
def delete_product(identifier):
    try:
        
        data_product=product_repo.delete(identifier)

        if data_product is None:
            return jsonify({"data": [], "message": "No product found"}), 404

        return jsonify({
            "message": f"Product with ID {identifier} was deleted successfully"
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error while deleting a product."}), 500
    

@products_bp.route("/<identifier>", methods=["PUT"])
@roles_required("administrator")
def update_product(identifier):
    try:
        
        data_product=request.get_json()
    
        updated_product=product_repo.update(
            product_id=identifier,
            name=data_product.get("name"),
            price=data_product.get("price"),
            entry_date=data_product.get("entry_date"),
            quantity=data_product.get("quantity")
        )
        if not updated_product:
            return jsonify({"error": "Product not found"}), 404
        return jsonify({
            "message": f"Product with ID {identifier} was updated successfully"
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error updating product."}), 500


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