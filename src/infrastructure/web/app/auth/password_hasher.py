from infrastructure.web.app.extensions import bcrypt

class PasswordHasher:

    def hash(self, password: str) -> str:
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def verify(self, password: str, password_hash: str) -> bool:
        return bcrypt.check_password_hash(password_hash, password)
