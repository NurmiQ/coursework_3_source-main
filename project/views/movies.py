from flask import request
from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.services.movies_service import MoviesService
from project.setup_db import db
from project.tools.security import auth_required

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        """Get all movies"""
        req_json = request.json
        if req_json:
            return MoviesService(db.session).get_filter_movies(req_json)
        else:
            return MoviesService(db.session).get_all_movies()


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    @auth_required
    def get(self, movie_id: int):
        """Get movie by id"""
        try:
            return MoviesService(db.session).get_item_by_id(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")
