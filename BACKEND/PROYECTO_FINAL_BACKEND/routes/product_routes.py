from flask import request,jsonify,Blueprint
from repositories.product_repository import ProductRepository


product_repo=ProductRepository()
products_bp=Blueprint("products",__name__)


@products_bp.route("/products", methods=["GET"])
def get_all_products():
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@products_bp.route("/products/<id>", methods=["GET"])
def get_product_by_id(product_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@products_bp.route("/products", methods=["POST"])
def create_product():
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@products_bp.route("/products/<id>", methods=["PUT"])
def update_product(product_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@products_bp.route("/products/<id>", methods=["DELETE"])
def delete_product(product_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500