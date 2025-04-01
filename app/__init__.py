from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        # Importa las rutas para registrarlas
        from . import routes

    return app
