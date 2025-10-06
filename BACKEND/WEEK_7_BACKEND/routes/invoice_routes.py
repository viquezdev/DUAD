
from flask import request, jsonify, Blueprint
from repositories.invoice_repository import InvoiceRepository
from services.decorators import roles_required, get_jwt_identity

invoice_repo = InvoiceRepository()
invoices_bp = Blueprint("invoices", __name__)


@invoices_bp.route("/", methods=["POST"])
@roles_required("administrator", "user")
def create_invoice():
    try:
        user_data = get_jwt_identity()
        invoice_data = request.get_json()

        required_fields = ["user_id", "total_amount", "invoice_date"]
        missing_fields = [field for field in required_fields if field not in invoice_data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        if user_data["role"] == "user" and str(user_data["sub"]) != str(invoice_data["user_id"]):
            return jsonify({"error": "Access denied"}), 403

        new_invoice = invoice_repo.create(**invoice_data)
        if new_invoice:
            return jsonify({
                "message": "Invoice created successfully",
                "invoice": new_invoice.to_dict()
            }), 201

        return jsonify({"error": "Error creating invoice"}), 400

    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@invoices_bp.route("/", methods=["GET"])
@roles_required("administrator", "user")
def get_all_invoices():
    try:
        user_data = get_jwt_identity()

        if user_data["role"] == "user":
            invoices = invoice_repo.get_by_user(user_data["sub"])
        else:
            invoices = invoice_repo.get_all()

        if not invoices:
            return jsonify({"data": [], "message": "No invoices found"}), 404

        return jsonify([invoice.to_dict() for invoice in invoices]), 200

    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@invoices_bp.route("/<invoice_id>", methods=["GET"])
@roles_required("administrator", "user")
def get_invoice_by_id(invoice_id):
    try:
        user_data = get_jwt_identity()
        invoice = invoice_repo.get_by_id(invoice_id)

        if not invoice:
            return jsonify({"error": "Invoice not found"}), 404


        if user_data["role"] == "user" and str(user_data["sub"]) != str(invoice.user_id):
            return jsonify({"error": "Access denied"}), 403

        return jsonify({"invoice": invoice.to_dict()}), 200

    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@invoices_bp.route("/<invoice_id>", methods=["PUT"])
@roles_required("administrator", "user")
def update_invoice(invoice_id):
    try:
        user_data = get_jwt_identity()
        data = request.get_json()

        invoice_owner_id = invoice_repo.get_user_id(invoice_id)
        if invoice_owner_id is None:
            return jsonify({"error": "Invoice not found"}), 404

        if user_data["role"] == "user" and str(user_data["sub"]) != str(invoice_owner_id):
            return jsonify({"error": "Access denied"}), 403

        updated_invoice = invoice_repo.update(
            invoice_id=invoice_id,
            total_amount=data.get("total_amount"),
            invoice_date=data.get("invoice_date")
        )

        return jsonify({
            "message": f"Invoice with ID {invoice_id} was updated successfully",
            "invoice": updated_invoice.to_dict()
        }), 200

    except Exception as e:
        return jsonify({"error": "Error updating invoice", "details": str(e)}), 500


@invoices_bp.route("/<invoice_id>", methods=["DELETE"])
@roles_required("administrator", "user")
def delete_invoice(invoice_id):
    try:
        user_data = get_jwt_identity()
        invoice_owner_id = invoice_repo.get_user_id(invoice_id)

        if invoice_owner_id is None:
            return jsonify({"error": "Invoice not found"}), 404

        if user_data["role"] == "user" and str(user_data["sub"]) != str(invoice_owner_id):
            return jsonify({"error": "Access denied"}), 403

        invoice_repo.delete(invoice_id)

        return jsonify({
            "message": f"Invoice with ID {invoice_id} was deleted successfully"
        }), 200

    except Exception as e:
        return jsonify({"error": "Error deleting invoice", "details": str(e)}), 500
