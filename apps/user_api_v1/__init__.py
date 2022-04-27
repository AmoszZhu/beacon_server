# -*- coding: utf-8 -*-

from flask import Blueprint

user_api_v1 = Blueprint("user_api", __name__, url_prefix="/user_api_v1")

from . import views