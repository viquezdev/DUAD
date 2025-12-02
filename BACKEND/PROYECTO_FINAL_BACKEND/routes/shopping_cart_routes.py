from flask import request,jsonify,Blueprint
from repositories.shopping_cart_repository import ShoppingCartRepository
from repositories.product_repository import ProductRepository
from repositories.shopping_cart_product_repository import ShoppingCartProduct
from services.decorators import roles_required,verify_cache,get_jwt_identity
from cache_utils.manager import cache_manager
from cache_utils.cart_keys import generate_cache_cart_key, generate_cache_carts_all_key


shopping_cart_repo=ShoppingCartRepository()
product_repo=ProductRepository()
shopping_cart_product_repo=ShoppingCartProduct()
shopping_carts_bp=Blueprint("shopping_carts",__name__)


@shopping_carts_bp.route("/shopping_carts", methods=["GET"])
@roles_required(True)
@verify_cache(cache_manager,key_func=lambda: generate_cache_carts_all_key(
    get_jwt_identity()["sub"],
    "admin" if get_jwt_identity()["is_admin"] else "user"
))
def get_all_carts():
    try:
        user_data=get_jwt_identity()
        if user_data["is_admin"]!=True:
            data_carts = shopping_cart_repo.get_by_user_id(user_data["sub"])
        else:
            data_carts = shopping_cart_repo.get_all()
        if not data_carts:
            return jsonify({"data": [], "message": "No carts found"}), 404

        serialized = [c.to_dict() for c in data_carts]
        return jsonify(serialized), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts/<id>", methods=["GET"])
