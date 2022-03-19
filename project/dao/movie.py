from sqlalchemy import desc
from sqlalchemy.orm.scoping import scoped_session

from project.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk):
        return self._db_session.query(Movie).filter(Movie.id == pk).one_or_none()

    def get_all(self):
        return self._db_session.query(Movie).all()

    def get_filter(self, limit, offset, status):
        if limit > 0 and status == "new":
            return self._db_session.query(Movie).order_by(desc(Movie.year)).limit(limit).offset(offset).all()
        elif limit > 0:
            return self._db_session.query(Movie).limit(limit).offset(offset).all()
        elif status == "new":
            return self._db_session.query(Movie).order_by(desc(Movie.year)).all()











    # def get_by_director_id(self, val):
    #     return self.session.query(Movie).filter(Movie.director_id == val).all()
    #
    # def get_by_genre_id(self, val):
    #     return self.session.query(Movie).filter(Movie.genre_id == val).all()
    #
    # def get_by_year(self, val):
    #     return self.session.query(Movie).filter(Movie.year == val).all()
    #
    # def create(self, movie_d):
    #     ent = Movie(**movie_d)
    #     self.session.add(ent)
    #     self.session.commit()
    #     return ent
    #
    # def delete(self, rid):
    #     movie = self.get_one(rid)
    #     self.session.delete(movie)
    #     self.session.commit()
    #
    # def update(self, movie_d):
    #     movie = self.get_one(movie_d.get("id"))
    #     movie.title = movie_d.get("title")
    #     movie.description = movie_d.get("description")
    #     movie.trailer = movie_d.get("trailer")
    #     movie.year = movie_d.get("year")
    #     movie.rating = movie_d.get("rating")
    #     movie.genre_id = movie_d.get("genre_id")
    #     movie.director_id = movie_d.get("director_id")
    #
    #     self.session.add(movie)
    #     self.session.commit()
