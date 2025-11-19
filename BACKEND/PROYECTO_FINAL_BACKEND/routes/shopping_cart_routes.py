from flask import request,jsonify,Blueprint
from repositories.shopping_cart_repository import ShoppingCart
from repositories.shopping_cart_product_repository import ShoppingCartProduct


shopping_cart_repo=ShoppingCart()
shopping_cart_product_repo=ShoppingCartProduct()
shopping_carts_bp=Blueprint("shopping_carts",__name__)


@shopping_carts_bp.route("/shopping_carts", methods=["GET"])
def get_all_carts():
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts/<id>", methods=["GET"])
def get_cart_by_id(cart_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts", methods=["POST"])
def create_cart():
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts/<id>", methods=["PUT"])
def update_cart(cart_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts/<id>", methods=["DELETE"])
def delete_cart(cart_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@shopping_carts_bp.route("/shopping_carts/<cart_id>/products", methods=["GET"])
def get_all_cart_products():
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts/<cart_id>/products", methods=["POST"])
def add_product_to_cart():
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts/<cart_id>/products/<product_id>", methods=["PATCH"])
def update_product_quantity_in_modify_cart(cart_id,product_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts/<cart_id>/products/<product_id>", methods=["DELETE"])
def remove_product_from_cart(cart_id,product_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500