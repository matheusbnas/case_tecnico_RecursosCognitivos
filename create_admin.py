from escola_manager import create_app, db
from escola_manager.models import User


def create_admin():
    app = create_app()
    with app.app_context():
        if not User.query.filter_by(username='admin').first():
            admin = User(
                username='admin',
                role='admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("Admin user created successfully!")


if __name__ == '__main__':
    create_admin()
