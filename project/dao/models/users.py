
from marshmallow import Schema, fields

from project.dao.models.base import BaseMixin
from project.setup.db import db


class User(BaseMixin, db.Model):
    __tablename__ = "users"

    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    genre = db.relationship("Genre")


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str(load=True)
    name = fields.Str()
    surname = fields.Str()
