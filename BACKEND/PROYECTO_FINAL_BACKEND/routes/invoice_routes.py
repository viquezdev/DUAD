from flask import request,jsonify,Blueprint
from repositories.invoice_repository import InvoiceRepository
from services.decorators import roles_required,verify_cache
from cache_utils.manager import cache_manager
from cache_utils.invoice_keys import generate_cache_invoice_key, generate_cache_invoices_all_key


invoice_repo=InvoiceRepository()
invoices_bp=Blueprint("invoices",__name__)


@invoices_bp.route("/invoices", methods=["GET"])
def get_all_invoices():
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@invoices_bp.route("/invoices/<id>", methods=["GET"])
def get_invoice_by_id(invoice_id):
    try:
        pass
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