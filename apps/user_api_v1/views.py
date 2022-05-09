# -*- coding: utf-8 -*-

from flask import request, current_app
from sqlalchemy import or_

from . import user_api_v1 as user_bp
from common.models.user import User
from common.models import db


@user_bp.route('/register', methods=["POST"])
def register_user():
    """
    创建用户
    {
        "mobile": not null,
        "password"
        "name"
        "email"
        "status"
    }
    :return:
    """

    error_msg = {
        "data": None,
        "response": "failed",
        "msg": ""
    }

    # 获取用户注册基本信息
    try:
        request_body = request.json
    except Exception as e:
        current_app.logger.error(e)
        error_msg["msg"] = "Lack of body"
        return error_msg, 400

    user_name = request_body.get("user_name", None)
    password = request_body.get("password", None)
    password_2 = request_body.get("password_2", None)
    email = request_body.get("email", None)
    mobile = request_body.get("mobile", None)

    # 验证注册信息
    if not all([user_name, password, password_2, mobile]):
        error_msg["msg"] = "Lack of parameter"
        return error_msg, 400

    if password != password_2:
        error_msg["msg"] = "password != password_2"
        return error_msg, 400

    # 检查该用户是否已注册
    try:
        user_list = User.query.filter(or_(User.mobile == mobile, User.name == user_name)).all()
    except Exception as e:
        current_app.logger.error(e)
        error_msg["msg"] = "Database exception"
        return error_msg, 400

    # 如果用户存在
    if user_list:
        error_msg["msg"] = "user has been registered"
        return error_msg, 400

    # 用户信息存入数据库
    user = User(name=user_name, mobile=mobile, email=email, password=password)
    current_app.logger.info(f"Create user info : {user}")

    try:
        db.session.add(user)
        db.session.commit()
        return {
            "data": {
                "uid": user.id
            },
            "response": "successful",
            "msg": "0"
        }, 201
    except Exception as e:
        current_app.logger.error(e)
        error_msg["msg"] = "Database exception"
        return error_msg, 400
