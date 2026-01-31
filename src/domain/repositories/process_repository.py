from abc import ABC, abstractmethod
from domain.entities.process import LegalProcess

class ProcessRepository(ABC):

    @abstractmethod
    def save(self, process: LegalProcess):
        pass

    @abstractmethod
    def get_by_id(self, process_id: str) -> LegalProcess:
        pass

    @abstractmethod
    def list_by_owner(self, owner_id: str) -> list[LegalProcess]:
        pass