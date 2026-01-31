from abc import ABC,abstractmethod
from domain.entities.user import User

class UserRepository(ABC):

    @abstractmethod
    def save(self, user:User):
        pass

    @abstractmethod
    def get_by_email(self, email:str) -> User:
        pass
