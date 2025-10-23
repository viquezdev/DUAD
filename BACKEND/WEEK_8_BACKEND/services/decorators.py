from functools import wraps
from flask import request, jsonify,g
from services.jwt_manager import jwt_manager 
from services.cache import CacheManager
import json

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


def verify_cache(cache_manager,key_func,time_to_live=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args,**kwargs):
            key=key_func(*args,**kwargs)
            if cache_manager.check_key(key):
                cached_data=cache_manager.get_data(key)
                if cached_data:
                    if time_to_live:
                        cache_manager.refresh_ttl(key, time_to_live)
                    data=json.loads(cached_data)
                    return jsonify(data),200
        
            response= f(*args,**kwargs)
            try:
                if isinstance(response, tuple) and len(response) == 2:
                    resp_json, status = response
                    if hasattr(resp_json, "get_json") and status == 200:
                        cache_manager.store_data(key, json.dumps(resp_json.get_json()), time_to_live)
                else:
                    if hasattr(response, "get_json"):
                        cache_manager.store_data(key, json.dumps(response.get_json()), time_to_live)
            except Exception:
                pass
            return response
        return wrapper
    return decorator