from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    score = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.username}>'

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    flag = db.Column(db.String(120), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    solved_by = db.relationship('User', secondary='solved_challenges', backref='solved_challenges')

# Association table for the many-to-many relationship between Users and Challenges
solved_challenges = db.Table('solved_challenges',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('challenge_id', db.Integer, db.ForeignKey('challenge.id'), primary_key=True)
)
