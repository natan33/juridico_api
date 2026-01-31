import uuid
from datetime import datetime


class ApiResponse:

    def __init__(self, *, code: int, message: str = "", data=None, errors=None, trace_id: str = None):
        self.code = code
        self.message = message
        self.data = data
        self.errors = errors or []
        self.trace_id = trace_id or str(uuid.uuid4())
        self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "code": self.code,
            "trace_id": self.trace_id,
            "message": self.message,
            "data": self.data,
            "errors": self.errors,
            "timestamp": self.timestamp
        }

    # -------------------------
    # Métodos estáticos (factory)
    # -------------------------
    @staticmethod
    def success(data=None, message="Sucesso", code=2000, trace_id=None):
        return ApiResponse(
            code=code,
            message=message,
            data=data,
            trace_id=trace_id,
            errors=[]
        )

    @staticmethod
    def error(message="Erro", errors=None, code=4000, trace_id=None):
        return ApiResponse(
            code=code,
            message=message,
            data=None,
            errors=errors or [],
            trace_id=trace_id
        )
