from flask import Blueprint

api_bp_v1 = Blueprint("api", __name__, template_folder="templates")

from . import routes
