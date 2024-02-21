from flask import Blueprint, request
from flask_cors import cross_origin
from app.util import METHOD_NOT_DEFINED
from app.controllers import answer as controller

answer = Blueprint('answer', __name__)

@answer.route("", methods=["POST"])
@cross_origin(supports_credentials=True)
def route_answer():
    if request.method == "POST":
        return controller.get_answer(request)
    
    return METHOD_NOT_DEFINED
