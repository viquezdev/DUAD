from flask import Blueprint, request, jsonify
from services.decorators import roles_required,get_jwt_identity
from repositories.product_repository import ProductRepository
from repositories.shopping_cart_repository import ShoppingCartRepository
from repositories.shopping_cart_product_repository import ShoppingCartProductRepository
from repositories.invoice_repository import InvoiceRepository
from models.product import Product
from datetime import datetime
from faker import Faker
from db.db import SessionLocal


product_repo = ProductRepository()

shopping_cart_repo = ShoppingCartRepository()

shopping_cart_product_repo =ShoppingCartProductRepository()

invoice_repo = InvoiceRepository()

checkout_bp=Blueprint("checkout",__name__)


@checkout_bp.route("/checkout", methods=["POST"])
@roles_required()
def checkout():
    fake=Faker()
    session=SessionLocal()
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
            product = session.query(Product).filter_by(id=item["id"]).one_or_none()
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
                    f"Insufficient stock for {product.name }"
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

        new_cart=shopping_cart_repo.create(session,user_id=user_data["sub"],status="active",created_at=datetime.utcnow())
        if not new_cart:
            session.rollback()

            return jsonify({
                "error": "Could not create cart"
            }), 500
        for item in validated_products:
            new_cart_product = shopping_cart_product_repo.create(
                session,
                shopping_cart_id=new_cart.id,
                product_id=item["product"].id,
                quantity=item["quantity"]
            )
            if not new_cart_product:
                session.rollback()
                return jsonify({
                    "error": "Could not create cart product"
                }), 500
            item["product"].quantity -= item["quantity"]

        new_invoice = invoice_repo.create(
            session,
            invoice_number=fake.bothify("INV-####-??"),
            user_id=user_data["sub"],
            shopping_cart_id=new_cart.id,
            created_at=datetime.utcnow(),
            billing_address=data["billing_address"],
            payment_method=data["payment_method"],
            payment_status="pending",
            total_amount=total_amount
        )
        if not new_invoice:
            session.rollback()

            return jsonify({
                "error": "Could not create invoice"
            }), 500

        session.commit()

        return jsonify({

            "message":
            "Checkout completed successfully",

            "shopping_cart":
            new_cart.to_dict(),

            "invoice":
            new_invoice.to_dict()

        }), 201
    except Exception as e:

        session.rollback()

        return jsonify({
            "error": "Unexpected error",
            "details": str(e)
        }), 500
    
    finally:

        session.close()
    
