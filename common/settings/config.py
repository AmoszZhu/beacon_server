# -*- coding: utf-8 -*-

class BaseConfig:
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'


class DevConfig(BaseConfig):
    DEBUG = True

    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zj122900@119.3.52.192:3306/beacon?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True