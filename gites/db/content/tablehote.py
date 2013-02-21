# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class TableHote(GitesMappedClassBase):
    __tablename__ = u'table_hote'

    tabho_pk = sa.Column('tabho_pk', sa.Integer,
                         primary_key=True)

    tabho_type_fr = sa.Column('tabho_type_fr', sa.String())
