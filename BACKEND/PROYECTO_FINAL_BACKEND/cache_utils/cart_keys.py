

def generate_cache_cart_key(cart_id):
    return f"cart:{cart_id}"

def generate_cache_users_all_key():
    return "carts:all"