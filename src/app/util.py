import json
from flask_api import status
from flask import Response

def make_response(body, status_code):
    return Response(
        json.dumps(body),
        status=status_code,
        mimetype="application/json"
    )

def make_error(mensage, status_code):
    return Response(
        json.dumps({"error": mensage}),
        status=status_code,
        mimetype="application/json"
    )

STANDARD_ERROR = make_error('Something wrong happened.', status.HTTP_500_INTERNAL_SERVER_ERROR)

METHOD_NOT_DEFINED = make_error('Method not defined', status.HTTP_500_INTERNAL_SERVER_ERROR)
