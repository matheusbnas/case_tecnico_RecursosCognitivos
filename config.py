import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'mysql+mysqlconnector://usuario:senha@localhost/escola_manager'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
