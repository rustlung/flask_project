from flask import Flask
from dotenv import load_dotenv

from app.config import get_config
from app.extensions import db, migrate
from app.routes import register_blueprints
import os

load_dotenv()

def create_app():
    env_name = os.getenv('FLASK_ENV', 'development')
    app = Flask(__name__)
    ## Берем нужную конфигурацию из окружения и применяем к приложению
    app.config.from_object(get_config(env_name))
    ## Инициализируем расширения
    db.init_app(app)
    migrate.init_app(app, db)
    ## Регистрируем blueprint'ы
    register_blueprints(app)
    return app


