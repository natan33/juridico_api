from domain.entities.user import User
from domain.value_objects.email import Email
from domain.repositories.user_repository import UserRepository
from domain.exceptions.domain_error import DomainError


class CreateUserUseCase:

    def __init__(self, user_repository: UserRepository, password_hasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, *, email: str, password: str):
        if self.user_repository.get_by_email(email):
            raise DomainError("Usuário já existe")

        password_hash = self.password_hasher.hash(password)

        user = User(
            user_id=None,
            email=Email(email),
            password_hash=password_hash
        )

        self.user_repository.save(user)
        return user