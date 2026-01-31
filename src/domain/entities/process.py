from domain.entities.process_status import ProcessStatus
from domain.value_objects.process_number import ProcessNumber
from domain.exceptions.process_errors import ProcessClosedError
from datetime import datetime

class LegalProcess:
    def __init__(
            self,
            id:str,
            number: ProcessNumber,
            title:str,
            owner_id:str,
            status: ProcessStatus = ProcessStatus.ABERTO,
            created_at: datetime  = None,
            updated_at: datetime  = None
            ):
        self.id = id
        self.number = number
        self.title = title
        self.owner_id = owner_id
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def update_title(self, new_title: str):
        if self.status == ProcessStatus.ENCERRADO:
            raise ProcessClosedError("Processo encerrado não pode ser alterado")
        self.title = new_title

    def close(self):
        self.status = ProcessStatus.ENCERRADO