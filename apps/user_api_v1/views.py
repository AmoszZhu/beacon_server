# -*- coding: utf-8 -*-

from flask import request, current_app, g
from sqlalchemy import or_

from . import user_api_v1 as user_bp
from common.models.user import User
from common.models import db
from common.utils.jwt_util import generate_token
from common.utils.decorators import login_required


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


@user_bp.route('/login', methods=["POST", "PUT"])
def login():
    """
    登录和刷新token
    :return:
    """
    error_msg = {
        "data": None,
        "response": "failed",
        "msg": ""
    }

    if request.method == "POST":
        # 获取用户登录信息
        try:
            request_body = request.json
        except Exception as e:
            current_app.logger.error(e)
            error_msg["msg"] = "Lack of body"
            return error_msg, 400

        # 检验用户信息
        user_name = request_body.get("user_name", None)
        password = request_body.get("password", None)

        if not all([user_name, password]):
            error_msg["msg"] = "Lack of parameter"
            return error_msg, 400

        # 检查用户是否存在
        try:
            user_list = User.query.filter(User.name == user_name).all()
        except Exception as e:
            current_app.logger.error(e)
            error_msg["msg"] = "Database except"
            return error_msg, 400

        # 如果用户不存在
        if not user_list:
            error_msg["msg"] = "User is not exist"
            return error_msg, 400

        user = user_list[0]
        # 验证密码
        if password != user.password:
            error_msg["msg"] = "Password is wrong, please try again"
            return error_msg, 400

        token, refresh_token = generate_token(user.id)

        return {
            "data": {
                "token": token,
                "refresh_token": refresh_token
            },
            "response": "success",
            "msg": 0
        }


@user_bp.route('/test')
@login_required
def test():
    print(g.user_id)

    return "Demo"
