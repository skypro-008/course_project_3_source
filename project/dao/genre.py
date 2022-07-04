from project.dao.models.genres import Genres, GenreSchema


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genres = Genres.query.all()
        result = GenreSchema(many=True).dump(genres)
        return result, 200

    def get_one(self, gid):
        genre = Genres.query.get(gid)
        result = GenreSchema().dump(genre)
        return result