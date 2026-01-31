from flask import request, jsonify
from . import api
from infrastructure.web.app.core.urls import URL_USERS, URL_LOGIN

from infrastructure.persistence.orm.repositories.user_repository import OrmUserRepository
from infrastructure.security.password_hasher import PasswordHasher
from application.use_cases.create_user import CreateUserUseCase
from application.use_cases.authenticate_user import AuthenticateUserUseCase
from infrastructure.web.app.auth.jwt_service import JwtService
from infrastructure.web.app.extensions import db
from infrastructure.web.app.utils.response_utils import success_response, error_response


jwt_service = JwtService()

@api.route(**URL_USERS)
def signup():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    repo = OrmUserRepository(db.session)
    hasher = PasswordHasher()
    use_case = CreateUserUseCase(repo, hasher)

    user = use_case.execute(email=email, password=password)

    return success_response(data={
        "id": user.id,
        "email": user.email.value
    },status_code=201) 


@api.route(**URL_LOGIN)
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    repo = OrmUserRepository(db.session)
    hasher = PasswordHasher()
    use_case = AuthenticateUserUseCase(repo, hasher)

    user = use_case.execute(email=email, password=password)
    token = jwt_service.generate(user.id)

    return success_response(data={"access_token": token},status_code=200)