# -*- coding: utf-8 -*-
import random

from flask_sqlalchemy import SQLAlchemy, SignallingSession, get_state
from sqlalchemy import orm
from sqlalchemy.sql.dml import UpdateBase


class RoutingSession(SignallingSession):
    """
    自定义Session类
    """
    def __init__(self, db, autocommit=False, autoflush=True, **options):

        SignallingSession.__init__(self, db, autocommit=autocommit, autoflush=autoflush, **options)

    def get_bind(self, mapper=None, clause=None):
        state = get_state(self.app)

        if mapper is not None:
            try:
                persist_selectable = mapper.persist_selectable
            except AttributeError:
                persist_selectable = mapper.mapped_table

            info = getattr(persist_selectable, 'info', {})
            bind_key = info.get('bind_key')

            if bind_key is not None:
                return state.db.get_engine(self.app, bind=bind_key)

        if self._flushing or isinstance(clause, UpdateBase):
            print("写操作")
            return state.db.get_engine(self.app, bind='master')
        else:
            print("读操作")
            return state.db.get_engine(self.app, bind='slave')


class RoutingSQLAlchemy(SQLAlchemy):
    """
    自定义数据库路由的sqlalchemy
    """
    def create_session(self, options):
        return orm.sessionmaker(class_=RoutingSession, db=self, **options)

