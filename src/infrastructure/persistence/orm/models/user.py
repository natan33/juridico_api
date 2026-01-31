from datetime import datetime, timezone
import uuid
from sqlalchemy import Column, String
from infrastructure.web.app.extensions import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))