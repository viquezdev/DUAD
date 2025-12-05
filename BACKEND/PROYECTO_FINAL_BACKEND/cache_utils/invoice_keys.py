

def generate_cache_invoice_key(user_id,role,invoice_id):
    return f"user:{user_id}:role:{role}:invoice:{invoice_id}"

def generate_cache_invoices_all_key(user_id,role):
    return f"user:{user_id}:role:{role}:invoices"