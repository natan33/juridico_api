from domain.repositories.process_repository import ProcessRepository


class ListProcessesUseCase:

    def __init__(self, process_repository: ProcessRepository):
        self.process_repository = process_repository

    def execute(self, *, owner_id: str):
        return self.process_repository.list_by_owner(owner_id)