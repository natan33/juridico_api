import bcrypt

class PasswordHasher:
    def __init__(self, rounds: int = 12):
        self.rounds = rounds

    def _normalize(self, password: str) -> bytes:
        # Limite de 72 bytes
        return password.encode("utf-8")[:72]

    def hash(self, password: str) -> str:
        pwd = self._normalize(password)
        hashed = bcrypt.hashpw(pwd, bcrypt.gensalt(self.rounds))
        return hashed.decode("utf-8")

    def verify(self, password: str, password_hash: str) -> bool:
        pwd = self._normalize(password)
        return bcrypt.checkpw(pwd, password_hash.encode("utf-8"))