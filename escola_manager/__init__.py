from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from .models import User  # Importação corrigida

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'auth.login'

    # Registro de Blueprints
    from escola_manager.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from escola_manager.routes import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
