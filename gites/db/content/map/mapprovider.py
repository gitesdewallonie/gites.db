# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class MapProvider(GitesMappedClassBase):
    __tablename__ = u'map_provider'

    provider_pk = sa.Column('provider_pk', sa.String(), primary_key=True,
                            unique=True)
