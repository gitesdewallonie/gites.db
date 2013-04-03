# -*- coding: utf-8 -*-

import sqlalchemy as sa
from sqlalchemy.orm import relation
import geoalchemy
from geoalchemy.postgis import PGComparator

from zope.interface import implements

from gites.db.interfaces import IInfoPratique
from gites.db.mapper import GitesMappedClassBase


class InfoPratique(GitesMappedClassBase):
    implements(IInfoPratique)
    __tablename__ = u'info_pratique'

    infoprat_pk = sa.Column('infoprat_pk', sa.Integer, primary_key=True)

    infoprat_nom = sa.Column('infoprat_nom', sa.String())

    infoprat_adresse = sa.Column('infoprat_adresse', sa.String())

    infoprat_url = sa.Column('infoprat_url', sa.String())

    infoprat_gps_long = sa.Column('infoprat_gps_long', sa.Float())

    infoprat_gps_lat = sa.Column('infoprat_gps_lat', sa.Float())

    infoprat_commune_fk = sa.Column('infoprat_commune_fk', sa.Integer)

    infoprat_type_infoprat_fk = sa.Column('infoprat_type_infoprat_fk', sa.Integer,
                                          sa.ForeignKey('type_info_pratique.typinfoprat_pk'))

    infoprat_localite = sa.Column('infoprat_localite', sa.String())

    infoprat_location = geoalchemy.GeometryColumn(geoalchemy.Geometry(dimension=2,
                                                                      srid=3447),
                                                  comparator=PGComparator)

    def getName(self):
        """
        get the name of ze info pratique
        """
        return self.info_pratique.infoprat_nom

    def getUrl(self):
        """
        get the url of ze info pratique
        """
        return self.info_pratique.infoprat_url

    @classmethod
    def __declare_last__(cls):
        from gites.db.content import TypeInfoPratique

        cls.type = relation(TypeInfoPratique, lazy=True)
