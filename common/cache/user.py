# -*- coding: utf-8 -*-

from flask import current_app
from sqlalchemy.orm import load_only
from sqlalchemy.exc import DatabaseError
from redis.exceptions import RedisError
import json

from common.models.user import User
from . import constants


class UserCache:
    """
    用户基本信息的缓存工具类
    """

    def __init__(self, user_id):
        # 记录到redis中的key, 使用的是redis的string类型
        self.redis_key = f"user:{user_id}:profile"
        self.user_id = user_id

    def save(self):
        """
        保存缓存记录
        """

        # 从current_app中获取redis连接
        r = current_app.redis_cluster

        try:
            user = User.query.options(load_only(
                User.name,
                User.mobile,
                User.status,
                User.email
            )).filter(User.id == self.user_id).first()
        except DatabaseError as e:
            current_app.logger.error(e)
            # 对于数据库异常，抛给调用者，由调用者决定
            raise e

        # 如果用户不存在
        if user is None:
            try:
                # 防止缓存击穿，给不存在的用户缓存为-1
                r.setex(self.redis_key, constants.UserNotExistsCacheTTL.get_val(), -1)
            except RedisError as e:
                current_app.logger.error(e)

            return None
        else:
            # 初始化返回数据格式
            user_dict = {
                'mobile': user.mobile,
                'name': user.name,
                'status': user.status,
                'email': user.email
            }
            try:
                r.setex(self.redis_key, constants.UserProfileCacheTTL.get_val(), json.dumps(user_dict))
            except RedisError as e:
                current_app.logger.error(e)

            return user_dict

    def get(self):
        """
        获取缓存数据
        """

        # 先到redis查询缓存记录
        r = current_app.redis_cluster

        try:
            ret = r.get(self.redis_key)
        except RedisError as e:
            current_app.logger.error(e)
            ret = None

        if ret is not None:
            # 如果redis中有缓存记录，判断是否是-1
            if ret == b"-1":
                return None
            else:
                user_dict = json.loads(ret)
                return user_dict
        else:
            return self.save()

    def clear(self):
        """
        清除缓存
        """
        try:
            r = current_app.redis_cluster
            r.delete(self.redis_key)
        except RedisError as e:
            current_app.logger.error(e)

    def is_user_exists(self):
        """
        通过缓存判断用户是否存在
        """
        r = current_app.redis_cluster

        # 查询redis中是否有缓存记录
        try:
            ret = r.get(self.redis_key)
        except RedisError as e:
            current_app.logger.error(e)
            ret = None

        # 如果redis中存在缓存记录，就判断值是否为-1
        if ret is not None:
            if ret == b"-1":
                return False
            else:
                return True
        else:
            ret = self.save()
            if ret is not None:
                return True
            else:
                return False
