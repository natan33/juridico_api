import jwt
from datetime import datetime, timezone, timedelta
from flask import current_app

class JwtService:

    def generate(self, user_id: str) -> str:
        payload = {
            "sub": user_id,
            "exp": datetime.now(timezone.utc) + timedelta(hours=1)
        }
        secret = current_app.config["JWT_SECRET"]
        return jwt.encode(payload, secret, algorithm="HS256")

    def decode(self, token: str) -> dict:
        secret = current_app.config["JWT_SECRET"]
        return jwt.decode(token, secret, algorithms=["HS256"])