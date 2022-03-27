from project.dao.user import UserDAO
from project.exceptions import ItemNotFound
from project.schemas.user import UserSchema
from project.services.base import BaseService
from project.tools.security import generate_password_digest


class UsersService(BaseService):
    def get_user_by_id(self, pk):
        user = UserDAO(self._db_session).get_by_id(pk)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def get_all_users(self):
        users = UserDAO(self._db_session).get_all()
        return UserSchema(many=True).dump(users)

    def get_user_by_email(self, email):
        user = UserDAO(self._db_session).get_by_email(email)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def create(self, data):
        user_pass = data.get("password")
        if user_pass:
            data["password"] = generate_password_digest(data)
        user = UserDAO(self._db_session).create(data)
        return UserSchema().dump(user)

    def update(self, data):
        user = UserDAO(self._db_session).update(data)
        return UserSchema().dump(user)

    def update_pass(self, data):
        pass_1 = data.get("password_1")
        pass_2 = data.get("password_2")
        if pass_1 and pass_2:
            new_pass = UserDAO(self._db_session).update(data)
            return UserSchema().dump(new_pass)






