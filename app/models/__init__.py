from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from app import application


class RecordNotFoundError(Exception):
    pass


class BaseModel(Model):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)


db = SQLAlchemy(application, model_class=BaseModel)

from .user import User  # nopep8
