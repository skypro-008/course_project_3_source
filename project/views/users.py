from flask import request
from flask_restx import Resource, Namespace, abort

from project.container import user_service
from project.dao.models.users import UserSchema
from project.services.users_service import UserService
from project.setup.db import db
from project.tools.security import auth_required

users_ns = Namespace('genres')


@users_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        new_data = request.json
        return user_service.get_by_email(new_data), 200

    @auth_required
    def patch(self):
        new_data = request.json
        user = user_service.get_by_email(new_data)

        user_role = new_data.get("role")
        if user_role != "user":
            abort(400)

        user_service.update(new_data)
        return user, 204

    @users_ns.route('/password')
    class UsersView(Resource):
        @auth_required
        def put(self):
            pass

