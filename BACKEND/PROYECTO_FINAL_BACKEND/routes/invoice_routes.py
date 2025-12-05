from flask import request,jsonify,Blueprint
from repositories.invoice_repository import InvoiceRepository
from services.decorators import roles_required,verify_cache,get_jwt_identity
from cache_utils.manager import cache_manager
from cache_utils.invoice_keys import generate_cache_invoice_key, generate_cache_invoices_all_key


invoice_repo=InvoiceRepository()
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
def create_invoice():
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@invoices_bp.route("/invoices/<id>", methods=["PUT"])
def update_invoice(invoice_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@invoices_bp.route("/invoices/<id>", methods=["DELETE"])
def delete_invoice(invoice_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500