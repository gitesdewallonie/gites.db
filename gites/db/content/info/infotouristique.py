# -*- coding: utf-8 -*-
import sqlalchemy as sa
import geoalchemy
from geoalchemy.postgis import PGComparator

from zope.interface import implements

from affinitic.db import mapper

from gites.db.interfaces import IInfoTouristique
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.commune import Commune
from gites.db.content.info.typeinfotouristique import TypeInfoTouristique


class InfoTouristique(GitesMappedClassBase):
    implements(IInfoTouristique)
    __tablename__ = u'info_touristique'

    infotour_pk = sa.Column('infotour_pk', sa.Integer, primary_key=True)

    infotour_nom = sa.Column('infotour_nom', sa.String())

    infotour_adresse = sa.Column('infotour_adresse', sa.String())

    infotour_url = sa.Column('infotour_url', sa.String())

    infotour_gps_long = sa.Column('infotour_gps_long', sa.Float())

    infotour_gps_lat = sa.Column('infotour_gps_lat', sa.Float())

    infotour_localite = sa.Column('infotour_localite', sa.String())

    infotour_commune_fk = sa.Column('infotour_commune_fk', sa.Integer,
                                    sa.ForeignKey('commune.com_pk'))

    infotour_type_infotour_fk = sa.Column('infotour_type_infotour_fk', sa.Integer,
                                          sa.ForeignKey('type_info_touristique.typinfotour_pk'))

    infotour_location = geoalchemy.GeometryColumn(geoalchemy.Geometry(dimension=2,
                                                                      srid=3447),
                                                  comparator=PGComparator)

    @mapper.Relation
    def type(cls):
        return sa.orm.relation(TypeInfoTouristique, lazy=True)

    @mapper.Relation
    def commune(cls):
        return sa.orm.relation(Commune, lazy=True)

    def getInfoTourisqueName(self):
        """
        get the name of ze info touristique
        """
        return self.info_touristique.infotour_nom

    def getInfoTouristiqueUrl(self):
        """
        get the url of ze info touristique
        """
        return self.info_touristique.infotour_url
