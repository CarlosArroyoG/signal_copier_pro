from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from database import db
from api import api_bp
from logging_config import configure_logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(api_bp, url_prefix='/api')

    configure_logging(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)