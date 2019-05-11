from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import Column, Integer
from app import application


class RecordNotFoundError(Exception):
    pass


class BaseModel(Model):
    id = Column(Integer, primary_key=True)


db = SQLAlchemy(application, model_class=BaseModel)
