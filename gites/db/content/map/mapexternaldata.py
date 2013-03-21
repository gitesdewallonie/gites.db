# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class MapExternalData(GitesMappedClassBase):
    __tablename__ = u'map_external_data'
    __table_args__ = (sa.UniqueConstraint('ext_data_id',
                                          'ext_data_provider_pk',
                                          name='ext_data_unique_id_provider'),)
    ext_data_pk = sa.Column('ext_data_pk', sa.Integer(), primary_key=True,
                             unique=True)

    ext_data_id = sa.Column('ext_data_id', sa.String(), nullable=False)

    ext_data_title = sa.Column('ext_data_title', sa.String(), nullable=False)

    ext_data_type = sa.Column('ext_data_type', sa.String())

    ext_data_date_begin = sa.Column('ext_data_date_begin', sa.DateTime())

    ext_data_date_end = sa.Column('ext_data_date_end', sa.DateTime())

    ext_data_picture_url = sa.Column('ext_data_picture_url', sa.String())

    ext_data_latitude = sa.Column('ext_data_latitude', sa.Float(),
                                   nullable=False)

    ext_data_longitude = sa.Column('ext_data_longitude', sa.Float(),
                                   nullable=False)

    ext_data_url = sa.Column('ext_data_url', sa.String(),
                             nullable=False)

    ext_data_provider_pk = sa.Column('ext_data_provider_pk', sa.String(),
                                         sa.ForeignKey('map_provider.provider_pk'),
                                         nullable=False)
