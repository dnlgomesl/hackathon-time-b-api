from flask_api import status as flask_status
from app.util import make_response, make_error
from app.services import answer as service

def get_answer(request):
    try:
        body = request.get_json()
        if "question" in body:
            question = str(body["question"])
            answer_question = service.answer_question(question)
            return make_response(answer_question, flask_status.HTTP_201_CREATED)
        else:
            return make_error(f'Something wrong happened: No valid body.', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return make_error(f'Something wrong happened: {str(e)}', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)