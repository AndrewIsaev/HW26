from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.favourite_movie import f_movie_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns
from views.auth import auth_ns


def create_app(config_object: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app: Flask) -> None:
    """ Init database and namespaces"""
    db.init_app(app)
    with app.app_context():
        db.create_all()
    api = Api(app)
    # Add namespaces
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(f_movie_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run()
