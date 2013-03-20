# -*- coding: utf-8 -*-
import sqlalchemy as sa
from zope.interface import implements
from gites.db.interfaces import IMaisonTourisme
from gites.db.mapper import GitesMappedClassBase


class MaisonTourisme(GitesMappedClassBase):
    implements(IMaisonTourisme)
    __tablename__ = u'maison_tourisme'

    mais_pk = sa.Column('mais_pk', sa.Integer, primary_key=True)

    mais_nom = sa.Column('mais_nom', sa.String())

    mais_url = sa.Column('mais_url', sa.String())

    mais_gps_lat = sa.Column('mais_gps_lat', sa.Float())

    mais_gps_long = sa.Column('mais_gps_long', sa.Float())

    def getCommunesName(self):
        return [commune.com_nom for commune in self.commune]

    com_nom = property(getCommunesName)

    @classmethod
    def __declare_last__(cls):
        from gites.db.content import Commune
        from gites.db.content import InfoTouristique

        cls.commune = sa.orm.relation(Commune, lazy=True)

        cls.infosTouristique = sa.orm.relation(InfoTouristique,
                                               secondary=Commune.__table__,
                                               lazy=True)
