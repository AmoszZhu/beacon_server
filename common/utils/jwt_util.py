# -*- coding: utf-8 -*-
import jwt
from flask import current_app
from datetime import datetime, timedelta


def generate_jwt(payload: dict, expiry: datetime, secret=None) -> str:
    """
    生成jwt
    :param payload: dict, 载荷
    :param expiry: datetime 有效期
    :param secret: 密钥
    :return: jwt
    """

    # 将过期时间加入payload
    _payload = {"exp": expiry}
    _payload.update(payload)

    if not secret:
        secret = current_app.config['JWT_SECRET']

    token = jwt.encode(_payload, secret, algorithm='HS256')
    return token


def verify_jwt(token: str, secret=None) -> dict:
    """
    检验token
    :param token: jwt
    :param secret: 密钥
    :return: payload
    """

    if not secret:
        secret = current_app.config["JWT_SECRET"]

    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
    except jwt.PyJWTError as e:
        current_app.logger.error(e)
        payload = None

    return payload


def generate_token(user_id: int, refresh=True) -> tuple:
    """
    生成token和refresh_token
    :param user_id: 用户id
    :param refresh:
    :return:
    """
    secret = current_app.config["JWT_SECRET"]

    expiry = datetime.utcnow() + timedelta(hours=current_app.config["JWT_EXPIRY_HOURS"])

    token = generate_jwt({"user_id": user_id}, expiry, secret)

    if refresh:
        expiry = datetime.utcnow() + timedelta(days=current_app.config["JWT_REFRESH_DAYS"])
        refresh_token = generate_jwt({"user_id": user_id, "is_refresh": True}, expiry, secret)
    else:
        refresh_token = None

    return token, refresh_token
