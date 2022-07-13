from project.config import Config
from project.container import user_service, genre_service
from project.server import create_app
from project.setup.db import db

if __name__ == '__main__':
    with create_app(Config).app_context():
        db.drop_all()
        db.create_all()
        genre_service.create(
            {
                "id": 1,
                "name": "Genre Roman"
            }
        )

        user_service.create(
            {
                "id": 1,
                "email": "test@mail.ru",
                "password": "123",
                "role": "1",
                "name": "Genre Roman",
                "surname": "1",
                "genre_id": 1
            }
        )
