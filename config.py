import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP="app.py"
    FLASK_ENV='development'
    SECRET_KEY='very_secret_key'
    NSQD_SERVER = os.getenv('NSQD_SERVER')
    DEBUG = True
