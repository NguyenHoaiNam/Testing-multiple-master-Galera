# Author: Nam Nguyen Hoai
# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
import models

_SESSION_FACTORY = None
_ENGINE_FACTORY = None


def setup_database_engine():
    global _SESSION_FACTORY, _ENGINE_FACTORY
    engine = create_engine(config.DATABASE_URI, echo=True)
    _ENGINE_FACTORY = engine
    _SESSION_FACTORY = sessionmaker(bind=engine)()


def get_engine():
    if not _ENGINE_FACTORY:
        setup_database_engine()
    return _ENGINE_FACTORY


def get_session():
    if not _SESSION_FACTORY:
        setup_database_engine()
    return _SESSION_FACTORY


def get_session_2():
    engine = create_engine(config.DATABASE_URI_2, echo=True)
    return sessionmaker(bind=engine)()


def get_records(session, name=''):
    # name = '{}_'.format(name)+'%'
    return session.query(models.TestTable).all()
        # filter(
        # models.TestTable.name.like('name_%')).from_self()


def delete_records(session, name=''):
    session.query(models.TestTable).delete(synchronize_session=False)
