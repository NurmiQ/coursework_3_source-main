from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.services.movies_service import MoviesService
from project.setup_db import db

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        def get(self):
            """Get all movies"""
            return MoviesService(db.session).get_all_movies()



@movies_ns.route('/<int:bid>')
class MovieView(Resource):
    def get(self, movie_id: int):
        """Get movie by id"""
        try:
            return MoviesService(db.session).get_item_by_id(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")





