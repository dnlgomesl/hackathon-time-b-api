from flask import Flask
from flask_cors import CORS

from app.routes import define_routes

def create_app():
    app = Flask(__name__)

    define_routes(app)
    CORS(app, support_credentials=True)
    
    return app
