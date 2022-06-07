# -*- coding: utf-8 -*-

class BaseConfig:
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'


class DevConfig(BaseConfig):
    DEBUG = True

    # mysql
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zj122900@119.3.52.192:3306/beacon?charset=utf8'
    SQLALCHEMY_BINDS = {
        'master': 'mysql+pymysql://root:zj122900@119.3.52.192:3306/beacon?charset=utf8',
        'slave': 'mysql+pymysql://root:zj122900@119.3.52.192:3307/beacon?charset=utf8',
    }
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

    # redis sentinel
    REDIS_SENTINELS = [
        ('119.3.52.192', '26379'),
        ('119.3.52.192', '26380'),
        ('119.3.52.192', '26381'),
    ]
    REDIS_SENTINEL_SERVICE_NAME = 'local-master'

    # redis cluster
    REDIS_CLUSTER = [
        {'host': '119.3.52.192', 'port': '6379'},
        {'host': '119.3.52.192', 'port': '6380'},
        {'host': '119.3.52.192', 'port': '6381'},
    ]
