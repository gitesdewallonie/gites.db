# -*- coding: utf-8 -*-
import sqlalchemy as sa
import geoalchemy
from geoalchemy.postgis import PGComparator

from affinitic.db import mapper

from gites.db.mapper import GitesMappedClassBase
from gites.db.content.map.mapprovider import MapProvider

MapProvider  # Pyflakes fix


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

    ext_data_location = geoalchemy.GeometryColumn(geoalchemy.Geometry(dimension=2,
                                                                      srid=3447),
                                                  comparator=PGComparator)

    @mapper.RelationImport('gites.db.content:MapBlacklist')
    @mapper.Relation
    def blacklist(cls, MapBlacklist):
        return sa.orm.relation(
            MapBlacklist,
            lazy=True,
            primaryjoin=sa.and_(
                cls.ext_data_id == MapBlacklist.blacklist_id,
                cls.ext_data_provider_pk == MapBlacklist.blacklist_provider_pk),
            backref='mapExternalData')

    @mapper.RelationImport('gites.db.content:MapProvider')
    @mapper.Relation
    def provider(cls, MapProvider):
        return sa.orm.relation(
            MapProvider, lazy=True)
