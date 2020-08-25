import pathlib

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = 'test'
    FLASK_APP = 'card_game'
    FLASK_ENV = 'development'

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/toppy/Desktop/card_game_backend/test.db'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False