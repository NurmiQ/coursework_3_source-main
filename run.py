from project.config import DevelopmentConfig
from project.dao.models import Genre
from project.server import create_app, db

from flask import Flask
from flask_restx import Api

from config import Config
from project.dao.models.user import User
from project.setup_db import db
from project.views.auth import auth_ns
from project.views.directors import directors_ns
from project.views.genres import genres_ns
from project.views.movies import movies_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(auth_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)

