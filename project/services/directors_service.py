from project.dao.director import DirectorDAO
from project.exceptions import ItemNotFound
from project.schemas.director import DirectorSchema
from project.services.base import BaseService


class DirectorsService(BaseService):
    def get_item_by_id(self, pk):
        director = DirectorDAO(self._db_session).get_by_id(pk)
        if not director:
            raise ItemNotFound
        return DirectorSchema().dump(director)

    def get_all_directors(self):
        directors = DirectorDAO(self._db_session).get_all()
        return DirectorSchema(many=True).dump(directors)




















# from dao.director import DirectorDAO
#
#
# class DirectorService:
#     def __init__(self, dao: DirectorDAO):
#         self.dao = dao
#
#     def get_one(self, bid):
#         return self.dao.get_one(bid)
#
#     def get_all(self):
#         return self.dao.get_all()
#
#     def create(self, director_d):
#         return self.dao.create(director_d)
#
#     def update(self, director_d):
#         self.dao.update(director_d)
#         return self.dao
#
#     def delete(self, rid):
#         self.dao.delete(rid)