import os

class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:010101@localhost:5432/parser'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'yoursecretkey12345')
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    ELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    NSQD_SERVER=os.getenv('NSQD_SERVER')
