

def generate_cache_active_cart_key(user_id, role):
    return f"user:{user_id}:role:{role}:active_cart"

def generate_cache_carts_all_key(user_id,role):
    return f"user:{user_id}:role:{role}:carts"