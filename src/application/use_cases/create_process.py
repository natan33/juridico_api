from domain.entities.process import LegalProcess
from domain.value_objects.process_number import ProcessNumber
from domain.repositories.process_repository import ProcessRepository


class CreateProcessUseCase:

    def __init__(self, process_repository: ProcessRepository):
        self.process_repository = process_repository

    def execute(self, *, number: str, title: str, owner_id: str):
        process = LegalProcess(
            process_id=None,
            number=ProcessNumber(number),
            title=title,
            owner_id=owner_id
        )

        self.process_repository.save(process)
        return process