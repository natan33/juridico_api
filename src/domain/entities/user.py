from datetime import datetime
from domain.value_objects.email import Email

class User:
    def __init__(self, user_id:str, email:Email, 
                 password_hash: str, 
                 is_admin:bool,
                 created_at: datetime,
                 updated_at: datetime):
        self.id = user_id
        self.email = email
        self.password_hash = password_hash
        self.is_admin = is_admin
        self.created_at = created_at
        self.updated_at = updated_at