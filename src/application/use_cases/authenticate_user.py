from domain.repositories.user_repository import UserRepository
from domain.exceptions.domain_error import DomainError


class AuthenticateUserUseCase:

    def __init__(self, user_repository: UserRepository, password_hasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, *, email: str, password: str):
        user = self.user_repository.get_by_email(email)

        if not user:
            raise DomainError("Credenciais inválidas")

        if not self.password_hasher.verify(password, user.password_hash):
            raise DomainError("Credenciais inválidas")

        return user