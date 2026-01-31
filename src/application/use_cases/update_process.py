from domain.repositories.process_repository import ProcessRepository

class UpdateProcessUseCase:
    def __init__(self, process_repo: ProcessRepository):
        self.process_repo = process_repo

    def execute(self, user_id: str, process_id: int, title: str, description: str):
        process = self.process_repo.find_by_id(process_id)

        if not process:
            raise ValueError("Processo não encontrado")

        # validação de dono
        if process.owner_id != user_id:
            raise PermissionError("Usuário não tem permissão para atualizar esse processo")

        # validação simples
        if title is not None:
            process.title = title
        if description is not None:
            process.description = description

        updated = self.process_repo.update(process)
        return updated