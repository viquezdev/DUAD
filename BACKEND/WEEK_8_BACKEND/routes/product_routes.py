
from flask import request, jsonify, Blueprint
from repositories.product_repository import ProductRepository
from services.decorators import roles_required,verify_cache
from services.cache import CacheManager
import json

product_repo = ProductRepository()
products_bp=Blueprint("products",__name__)

cache_manager = CacheManager(
    host="placeholder",
    port=15228,
    password="placeholder",
)

def generate_cache_fruit_key(fruit_id):
    return f'fruit:{fruit_id}'

def generate_cache_fruits_all_key():
    return "fruits:all"



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
            cache_manager.delete_data(generate_cache_fruits_all_key())
            return jsonify({"message":"Product created succesfully"}),201
        return jsonify({"error":"error creating product"}),400 
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@products_bp.route("/", methods=["GET"])
@roles_required("administrator","user")
@verify_cache(cache_manager,key_func=lambda:generate_cache_fruits_all_key())
def get_all_products():
    try:
        data_products = product_repo.get_all()
        if not data_products:
            return jsonify({"data": [], "message": "No products found"}), 404

        serialized = [p.to_dict() for p in data_products]
        return jsonify(serialized), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@products_bp.route("/<int:fruit_id>", methods=["GET"])
@roles_required("administrator","user")
@verify_cache(cache_manager,key_func=lambda fruit_id:generate_cache_fruit_key(fruit_id),time_to_live=600)
def get_by_id(fruit_id):
    try:
        data_product=product_repo.get_by_id(fruit_id)
        
        if not data_product:
            return jsonify({"data": [], "message": "No product found"}), 404
        
        serialized=data_product.to_dict()
        return jsonify(serialized), 200
        
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@products_bp.route("/<identifier>", methods=["DELETE"])
@roles_required("administrator")
def delete_product(identifier):
    try:
        
        data_product=product_repo.delete(identifier)

        if data_product is None:
            return jsonify({"data": [], "message": "No product found"}), 404
        
        cache_manager.delete_data(generate_cache_fruit_key(identifier))
        cache_manager.delete_data(generate_cache_fruits_all_key())
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
        cache_manager.delete_data(generate_cache_fruit_key(identifier))
        cache_manager.delete_data(generate_cache_fruits_all_key())
        return jsonify({
            "message": f"Product with ID {identifier} was updated successfully"
        }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error updating product."}), 500


