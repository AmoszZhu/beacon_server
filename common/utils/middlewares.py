# -*- coding: utf-8 -*-

from flask import g, request, current_app
from common.utils.jwt_util import verify_jwt


def jwt_authentication():
    """
    获取请求头中的token
    :return:
    """
    # 对于进入的请求先设定g中的user_id,is_refresh 来判定是否登录过
    g.user_id = None
    g.is_refresh = False

    token = request.headers.get("Authorization")
    current_app.logger.info(f"token is {token}")

    if token is not None and token.startswith("Bearer "):
        token = token[7:]

        # 验证token
        payload = verify_jwt(token)
        current_app.logger.info(f"payload is {payload}")
        if payload is not None:
            g.user_id = payload.get("user_id")
            g.is_refresh = payload.get("is_refresh", False)
