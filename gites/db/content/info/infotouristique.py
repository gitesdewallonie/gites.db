# -*- coding: utf-8 -*-
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.orm import relation

from zope.interface import implements

from gites.db.interfaces import IInfoTouristique
from gites.db.mapper import GitesMappedClassBase


class InfoTouristique(GitesMappedClassBase):
    implements(IInfoTouristique)
    __tablename__ = u'info_touristique'

    infotour_pk = sa.Column('infotour_pk', sa.Integer, primary_key=True)

    infotour_nom = sa.Column('infotour_nom', sa.String())

    infotour_adresse = sa.Column('infotour_adresse', sa.String())

    infotour_url = sa.Column('infotour_url', sa.String())

    infotour_gps_long = sa.Column('infotour_gps_long', DOUBLE_PRECISION())

    infotour_gps_lat = sa.Column('infotour_gps_lat', DOUBLE_PRECISION())

    infotour_localite = sa.Column('infotour_localite', sa.String())

    infotour_commune_fk = sa.Column('infotour_commune_fk', sa.Integer,
                                    sa.ForeignKey('commune.com_pk'))

    infotour_type_infotour_fk = sa.Column('infotour_type_infotour_fk', sa.Integer,
                                          sa.ForeignKey('type_info_touristique.typinfotour_pk'))

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

    @classmethod
    def __declare_last__(cls):
        from gites.db.content import TypeInfoTouristique
        from gites.db.content import Commune

        cls.type = relation(TypeInfoTouristique, lazy=True)
        cls.commune = relation(Commune, lazy=True)
