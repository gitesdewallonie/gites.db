# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class MapBlacklist(GitesMappedClassBase):
    __tablename__ = u'map_blacklist'
    __table_args__ = (sa.UniqueConstraint('blacklist_id',
                                          'blacklist_provider_pk',
                                          name='unique_id_provider'),)
    blacklist_pk = sa.Column('blacklist_pk', sa.Integer(), primary_key=True,
                             unique=True)

    blacklist_id = sa.Column('blacklist_id', sa.String(), nullable=False)

    blacklist_name = sa.Column('blacklist_name', sa.String(), nullable=False)

    blacklist_description = sa.Column('blacklist_description', sa.String(),
                                      nullable=False)

    blacklist_provider_pk = sa.Column('blacklist_provider_pk', sa.String(),
                                      sa.ForeignKey('map_provider.provider_pk'),
                                      nullable=False)
