# author: Nam Nguyen Hoai
# coding: utf-8

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TestTable(Base):
    __tablename__ = 'testtable'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100))
