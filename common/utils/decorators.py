# -*- coding: utf-8 -*-

from functools import wraps
from flask import g, current_app


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if g.user_id is not None and g.is_refresh is False:
            return func(*args, **kwargs)
        else:
            current_app.logger.warn("Invalid token")
            return {
                       "msg": "Invalid token"
                   }, 401

    return wrapper
