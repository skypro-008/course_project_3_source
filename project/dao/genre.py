from project.dao.models.genres import Genre, GenreSchema


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Genre).get(bid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        new_data = Genre(**data)
        self.session.add(new_data)
        self.session.commit()
        return new_data