from flask import Blueprint, request, jsonify
from services.decorators import roles_required,get_jwt_identity
from repositories.product_repository import ProductRepository
from repositories.shopping_cart_repository import ShoppingCartRepository
from repositories.shopping_cart_product_repository import ShoppingCartProductRepository
from repositories.invoice_repository import InvoiceRepository
from db.db import SessionLocal


product_repo = ProductRepository()

shopping_cart_repo = ShoppingCartRepository()

shopping_cart_product_repo =ShoppingCartProductRepository()

invoice_repo = InvoiceRepository()

checkout_bp=Blueprint("checkout",__name__)


@checkout_bp.route("/checkout", methods=["POST"])
@roles_required(True)
def checkout():

    try:
        user_data=get_jwt_identity()

        data = request.get_json()

        required_fields = ["billing_address","payment_method","products"]
        missing_fields = [
            field for field in required_fields
            if field not in data
        ]
        if missing_fields:
            return jsonify({
                "error":
                f"Missing fields: {', '.join(missing_fields)}"
            }), 400
        
        products = data["products"]
        if len(products) == 0:
            return jsonify({"error": "Cart is empty"}), 400
        
        total_amount=0
        validated_products=[]

        for item in products:
            product = product_repo.get_by_id(item["id"])
            if not product:
                return jsonify({"error": f"Product {item['id']} not found"}), 404
            if item["quantity"] <= 0:
                return jsonify({
                    "error":
                    "Quantity must be greater than 0"
                }), 400
            if item["quantity"] > product.quantity:
                return jsonify({
                    "error":
                    f"Insufficient stock for {product.name}"
                }), 400
            subtotal = (
                product.price * item["quantity"]
            )
            total_amount += subtotal
            validated_products.append({

                "product": product,

                "quantity": item["quantity"],

                "subtotal": subtotal
            })