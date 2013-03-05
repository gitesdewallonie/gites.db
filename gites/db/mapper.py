# -*- coding: utf-8 -*-
from Acquisition import ImplicitAcquisitionWrapper
from z3c.sqlalchemy.mapper import MappedClassBase
from gites.db import DeclarativeBase


class GitesMappedClassBase(DeclarativeBase, MappedClassBase):
    __abstract__ = True

    def __of__(self, wrapper):
        return ImplicitAcquisitionWrapper(self, wrapper)
