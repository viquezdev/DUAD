from flask import request, jsonify, Blueprint
from repositories.invoice_products_repository import InvoiceProductsRepository
from repositories.invoice_repository import InvoiceRepository
from services.decorators import roles_required, get_jwt_identity

invoice_product_repo = InvoiceProductsRepository()
invoice_repo = InvoiceRepository()
invoice_products_bp = Blueprint("invoice_products", __name__)


@invoice_products_bp.route("/<invoice_id>/products", methods=["POST"])
@roles_required("administrator", "user")
def create_invoice_product(invoice_id):
    try:
        user_data = get_jwt_identity()
        data = request.get_json()

        required_fields = ["product_id", "quantity", "subtotal"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        invoice_owner_id = invoice_repo.get_user_id(invoice_id)
        if invoice_owner_id is None:
            return jsonify({"error": "Invoice not found"}), 404

        if user_data["role"] == "user" and str(user_data["sub"]) != str(invoice_owner_id):
            return jsonify({"error": "Access denied"}), 403

        new_item = invoice_product_repo.create(
            invoice_id=invoice_id,
            product_id=data["product_id"],
            quantity=data["quantity"],
            subtotal=data["subtotal"]
        )

        if not new_item:
            return jsonify({"error": "Error creating invoice product"}), 400

        return jsonify({
            "message": "Invoice product created successfully",
            "invoice_product": new_item.to_dict()
        }), 201

    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@invoice_products_bp.route("/<invoice_id>/products", methods=["GET"])
@roles_required("administrator", "user")
def get_invoice_products(invoice_id):
    try:
        user_data = get_jwt_identity()
        invoice_owner_id = invoice_repo.get_user_id(invoice_id)
        if invoice_owner_id is None:
            return jsonify({"error": "Invoice not found"}), 404

        if user_data["role"] == "user" and str(user_data["sub"]) != str(invoice_owner_id):
            return jsonify({"error": "Access denied"}), 403

        products = invoice_product_repo.get_by_invoice(invoice_id)
        if not products:
            return jsonify({"data": [], "message": "No products found"}), 404

        return jsonify([product.to_dict() for product in products]), 200

    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@invoice_products_bp.route("/<invoice_id>/products/<product_id>", methods=["PUT"])
@roles_required("administrator", "user")
def update_invoice_product(invoice_id, product_id):
    try:
        user_data = get_jwt_identity()
        data = request.get_json()

        invoice_owner_id = invoice_repo.get_user_id(invoice_id)
        if invoice_owner_id is None:
            return jsonify({"error": "Invoice not found"}), 404

        if user_data["role"] == "user" and str(user_data["sub"]) != str(invoice_owner_id):
            return jsonify({"error": "Access denied"}), 403

        updated_item = invoice_product_repo.update(
            invoice_product_id=product_id,
            invoice_id=invoice_id,
            product_id=data.get("product_id"),
            quantity=data.get("quantity"),
            subtotal=data.get("subtotal")
        )

        if not updated_item:
            return jsonify({"error": "Invoice product not found"}), 404

        return jsonify({
            "message": "Invoice product updated successfully",
            "invoice_product": updated_item.to_dict()
        }), 200

    except Exception as e:
        return jsonify({"error": "Error updating invoice product", "details": str(e)}), 500


@invoice_products_bp.route("/<invoice_product_id>", methods=["DELETE"])
@roles_required("administrator", "user")
def delete_invoice_product(invoice_product_id):
    try:
        user_data = get_jwt_identity()
        
        invoice_product = invoice_product_repo.get_by_id(invoice_product_id)
        if not invoice_product:
            return jsonify({"error": "Invoice product not found"}), 404

        invoice_owner_id = invoice_repo.get_user_id(invoice_product.invoice_id)
        if invoice_owner_id is None:
            return jsonify({"error": "Invoice not found"}), 404

        if user_data["role"] == "user" and str(user_data["sub"]) != str(invoice_owner_id):
            return jsonify({"error": "Access denied"}), 403

        deleted_item = invoice_product_repo.delete(invoice_product_id)
        return jsonify({"message": "Invoice product deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": "Error deleting invoice product", "details": str(e)}), 500