@roles_required()
@verify_cache(cache_manager,key_func=lambda id: generate_cache_cart_key(
    get_jwt_identity()["sub"],
    "admin" if get_jwt_identity()["is_admin"] else "user",
    id
),time_to_live=600)
def get_cart_by_id(id):
    try:
        user_data = get_jwt_identity()
        data_cart = shopping_cart_repo.get_by_id(id)

        if not data_cart:
            return jsonify({"error": "Cart not found"}), 404


        if user_data["is_admin"] != True and str(user_data["sub"]) != str(data_cart.user_id):
            return jsonify({"error": "Access denied"}), 403

        return jsonify({"Shopping Cart": data_cart.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts", methods=["POST"])
@roles_required()
def create_cart():
    try:
        user_data = get_jwt_identity()
        cart_data = request.get_json()

        required_fields = ["user_id", "status", "created_at"]
        missing_fields = [field for field in required_fields if field not in cart_data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        new_shopping_cart = shopping_cart_repo.create(**cart_data)
        request_user_role = "admin" if user_data["is_admin"] else "user"
        cache_key_requester = generate_cache_carts_all_key(
            user_data["sub"],
            request_user_role
        )
        cache_manager.delete_data(cache_key_requester)

        owner_user_id = cart_data["user_id"]
        cache_key_owner = generate_cache_carts_all_key(
            owner_user_id,
            "user"   
        )
        cache_manager.delete_data(cache_key_owner)

        return jsonify({
            "message": "Shopping cart created successfully",
            "shopping_cart": new_shopping_cart.to_dict()
        }), 201
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts/<id>", methods=["PUT"])
@roles_required()
def update_cart(id):
    try:
        user_data = get_jwt_identity()
        data_cart=shopping_cart_repo.get_by_id(id)
        if not data_cart:
            return jsonify({"error": "Shopping cart not found"}), 404
        if user_data["is_admin"] != True and str(user_data["sub"]) != str(data_cart.user_id):
            return jsonify({"error": "Access denied"}), 403
        update_data = request.get_json()
        updated_cart=shopping_cart_repo.update(
            id=id,
            user_id=update_data.get("user_id", data_cart.user_id),
            status=update_data.get("status", data_cart.status),
            created_at=update_data.get("created_at", data_cart.created_at)
        )
        if not updated_cart:
            return jsonify({"error": "Update failed"}), 404
        requester_role = "admin" if user_data["is_admin"] else "user"
        cache_key_requester = generate_cache_carts_all_key(
            user_data["sub"], requester_role
        )
        cache_manager.delete_data(cache_key_requester)
        owner_user_id = data_cart.user_id
        cache_key_owner = generate_cache_carts_all_key(
            owner_user_id, "user"
        )
        cache_manager.delete_data(cache_key_owner)
        cache_key_cart = generate_cache_cart_key(
            owner_user_id,"user", id
        )
        cache_manager.delete_data(cache_key_cart)
        return jsonify({
            "message": f"Shopping cart with ID {id} updated successfully",
            "shopping_cart": updated_cart.to_dict()
        }), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts/<id>", methods=["DELETE"])
@roles_required()
def delete_cart(id):
    try:
        user_data = get_jwt_identity()
        data_cart = shopping_cart_repo.get_by_id(id)
        if not data_cart:
            return jsonify({"error": "Shopping cart not found"}), 404
        if user_data["is_admin"] != True and str(user_data["sub"]) != str(data_cart.user_id):
            return jsonify({"error": "Access denied"}), 403
        deleted = shopping_cart_repo.delete(id)
        if not deleted:
            return jsonify({"error": "Delete failed"}), 400
        requester_role = "admin" if user_data["is_admin"] else "user"
        cache_key_requester = generate_cache_carts_all_key(
            user_data["sub"], requester_role
        )
        cache_manager.delete_data(cache_key_requester)
        owner_user_id = data_cart.user_id
        cache_key_owner = generate_cache_carts_all_key(
            owner_user_id, "user"
        )
        cache_manager.delete_data(cache_key_owner)
        cache_key_cart = generate_cache_cart_key(
            owner_user_id,"user", id
        )
        cache_manager.delete_data(cache_key_cart)
        return jsonify({
            "message": f"Shopping cart with ID {id} was deleted successfully"
        }), 200 
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


@shopping_carts_bp.route("/shopping_carts/<cart_id>/products", methods=["GET"])
@roles_required()
def get_all_cart_products(cart_id):
    try:
        user_data = get_jwt_identity()
        shopping_cart = shopping_cart_repo.get_by_id(cart_id)
        if not shopping_cart:
            return jsonify({"error": "Shopping cart not found"}), 404
        if not user_data["is_admin"] and str(user_data["sub"]) != str(shopping_cart.user_id):
            return jsonify({"error": "Access denied"}), 403
        data_products_cart = shopping_cart_product_repo.get_by_shopping_cart_id(cart_id)
        if not data_products_cart:
            return jsonify({"data": [], "message": "No products found"}), 404
        serialized = [p.to_dict() for p in data_products_cart]
        return jsonify(serialized), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts/<cart_id>/products", methods=["POST"])
@roles_required()
def add_product_to_cart(cart_id):
    try:
        user_data = get_jwt_identity()

        shopping_cart = shopping_cart_repo.get_by_id(cart_id)

        if not shopping_cart:
            return jsonify({"error": "Shopping cart not found"}), 404
        
        if not user_data["is_admin"] and str(user_data["sub"]) != str(shopping_cart.user_id):
            return jsonify({"error": "Access denied"}), 403
        
        product_data = request.get_json()
        required_fields = ["product_id", "quantity"]
        missing = [f for f in required_fields if f not in product_data]
        if missing:
            return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400
        
        product = product_repo.get_by_id(product_data["product_id"])
        if not product:
            return jsonify({"error": "Product not found"}), 404
        
        desired_quantity = product_data["quantity"]
        if product.stock < desired_quantity:
            return jsonify({"error": "Not enough stock"}), 400

        existing = shopping_cart_product_repo.get_product_in_cart(cart_id, product.id)

        if existing:
            new_quantity = existing.quantity + desired_quantity

            if product.stock < new_quantity:
                return jsonify({"error": "Not enough stock to increase quantity"}), 400

            updated_item = shopping_cart_product_repo.update_quantity(
                cart_product_id=existing.id,
                quantity=new_quantity
            )

            return jsonify(updated_item.to_dict()), 200

        else:
            new_item = shopping_cart_product_repo.create(
                shopping_cart_id=cart_id,
                product_id=product.id,
                quantity=desired_quantity
            )

            return jsonify(new_item.to_dict()), 201

    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts/<cart_id>/products/<product_id>", methods=["PATCH"])
@roles_required()
def update_product_quantity_in_modify_cart(cart_id,product_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@shopping_carts_bp.route("/shopping_carts/<cart_id>/products/<product_id>", methods=["DELETE"])
@roles_required(True)
def remove_product_from_cart(cart_id,product_id):
    try:
        pass
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500