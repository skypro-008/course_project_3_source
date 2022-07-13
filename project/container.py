from project.dao import GenreDAO
from project.dao.user import UserDAO

from project.services.genres_service import GenreService
from project.services.users_service import UserService
from project.setup.db import db

# DAO
genre_dao = GenreDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenreService(dao=genre_dao)
user_service = UserService(dao=user_dao)
