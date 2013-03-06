# -*- coding: utf-8 -*-
from Acquisition import ImplicitAcquisitionWrapper
from affinitic.db.mapper import MappedClassBase
from gites.db import DeclarativeBase, session


class GitesMappedClassBase(DeclarativeBase, MappedClassBase):
    __abstract__ = True

    def __of__(self, wrapper):
        return ImplicitAcquisitionWrapper(self, wrapper)

    @classmethod
    def _session(self):
        return session()
