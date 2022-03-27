from project.dao.models.base import BaseMixin
from project.setup_db import db


class User(BaseMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), unique=True)
    surname = db.Column(db.String(100), unique=True)
    favorite_genre = db.Column(db.String(100))
    role = db.Column(db.String(50), default="user")


    def __repr__(self):
        return f"<User '{self.name.title()}'>"
