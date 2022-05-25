# -*- coding: utf-8 -*-
import random


class BaseCacheTTL:
    """
    缓存有效期，在设置缓存有效期时采用设置不同的有效期方案
    通过增加随机值来实现
    """
    TTL = 0
    MAX_DELTA = 10 * 60

    @classmethod
    def get_val(cls):
        return cls.TTL + random.randrange(0, cls.MAX_DELTA)


class UserProfileCacheTTL(BaseCacheTTL):
    TTL = 30 * 60


class UserNotExistsCacheTTL(BaseCacheTTL):
    """
    用户不存在时，为解决缓存击穿，有效期不适合过长
    """
    TTL = 5 * 60
    MAX_DELTA = 60
