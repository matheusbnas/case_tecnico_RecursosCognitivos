from escola_manager import create_app, db
from escola_manager.models import User, School, Class, Teacher, Student

app = create_app()


def init_db():
    with app.app_context():
        # Garante que todas as tabelas sejam criadas
        db.create_all()

        # Verifica se já existe um usuário admin
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', role='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("Usuário admin criado com sucesso!")

        print("Banco de dados inicializado!")


if __name__ == '__main__':
    init_db()
