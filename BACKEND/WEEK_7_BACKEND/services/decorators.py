from functools import wraps
from flask import request, jsonify
from services.jwt_manager import jwt_manager 

def roles_required(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                return jsonify({"error": "Token required"}), 401

            token = auth_header.split(" ")[1]
            try:
                payload = jwt_manager.decode(token)
                user_role = payload.get("role")
                if user_role not in allowed_roles:
                    return jsonify({"error": "Access denied"}), 403
            except Exception as e:
                return jsonify({"error": "Invalid token", "details": str(e)}), 401

            return f(*args, **kwargs)
        return wrapper
    return decorator