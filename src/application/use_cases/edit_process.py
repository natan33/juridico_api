from domain.repositories.process_repository import ProcessRepository


class EditProcessUseCase:

    def __init__(self, process_repository: ProcessRepository):
        self.process_repository = process_repository

    def execute(self, *, process_id: str, owner_id: str, new_title: str):
        process = self.process_repository.get_by_id(process_id)

        if process.owner_id != owner_id:
            raise Exception("Usuário não autorizado")

        process.update_title(new_title)

        self.process_repository.save(process)
        return process