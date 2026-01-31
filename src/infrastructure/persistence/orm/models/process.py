from datetime import datetime, timezone
from sqlalchemy import Column, String
from infrastructure.web.app.extensions import db

class ProcessModel(db.Model):
    __tablename__ = "processes"

    id = Column(String, primary_key=True)
    number = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    status = Column(String, nullable=False)
    owner_id = Column(String, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))