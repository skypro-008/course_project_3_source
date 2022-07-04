from flask_restx import Resource, Namespace

from project.container import genre_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres, 200


@genres_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid):
        genres = genre_service.get_one(gid)
        return genres, 200