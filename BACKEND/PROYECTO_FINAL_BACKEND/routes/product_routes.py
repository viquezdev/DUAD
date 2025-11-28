from flask import request,jsonify,Blueprint
from repositories.product_repository import ProductRepository
from services.decorators import roles_required,verify_cache
from cache_utils.manager import cache_manager
from cache_utils.product_keys import generate_cache_product_key, generate_cache_products_all_key
import json


product_repo=ProductRepository()
products_bp=Blueprint("products",__name__)




@products_bp.route("/products", methods=["GET"])
@roles_required()
@verify_cache(cache_manager,key_func=lambda:generate_cache_products_all_key())
def get_all_products():
    try:
        data_products = product_repo.get_all()
        if not data_products:
            return jsonify({"data": [], "message": "No products found"}), 404

        serialized = [p.to_dict() for p in data_products]
        return jsonify(serialized), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@products_bp.route("/products/<id>", methods=["GET"])
@roles_required()
@verify_cache(cache_manager,key_func=lambda id:generate_cache_product_key(id),time_to_live=600)
def get_product_by_id(id):
    try:
        data_product=product_repo.get_by_id(id)
        if not data_product:
            return jsonify({"data": [], "message": "No product found"}), 404
        serialized=data_product.to_dict()
        return jsonify(serialized), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@products_bp.route("/products", methods=["POST"])
@roles_required(True)
def create_product():
    try:
        product_data=request.get_json()
        required_fields = ["sku", "name","price","description","quantity"]
        missing_fields = [field for field in required_fields if field not in product_data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        new_product=product_repo.create(**product_data)
        if new_product:
            cache_manager.delete_data(generate_cache_products_all_key())
            return jsonify({"message":"Product created succesfully"}),201
        return jsonify({"error":"error creating product"}),400 
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@products_bp.route("/products/<id>", methods=["PUT"])
@roles_required(True)
def update_product(id):
    try:
        data_product=request.get_json()
    
        updated_product=product_repo.update(
            id=id,
            sku=data_product.get("sku"),
            name=data_product.get("name"),
            price=data_product.get("price"),
            description=data_product.get("description"),
            quantity=data_product.get("quantity")
        )
        if not updated_product:
            return jsonify({"error": "Product not found"}), 404
        cache_manager.delete_data(generate_cache_product_key(id))
        cache_manager.delete_data(generate_cache_products_all_key())
        return jsonify({
            "message": f"Product with ID {id} was updated successfully"
        }), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@products_bp.route("/products/<id>", methods=["DELETE"])
@roles_required(True)
def delete_product(id):
    try:
        data_product=product_repo.delete(id)

        if data_product is None:
            return jsonify({"data": [], "message": "No product found"}), 404
        
        cache_manager.delete_data(generate_cache_product_key(id))
        cache_manager.delete_data(generate_cache_products_all_key())
        return jsonify({
            "message": f"Product with ID {id} was deleted successfully"
        }), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500