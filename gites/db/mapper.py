# -*- coding: utf-8 -*-
from z3c.sqlalchemy.mapper import MappedClassBase
from gites.db import DeclarativeBase


class GitesMappedClassBase(DeclarativeBase, MappedClassBase):
    __abstract__ = True
