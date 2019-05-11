from app import application
from app.models import db


class User(db.Model):
    __tablename__ = 'users'

    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
