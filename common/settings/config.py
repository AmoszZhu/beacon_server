# -*- coding: utf-8 -*-

class BaseConfig:
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'


class DevConfig(BaseConfig):
    DEBUG = True

    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zj122900@119.3.52.192:3306/beacon?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

    # 日志
    LOGGING_LEVEL = 'INFO'
    LOGGING_FILE_DIR = '/tmp/logs'
    LOGGING_FILE_MAX_BYTES = 30 * 1024 * 1024
    LOGGING_FILE_BACKUP = 2

    # JWT
    JWT_SECRET = 'TPmi4aLWRbyVq8zu9v82dWYW17/z+UvRnYTt4P6fAXAasd2'
    JWT_EXPIRY_HOURS = 2
    JWT_REFRESH_DAYS = 14
