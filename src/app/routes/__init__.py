from app.routes.status import status
from app.routes.answer import *


def define_routes(app):
    app.register_blueprint(status, url_prefix='/status/')
    app.register_blueprint(answer, url_prefix='/answer/')
