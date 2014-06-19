# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class PivotOrigin(GitesMappedClassBase):
    __tablename__ = u'notification_origin'

    pk = sa.Column('origin_pk', sa.String, primary_key=True, unique=True)
