import uuid
from domain.entities.user import User
from domain.value_objects.email import Email
from domain.repositories.user_repository import UserRepository
from infrastructure.persistence.orm.models import UserModel


class OrmUserRepository(UserRepository):

    def __init__(self, session):
        self.session = session

    def save(self, user: User):
        if not user.id:
            user.id = str(uuid.uuid4())

        model = UserModel(
            id=user.id,
            email=user.email.value,
            password_hash=user.password_hash,
            created_at=user.created_at,
            updated_at=user.updated_at
        )

        # merge evita duplicação e funciona para update
        self.session.merge(model)
        self.session.commit()

        return user

    def get_by_email(self, email: str):
        model = self.session.query(UserModel).filter_by(email=email).first()
        if not model:
            return None

        return User(
            user_id=model.id,
            email=Email(model.email),
            password_hash=model.password_hash,
            is_admin=model.is_admin, 
            created_at=model.created_at,
            updated_at=model.updated_at
        )
