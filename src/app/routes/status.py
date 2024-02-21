import time
from flask import Blueprint
from flask_api import status as flask_status
from app.util import make_response
from __version__ import __version__
from flask_cors import cross_origin

START_TIMESTAMP = int(time.time())

status = Blueprint('status', __name__)

@status.route("", methods=["GET"])
@cross_origin(supports_credentials=True)
def main():
    status_msg = {
        "status": "online",
        "timestamp": int(time.time()),
        "started": START_TIMESTAMP,
        "service": "api",
        "version": __version__
    }

    return make_response(status_msg, flask_status.HTTP_200_OK)
