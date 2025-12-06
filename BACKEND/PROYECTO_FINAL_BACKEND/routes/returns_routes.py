from flask import request,jsonify,Blueprint
from repositories.returns_repository import ReturnsRepository
from repositories.invoice_repository import InvoiceRepository
from repositories.product_repository import ProductRepository
from services.decorators import roles_required,verify_cache,get_jwt_identity
from cache_utils.manager import cache_manager
from cache_utils.return_keys import generate_cache_return_key, generate_cache_returns_all_key


returns_repo=ReturnsRepository()
invoice_repo=InvoiceRepository()
product_repo=ProductRepository()
returns_bp=Blueprint("returns",__name__)


@returns_bp.route("/returns", methods=["GET"])
@roles_required(True)
@verify_cache(cache_manager,key_func=lambda: generate_cache_returns_all_key(
    get_jwt_identity()["sub"],
    "admin" if get_jwt_identity()["is_admin"] else "user"
))
def get_all_returns():
    try:
        user_data=get_jwt_identity()
        if user_data["is_admin"]!=True:
            data_returns = returns_repo.get_by_user_id(user_data["sub"])
        else:
            data_returns = returns_repo.get_all()
        if not data_returns:
            return jsonify({"data": [], "message": "No returns found"}), 404

        serialized = [r.to_dict() for r in data_returns]
        return jsonify(serialized), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@returns_bp.route("/returns/<id>", methods=["GET"])
@roles_required()
@verify_cache(cache_manager,key_func=lambda id: generate_cache_return_key(
    get_jwt_identity()["sub"],
    "admin" if get_jwt_identity()["is_admin"] else "user",
    id
),time_to_live=600)
def get_return_by_id(id):
    try:
        user_data = get_jwt_identity()
        data_return = returns_repo.get_by_id(id)

        if not data_return:
            return jsonify({"error": "Return not found"}), 404


        if user_data["is_admin"] != True and str(user_data["sub"]) != str(data_return.user_id):
            return jsonify({"error": "Access denied"}), 403

        return jsonify({"Return": data_return.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@returns_bp.route("/returns", methods=["POST"])
@roles_required()
def create_return():
    try:
        user_data = get_jwt_identity()
        return_data = request.get_json()

        required_fields = [
            "invoice_id",
            "product_id",
            "quantity_returned",
            "return_date",
            "reason",
            "processed"
        ]

        missing_fields = [field for field in required_fields if field not in return_data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        invoice_id = return_data["invoice_id"]
        product_id = return_data["product_id"]
        quantity = return_data["quantity_returned"]
        processed = return_data["processed"]

        if quantity <= 0:
            return jsonify({"error": "Quantity must be greater than 0"}), 400

        invoice = invoice_repo.get_by_id(invoice_id)
        if not invoice:
            return jsonify({"error": "Invoice not found"}), 404

        if not user_data["is_admin"] and str(user_data["sub"]) != str(invoice.user_id):
            return jsonify({"error": "Access denied"}), 403
    
        product = product_repo.get_by_id(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        if processed is True:
            product.quantity += quantity
            product_repo.update_quantity(product.id, product.quantity)

        new_return = returns_repo.create(
            invoice_id=invoice_id,
            product_id=product_id,
            quantity_returned=quantity,
            return_date=return_data["return_date"],
            reason=return_data["reason"],
            processed=processed
        )

        if not new_return:
            return jsonify({"error": "Error creating return"}), 400

        role = "admin" if user_data["is_admin"] else "user"
        cache_key_user = generate_cache_returns_all_key(user_data["sub"], role)
        cache_manager.delete_data(cache_key_user)

        cache_key_owner = generate_cache_returns_all_key(invoice.user_id, "user")
        cache_manager.delete_data(cache_key_owner)

        return jsonify({
            "message": "Return created successfully",
            "return": new_return.to_dict()
        }), 201
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@returns_bp.route("/returns/<id>", methods=["PUT"])
@roles_required()
def update_return(id):
    try:
        user_data = get_jwt_identity()

        found_return = returns_repo.get_by_id(id)
        if not found_return:
            return jsonify({"error": "Return not found"}), 404

        invoice = invoice_repo.get_by_id(found_return.invoice_id)

        if not user_data["is_admin"] and str(user_data["sub"]) != str(invoice.user_id):
            return jsonify({"error": "Access denied"}), 403

        data = request.get_json()

        if "processed" not in data:
            return jsonify({"error": "Missing field: processed"}), 400

        new_processed = data["processed"]

        if type(new_processed) is not bool:
            return jsonify({"error": "processed must be boolean"}), 400

        product = product_repo.get_by_id(found_return.product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404


        if not found_return.processed and new_processed is True:
            product.quantity += found_return.quantity_returned
            product_repo.update_quantity(product.id, product.quantity)

        updated_return = returns_repo.update(
            id=id,
            processed=new_processed
        )

        role = "admin" if user_data["is_admin"] else "user"
        cache_manager.delete_data(generate_cache_returns_all_key(user_data["sub"], role))
        cache_manager.delete_data(generate_cache_returns_all_key(invoice.user_id, "user"))
        cache_manager.delete_data(generate_cache_return_key(invoice.user_id, role, id))

        return jsonify({
            "message": f"Return {id} updated successfully",
            "return": updated_return.to_dict()
        }), 200

    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

