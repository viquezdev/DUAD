

def generate_cache_user_key(user_id):
    return f"user:{user_id}"


def generate_cache_users_all_key():
    return "users:all"