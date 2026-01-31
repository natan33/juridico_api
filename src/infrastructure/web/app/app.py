from flask import Flask
from infrastructure.web.app.extensions import db, bcrypt,migrate
from infrastructure.web.app.core.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from infrastructure.persistence.orm import models

    # Registrar blueprints
    register_blueprints(app)

    return app

def register_blueprints(app):
    from infrastructure.web.app.controllers.api import api
    app.register_blueprint(api)
