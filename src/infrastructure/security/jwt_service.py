import jwt
import datetime
import os

SECRET_KEY = os.getenv("JWT_SECRET", "dev-secret")

class JwtService:

    def generate(self, user_id: str) -> str:
        payload = {
            "sub": user_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    def decode(self, token: str) -> dict:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])