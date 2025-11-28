

def generate_cache_invoice_key(invoice_id):
    return f"invoice:{invoice_id}"


def generate_cache_invoices_all_key():
    return "invoices:all"