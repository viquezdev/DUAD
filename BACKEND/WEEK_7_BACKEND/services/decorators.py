from functools import wraps
from flask import request, jsonify,g
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
                if not payload:
                    return jsonify({"error": "Invalid token"}), 401
                user_role = payload.get("role")
                if user_role not in allowed_roles:
                    return jsonify({"error": "Access denied"}), 403
            
                g.current_user=payload
            except Exception as e:
                return jsonify({"error": "Invalid token", "details": str(e)}), 401

            return f(*args, **kwargs)
        return wrapper
    return decorator


def get_jwt_identity():
    return getattr(g, "current_user", None)