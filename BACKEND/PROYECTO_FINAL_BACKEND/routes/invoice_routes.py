from flask import request,jsonify,Blueprint
from repositories.invoice_repository import InvoiceRepository
from repositories.shopping_cart_repository import ShoppingCartRepository
from repositories.shopping_cart_product_repository import ShoppingCartProductRepository
from repositories.product_repository import ProductRepository
from services.decorators import roles_required,verify_cache,get_jwt_identity
from cache_utils.manager import cache_manager
from cache_utils.invoice_keys import generate_cache_invoice_key, generate_cache_invoices_all_key


invoice_repo=InvoiceRepository()
shopping_cart_repo=ShoppingCartRepository()
shopping_cart_product_repo=ShoppingCartProductRepository()
product_repo=ProductRepository()
invoices_bp=Blueprint("invoices",__name__)


@invoices_bp.route("/invoices", methods=["GET"])

@roles_required(True)
@verify_cache(cache_manager,key_func=lambda: generate_cache_invoices_all_key(
    get_jwt_identity()["sub"],
    "admin" if get_jwt_identity()["is_admin"] else "user"
))
def get_all_invoices():
    try:
        user_data=get_jwt_identity()
        if user_data["is_admin"]!=True:
            data_invoices = invoice_repo.get_by_user_id(user_data["sub"])
        else:
            data_invoices = invoice_repo.get_all()
        if not data_invoices:
            return jsonify({"data": [], "message": "No invoices found"}), 404

        serialized = [i.to_dict() for i in data_invoices]
        return jsonify(serialized), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@invoices_bp.route("/invoices/<id>", methods=["GET"])
@roles_required()
@verify_cache(cache_manager,key_func=lambda id: generate_cache_invoice_key(
    get_jwt_identity()["sub"],
    "admin" if get_jwt_identity()["is_admin"] else "user",
    id
),time_to_live=600)
def get_invoice_by_id(id):
    try:
        user_data = get_jwt_identity()
        data_invoice = invoice_repo.get_by_id(id)

        if not data_invoice:
            return jsonify({"error": "Invoice not found"}), 404


        if user_data["is_admin"] != True and str(user_data["sub"]) != str(data_invoice.user_id):
            return jsonify({"error": "Access denied"}), 403

        return jsonify({"Shopping Cart": data_invoice.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@invoices_bp.route("/invoices", methods=["POST"])
@roles_required(True)
def create_invoice():
    try:
        user_data = get_jwt_identity()
        invoice_data = request.get_json()

        required_fields = [
            "invoice_number",
            "user_id",
            "shopping_cart_id",
            "created_at",
            "billing_address",
            "payment_method",
            "payment_status"
        ]

        missing_fields = [f for f in required_fields if f not in invoice_data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        shopping_cart = shopping_cart_repo.get_by_id(invoice_data["shopping_cart_id"])
        if not shopping_cart:
            return jsonify({"error": "Shopping cart not found"}), 404

        if not user_data["is_admin"] and str(user_data["sub"]) != str(shopping_cart.user_id):
            return jsonify({"error": "Access denied"}), 403

        if shopping_cart.status != "completed":
            return jsonify({"error": "Shopping cart must be 'completed' before invoicing"}), 400

        cart_products = shopping_cart_product_repo.get_by_shopping_cart_id(shopping_cart.id)

        if not cart_products:
            return jsonify({"error": "This cart has no products"}), 400

        total = 0

        for cp in cart_products:

            product = product_repo.get_by_id(cp.product_id)
            if not product:
                return jsonify({"error": f"Product {cp.product_id} not found"}), 404

            if product.quantity < cp.quantity:
                return jsonify({"error": f"Not enough stock for product {product.id}"}), 400

            total += cp.subtotal

        invoice_data["total_amount"] = total


        new_invoice = invoice_repo.create(**invoice_data)

        for cp in cart_products:
            product = product_repo.get_by_id(cp.product_id)
            product_repo.update(
                id=product.id,
                quantity=product.quantity - cp.quantity
            )

        shopping_cart_repo.update(
            id=shopping_cart.id,
            status="invoiced"
        )

        role = "admin" if user_data["is_admin"] else "user"
        cache_manager.delete_data(generate_cache_invoices_all_key(user_data["sub"], role))
        cache_manager.delete_data(generate_cache_invoices_all_key(invoice_data["user_id"], "user"))

        return jsonify({
            "message": "Invoice created successfully",
            "invoice": new_invoice.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    