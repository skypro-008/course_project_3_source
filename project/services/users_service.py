from project.dao.models.users import UserSchema
from project.dao.user import UserDAO
from project.exceptions import ItemNotFound
from project.tools.security import generate_password_digest


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, item_id):
        item_db = self.dao.get_one(item_id)
        item_serialized = UserSchema().dump(item_db)
        return item_serialized

    def get_one_by_email(self, item_data):
        item_db = self.dao.get_one_by_email(item_data)
        item_serialized = UserSchema().dump(item_db)
        return item_serialized

    def get_all(self):
        items_db = self.dao.get_all()
        items_serialized = UserSchema(many=True).dump(items_db)
        return items_serialized

    def create(self, item_data):
        item_in_schema = UserSchema().load(item_data)
        item_db = self.dao.create(data=item_in_schema)

    def update(self, new_data):
        self.dao.update(new_data)
        return self.dao

    def update_by_email(self, new_data):
        self.dao.update_by_email(new_data)
        return self.dao