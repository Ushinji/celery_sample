import os
from app.config import BaseConfig


database_name = 'celery_sample_test'
database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
database_host = os.getenv('DATABASE_HOST')


class Config(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f'mysql://{database_user}:{database_password}@{database_host}:3306/{database_name}?charset=utf8mb4'
