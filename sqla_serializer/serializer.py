# -*- coding: utf-8 -*-
from marshmallow_sqlalchemy import ModelSchema

from sqla_model.users import User
from example.main import session


class UserSchema(ModelSchema):

    class Meta:
        model = User
        sqla_session = session

