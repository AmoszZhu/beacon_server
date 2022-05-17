# -*- coding: utf-8 -*-

from flask import Flask
from werkzeug.utils import import_string
import os

from common.utils.middlewares import jwt_authentication


def create_flask_app(config, enable_config_file=False):
    """
    创建flask应用
    :param config: 配置信息对象
    :param enable_config_file: 是否允许运行环境中的配置文件覆盖已加载的配置信息
    :return: flask app
    """

    # init app
    app = Flask(__name__)

    # 配置config
    app.config.from_object(config)

    # if enable config file
    if enable_config_file:
        from common.utils import constants
        app.config.from_envvar(constants.GLOBAL_SETTING_ENV_NAME, silent=True)

    return app


def create_app(config, enable_config_file=False):
    """
    创建应用
    :param config: 配置信息对象
    :param enable_config_file: 是否允许运行环境中的配置文件覆盖已加载的配置信息
    :return:
    """
    app = create_flask_app(config, enable_config_file)

    # register blueprint
    register_blueprint(app)

    # 日志
    from common.utils.logging import create_logger
    create_logger(app)

    # DB
    from common.models import db
    db.init_app(app)

    # 添加请求钩子
    app.before_request(jwt_authentication)

    return app


def register_blueprint(app):
    apps_absolute_path = os.path.dirname(__file__)
    base_file = apps_absolute_path.split("/")[-1]
    file_list = os.listdir(apps_absolute_path)
    for file_name in file_list:
        file_path = os.path.join(apps_absolute_path, file_name)
        if not os.path.isdir(file_path):
            continue
        if not os.path.exists(os.path.join(apps_absolute_path, "__init__.py")):
            continue
        if file_name == "__pycache__":
            continue
        blueprint_name = base_file + '.' + file_name + ":" + file_name
        print(f"bp name is {blueprint_name}")
        auto_blueprint = import_string(blueprint_name)
        app.register_blueprint(auto_blueprint)




