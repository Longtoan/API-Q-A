from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.model):
    __tablename__ = "table user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__:
        return '<User> {}'.format(self.username)

    def check_password_hash(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def generate_password_hash(self, password):
        return check_password_hash(self.password, password)


class Question(db.model):
    __tablename__ = "table question"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100), nullable=False)


class Answer(db.Model):
    __tablename__ = "table Answer"
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(100), nullable=False)
