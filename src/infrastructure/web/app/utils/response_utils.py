from flask import jsonify
from infrastructure.web.app.responses.api_response import ApiResponse


def success_response(data=None, message="Sucesso", code=2000, status_code=200, trace_id=None):
    response = ApiResponse.success(
        data=data,
        message=message,
        code=code,
        trace_id=trace_id
    )
    return jsonify(response.to_dict()), status_code


def error_response(message="Erro", errors=None, code=4000, status_code=400, trace_id=None):
    response = ApiResponse.error(
        message=message,
        errors=errors,
        code=code,
        trace_id=trace_id
    )
    return jsonify(response.to_dict()), status_code
