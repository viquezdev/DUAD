

def generate_cache_cart_key(user_id,role,cart_id):
    return f"user:{user_id}:role:{role}:cart:{cart_id}"

def generate_cache_carts_all_key(user_id,role):
    return f"user:{user_id}:role:{role}:carts"