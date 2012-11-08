# -*- coding: utf-8 -*-
from z3c.sqlalchemy.mapper import MappedClassBase
from affinitic.caching import cache
from gites.db import session


class Proprio(MappedClassBase):
    c = None

    @classmethod
    @cache(lambda x, y, z: z, dependencies=['pgsql'])
    def get(cls, heb_pk):
        sess = session()
        return sess.query(cls).get(heb_pk)
