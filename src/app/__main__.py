from flask import Flask
from flask_cors import CORS

from app.routes import define_routes

def create_app():
    app = Flask(__name__)

    define_routes(app)
    CORS(app, support_credentials=True)

    @app.after_request
    def cors(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    
    return app
