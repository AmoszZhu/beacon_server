# -*- coding: utf-8 -*-

from . import db

class User(db.Model):
    """
    用户的基本信息
    """
    __tablename__ = "user_basic"

    class STATUS:
        ACTIVE = 1
        INACTIVE = 0

    id = db.Column("user_id", db.Integer, primary_key=True, doc='用户ID')
    mobile = db.Column(db.String(11), doc='手机号')
    password = db.Column(db.String(80), doc='密码')
    name = db.Column("user_name", db.String(50), doc='用户名')
    last_login = db.Column(db.DateTime, doc='最后的登录时间')
    email = db.Column(db.String(50), doc='邮箱')
    status = db.Column(db.Integer, default=1, doc='状态')

    def __repr__(self):
        return '<User : %s>' % self.name

