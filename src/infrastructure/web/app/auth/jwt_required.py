from functools import wraps
from flask import request, jsonify
from infrastructure.web.app.auth.jwt_service import JwtService
from infrastructure.web.app.utils.response_utils import error_response 


jwt_service = JwtService()

def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization")
        if not auth:
            return error_response(errors={"error": "Token ausente"},status_code=401)

        try:
            token = auth.split(" ")[1]
            payload = jwt_service.decode(token)
            request.user_id = payload["sub"]
        except Exception:
            return error_response(errors={"error": "Token inválido"},status_code=401)

        return fn(*args, **kwargs)
    return wrapper