# escola_manager/__init__.py
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'auth.login'

    # Importe os blueprints usando o nome do pacote
    from escola_manager.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from escola_manager.routes import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
