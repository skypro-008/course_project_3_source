from project.dao.genre import GenreDAO, GenreSchema


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, item_data):
        item_in_schema = GenreSchema().load(item_data)
        self.dao.create(item_in_schema)
