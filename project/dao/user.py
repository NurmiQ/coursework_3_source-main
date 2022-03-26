from flask import request
from sqlalchemy.orm.scoping import scoped_session

from project.dao.models.user import User


class UserDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk):
        return self._db_session.query(User).filter(User.id == pk).one_or_none()

    def get_all(self):
        return self._db_session.query(User).all()

    def get_by_email(self, email):
        return self._db_session.query(User).filter(User.email == email).one_or_none()

    def create(self):
        req_json = request.json
        new_user = User(**req_json)
        self._db_session.add(new_user)
        self._db_session.commit()
        return new_user


    def update(self, data):
        new_pass = self.get_by_id(data.get('id'))
        if new_pass:
            if data.get('password'):
                new_pass.password = data.get('password')
            if data.get('name'):
                new_pass.name = data.get('name')
            if data.get('surname'):
                new_pass.surname = data.get('surname')
            self._db_session.add(new_pass)
            self._db_session.commit()
        return "", 204