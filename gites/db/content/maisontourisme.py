# -*- coding: utf-8 -*-
import sqlalchemy as sa
import geoalchemy
from zope.interface import implements
from geoalchemy.postgis import PGComparator
from affinitic.db import mapper
from gites.db.interfaces import IMaisonTourisme
from gites.db.mapper import GitesMappedClassBase


class MaisonTourisme(GitesMappedClassBase):
    implements(IMaisonTourisme)
    """
    Table permettant de gérer les informations des Maisons du Tourisme
    """

    __tablename__ = u'maison_tourisme'

    mais_pk = sa.Column('mais_pk', sa.Integer,
                        primary_key=True,
                        doc=u"Numéro d'identifiant unique")

    mais_nom = sa.Column('mais_nom', sa.String(),
                         doc=u"Nom de la Maison du Tourisme")

    mais_url = sa.Column('mais_url', sa.String(),
                         doc=u"URL de la Maison du Tourisme")

    mais_gps_lat = sa.Column('mais_gps_lat', sa.Float(),
                             doc=u"Coordonnée latitudinale de la Maison du Tourisme")

    mais_gps_long = sa.Column('mais_gps_long', sa.Float(),
                              doc=u"Coordonnée longitudinale de la Maison du Tourisme")

    mais_location = geoalchemy.GeometryColumn(geoalchemy.Geometry(dimension=2,
                                                                  srid=3447),
                                              comparator=PGComparator,
                                              doc=u"Géolocalisation de la Maison du Tourisme sur une carte")

    def getCommunesName(self):
        return [commune.com_nom for commune in self.commune]

    com_nom = property(getCommunesName)

    @mapper.RelationImport('gites.db.content:Commune')
    @mapper.Relation
    def commune(cls, Commune):
        return sa.orm.relation(Commune, lazy=True)

    @mapper.RelationImport('gites.db.content:InfoTouristique',
                           'gites.db.content:Commune')
    @mapper.Relation
    def infosTouristique(cls, InfoTouristique, Commune):
        return sa.orm.relation(InfoTouristique,
                               secondary=Commune.__table__,
                               lazy=True)
