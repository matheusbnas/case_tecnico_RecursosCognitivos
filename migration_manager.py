from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from escola_manager import create_app, db
# Importar todos os models
from escola_manager.models import School, Class, Teacher, Student, User

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        if db.engine.url.drivername == 'mysql+mysqlconnector':
            db.create_all()  # Isso vai tentar criar as tabelas diretamente
