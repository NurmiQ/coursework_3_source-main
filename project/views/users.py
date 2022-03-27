from flask import request
from flask_restx import abort, Namespace, Resource

from project.dao.models.user import User
from project.exceptions import ItemNotFound
from project.schemas.user import UserSchema
from project.services.users_service import UsersService
from project.setup_db import db
from project.tools.security import auth_required

users_ns = Namespace('users')


@users_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        def get(self):
            """Get all users"""
            return UsersService(db.session).get_all_users()


@users_ns.route('/<int:user_id>')
class UserView(Resource):
    @auth_required
    def get(self, user_id: int):
        """Get user by id"""
        try:
            return UsersService(db.session).get_user_by_id(user_id)
        except ItemNotFound:
            abort(404, message="Movie not found")

    def patch(self, user_id):
        req_json = request.json
        if not req_json:
            abort(400, "bad request")
        if not req_json.get('id'):
            req_json['id'] = user_id
        try:
            return UsersService(db.session).update(req_json)
        except ItemNotFound:
            abort(404, "user not found")


@users_ns.route('password/<int:user_id>')
class UserView(Resource):
    @auth_required
    def put(self, user_id):
        req_json = request.json
        if not req_json:
            abort(400, "bad request")
        if not req_json.get('password_1') or not req_json.get('password_2'):
            abort(400, "bad request")
        if not req_json.get('id'):
            req_json['id'] = user_id
        try:
            return UsersService(db.session).update_pass(req_json)
        except ItemNotFound:
            abort(404, "user not found")
