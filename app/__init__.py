from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect


from config import Configuration


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    app.debug = True
    return app

app = create_app()
db = SQLAlchemy(app)
celery = Celery(app.name, broker='redis://localhost:6379/0')
celery.conf.update(app.config)

from app import routes, models, forms
db.create_all()
