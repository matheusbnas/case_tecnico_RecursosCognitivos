from escola_manager import create_app, db
from escola_manager.models import User

app = create_app()

with app.app_context():
    # Cria todas as tabelas
    db.create_all()

    # Opcional: Cria um usuário admin inicial
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin')
        admin.set_password('admin123')  # Altere para uma senha segura
        admin.role = 'admin'
        db.session.add(admin)
        db.session.commit()
