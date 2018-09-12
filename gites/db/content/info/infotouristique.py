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
    """
    Table permettant de gérer les informations touristiques d'un hébergement
    """

    __tablename__ = u'info_touristique'

    infotour_pk = sa.Column('infotour_pk', sa.Integer,
                            primary_key=True,
                            )

    infotour_nom = sa.Column('infotour_nom', sa.String(),
                             doc=u"Nom de l'information touristique")

    infotour_adresse = sa.Column('infotour_adresse', sa.String(),
                                 doc=u"Adresse de l'information touristique")

    infotour_url = sa.Column('infotour_url', sa.String(),
                             doc=u"URL de l'information touristique")

    infotour_gps_long = sa.Column('infotour_gps_long', sa.Float(),
                                  doc=u"Coordonnée longitudinale de l'information touristique")

    infotour_gps_lat = sa.Column('infotour_gps_lat', sa.Float(),
                                 doc=u"Coordonnée latitudinale de l'information touristique")

    infotour_localite = sa.Column('infotour_localite', sa.String(),
                                  doc=u"Localité de l'information touristique")

    infotour_commune_fk = sa.Column('infotour_commune_fk', sa.Integer,
                                    sa.ForeignKey('commune.com_pk'),
                                    doc=u"Numéro d'identifiant unique vers la table commune")

    infotour_type_infotour_fk = sa.Column('infotour_type_infotour_fk', sa.Integer,
                                          sa.ForeignKey('type_info_touristique.typinfotour_pk'),
                                          doc=u"Numéro d'identifiant unique vers la table type d'information touristique")

    infotour_location = geoalchemy.GeometryColumn(geoalchemy.Geometry(dimension=2,
                                                                      srid=3447),
                                                  comparator=PGComparator,
                                                  doc=u"Géolocalisation de l'information touristique sur une carte")

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
