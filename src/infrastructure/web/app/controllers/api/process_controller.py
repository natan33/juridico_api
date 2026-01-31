from flask import request, jsonify
from . import api
from infrastructure.web.app.core.urls import URL_PROCESSES, URL_PROCESS_UPDATE
from infrastructure.web.app.auth.jwt_required import jwt_required
from infrastructure.persistence.orm.repositories.process_repository import OrmProcessRepository
from infrastructure.persistence.orm.models import ProcessModel
from application.use_cases.create_process import CreateProcessUseCase
from application.use_cases.list_processes import ListProcessesUseCase
from application.use_cases.update_process import UpdateProcessUseCase
from infrastructure.web.app.extensions import db
from infrastructure.web.app.utils.response_utils import success_response, error_response

@api.route(**URL_PROCESSES)
@jwt_required
def list_or_create_process():
    user_id = request.user_id
    repo = OrmProcessRepository(db.session)

    try:
        if request.method == "POST":
            data = request.json
            title = data.get("title")
            number = data.get("number")

            use_case = CreateProcessUseCase(repo)
            process = use_case.execute(
                number=number,
                title=title,
                owner_id=user_id
            )

            return success_response(
                data={
                    "id": process.id,
                    "title": process.title,
                    "number": process.number.value,
                    "owner_id": process.owner_id
                },
                status_code=201
            )

        else:
            use_case = ListProcessesUseCase(repo)
            processes = use_case.execute(owner_id=user_id)

            return success_response(
                            data=[
                    {
                        "id": p.id,
                        "title": p.title,
                        "number": p.number.value,
                        "owner_id": p.owner_id
                    } for p in processes
                ]
            )

    except Exception as e:
        # Imprime no console (para debugar)
        print("ERROR:", str(e))

        # Retorna uma resposta JSON válida
        return error_response(
            code=500,
            message="Erro ao processar a requisição",
            errors=str(e),
            status_code=500
        )


@api.route(**URL_PROCESS_UPDATE)
@jwt_required
def update_process(process_id):
    user_id = request.user_id
    data = request.json

    title = data.get("title")
    description = data.get("description")

    repo = OrmProcessRepository(db.session)
    use_case = UpdateProcessUseCase(repo)

    process = use_case.execute(user_id=user_id, process_id=process_id, title=title, description=description)

    return success_response(data={
        "id": process.id,
        "title": process.title,
        "description": process.description,
        "owner_id": process.owner_id
    })