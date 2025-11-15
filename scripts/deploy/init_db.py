from app import create_app, db
from app.models.models import User, Challenge

app = create_app()

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()
    print("Creating all tables...")
    db.create_all()
    print("Database initialized successfully.")

    # Add a test user
    test_user = User(username='admin', password_hash='placeholder_hash')
    db.session.add(test_user)

    # Add a test challenge
    test_challenge = Challenge(title='Test Challenge', category='misc', description='A simple test challenge.', flag='flag{test_challenge}', points=100)
    db.session.add(test_challenge)

    db.session.commit()
    print("Test user and challenge created.")
