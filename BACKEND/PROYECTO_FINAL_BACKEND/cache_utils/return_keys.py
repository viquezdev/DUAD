

def generate_cache_return_key(user_id,role,return_id):
    return f"user:{user_id}:role:{role}:return:{return_id}"

def generate_cache_returns_all_key(user_id,role):
    return f"user:{user_id}:role:{role}:return"