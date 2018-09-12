# -*- coding: utf-8 -*-

import sqlalchemy as sa
import geoalchemy
from geoalchemy.postgis import PGComparator

from zope.interface import implements

from affinitic.db import mapper

from gites.db.interfaces import IInfoPratique
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.info.typeinfopratique import TypeInfoPratique


class InfoPratique(GitesMappedClassBase):
    implements(IInfoPratique)
    """
    Table permettant de gérer les informations pratiques d'un hébergement
    """

    __tablename__ = u'info_pratique'

    infoprat_pk = sa.Column('infoprat_pk', sa.Integer,
                            primary_key=True,
                            doc=u"Identifiant unique")

    infoprat_nom = sa.Column('infoprat_nom', sa.String(),
                             doc=u"Nom de l'information pratique")

    infoprat_adresse = sa.Column('infoprat_adresse', sa.String(),
                                 doc=u"Adresse de l'information pratique")

    infoprat_url = sa.Column('infoprat_url', sa.String(),
                             doc=u"URL de l'information pratique")

    infoprat_gps_long = sa.Column('infoprat_gps_long', sa.Float(),
                                  doc=u"Coordonnée longitudinale de l'information pratique")

    infoprat_gps_lat = sa.Column('infoprat_gps_lat', sa.Float(),
                                 doc=u"Coordonnée latitudinale de l'information pratique")

    infoprat_commune_fk = sa.Column('infoprat_commune_fk', sa.Integer,
                                    doc=u"Numéro d'identifiant unique vers la table commune")

    infoprat_type_infoprat_fk = sa.Column('infoprat_type_infoprat_fk', sa.Integer,
                                          sa.ForeignKey('type_info_pratique.typinfoprat_pk'),
                                          doc=u"Numéro d'identifiant unique vers la table type d'information pratique")

    infoprat_localite = sa.Column('infoprat_localite', sa.String(),
                                  doc=u"Localité de l'information pratique")

    infoprat_location = geoalchemy.GeometryColumn(geoalchemy.Geometry(dimension=2,
                                                                      srid=3447),
                                                  comparator=PGComparator,
                                                  doc=u"Géolocalisation de l'information pratique sur une carte")

    @mapper.Relation
    def type(cls):
        return sa.orm.relation(TypeInfoPratique, lazy=True)

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
