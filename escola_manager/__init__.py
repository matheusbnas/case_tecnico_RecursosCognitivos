from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app():
    # Especifica a pasta de templates
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'auth.login'

    from .models import User

    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registrar blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .routes import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
