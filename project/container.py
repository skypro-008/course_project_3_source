from project.dao import GenresDAO

from project.services import GenreService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)

# Services
genre_service = GenreService(genres_dao=genre_dao)
