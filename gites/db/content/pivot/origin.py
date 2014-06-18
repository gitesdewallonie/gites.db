# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class PivotOrigin(GitesMappedClassBase):
    __tablename__ = u'pivot_origin'

    origin_pk = sa.Column('origin_pk',
                          sa.String(),
                          primary_key=True,
                          unique=True)
