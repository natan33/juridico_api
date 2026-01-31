import uuid
from domain.entities.process import LegalProcess
from domain.entities.process_status import ProcessStatus
from domain.value_objects.process_number import ProcessNumber
from domain.repositories.process_repository import ProcessRepository
from infrastructure.persistence.orm.models.process import ProcessModel

class OrmProcessRepository(ProcessRepository):

    def __init__(self, session):
        self.session = session

    def save(self, process: LegalProcess):
        if not process.id:
            process.id = str(uuid.uuid4())

        model = ProcessModel(
            id=process.id,
            number=process.number.value,
            title=process.title,
            status=process.status.value,
            owner_id=process.owner_id,
            created_at=process.created_at,   # se vier do domínio
            updated_at=process.updated_at    # se vier do domínio
        )

        self.session.merge(model)
        self.session.commit()

        return process

    def get_by_id(self, process_id: str):
        model = self.session.query(ProcessModel).filter_by(id=process_id).first()
        if not model:
            return None

        return LegalProcess(
            process_id=model.id,
            number=ProcessNumber(model.number),
            title=model.title,
            owner_id=model.owner_id,
            status=ProcessStatus(model.status),
            created_at=model.created_at,
            updated_at=model.updated_at
        )

    def list_by_owner(self, owner_id: str):
        models = self.session.query(ProcessModel).filter_by(owner_id=owner_id).all()

        return [
            LegalProcess(
                id=m.id,
                number=ProcessNumber(m.number),
                title=m.title,
                owner_id=m.owner_id,
                status=ProcessStatus(m.status),
                created_at=m.created_at,
                updated_at=m.updated_at
            )
            for m in models
        ]
    
    def update(self, process: LegalProcess):
        self.session.commit()
        return process
