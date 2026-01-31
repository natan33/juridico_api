from flask import Blueprint


api = Blueprint("api", __name__, url_prefix="/api")

from . import process_controller
from . import user_controller