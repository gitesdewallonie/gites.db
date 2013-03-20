# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
import sqlalchemy
from sqlalchemy.orm import relation
from zope.interface import implements
from affinitic.caching import cache
from gites.db import session
from gites.db.content.charge import Charge
from gites.db.content.proprio.proprio import Proprio
from gites.db.content.hebergement.typehebergement import TypeHebergement
from gites.db.interfaces import IHebergement
from gites.db.mapper import GitesMappedClassBase


class Hebergement(GitesMappedClassBase):
    implements(IHebergement)
    __tablename__ = u'hebergement'

    heb_pk = sqlalchemy.Column('heb_pk', sqlalchemy.Integer, primary_key=True)

    heb_nom = sqlalchemy.Column('heb_nom', sqlalchemy.String())

    heb_code_gdw = sqlalchemy.Column('heb_code_gdw', sqlalchemy.String())

    heb_code_gdw = sqlalchemy.Column('heb_code_gdw', sqlalchemy.String())

    heb_site_public = sqlalchemy.Column('heb_site_public', sqlalchemy.String())

    heb_calendrier_proprio = sqlalchemy.Column('heb_calendrier_proprio', sqlalchemy.String())

    heb_charge_fk = sqlalchemy.Column('heb_charge_fk', sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey('charge.cha_pk'))

    heb_com_fk = sqlalchemy.Column('heb_com_fk', sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('commune.com_pk'))

    heb_typeheb_fk = sqlalchemy.Column('heb_typeheb_fk', sqlalchemy.Integer,
                                       sqlalchemy.ForeignKey('type_heb.type_heb_pk'))

    heb_pro_fk = sqlalchemy.Column('heb_pro_fk', sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('proprio.pro_pk'))

    heb_calendrier_proprio_date_maj = sqlalchemy.Column('heb_calendrier_proprio_date_maj', sqlalchemy.Date)

    def Title(self):
        language = self.REQUEST.get('LANGUAGE', 'en')
        typeHeb = self.type.getTitle(language)
        return u"%s - %s - %s" % (typeHeb, self.heb_nom, self.heb_localite)

    def getVignette(self):
        return "%s00.jpg" % (self.heb_code_gdw)

    def getProprioName(self):
        return self.proprio.pro_nom1

    proprioName = property(getProprioName)

    def getMaisonTourisme(self):
        return self.maisonTourisme[0]

    def getSituation(self, languageCode):
        if 'fr' in languageCode:
            return self.heb_pointfort_fr
        elif 'nl' in languageCode:
            return self.heb_pointfort_nl
        elif 'it' in languageCode:
            return self.heb_pointfort_it
        elif 'de' in languageCode:
            return self.heb_pointfort_de
        else:
            return self.heb_pointfort_uk

    def getDescription(self, languageCode):
        if 'fr' in languageCode:
            return self.heb_descriptif_fr
        elif 'nl' in languageCode:
            return self.heb_descriptif_nl
        elif 'it' in languageCode:
            return self.heb_descriptif_it
        elif 'de' in languageCode:
            return self.heb_descriptif_de
        else:
            return self.heb_descriptif_uk

    def getDistribution(self, languageCode):
        if 'fr' in languageCode:
            return self.heb_distribution_fr
        elif 'nl' in languageCode:
            return self.heb_distribution_nl
        elif 'it' in languageCode:
            return self.heb_distribution_it
        elif 'de' in languageCode:
            return self.heb_distribution_de
        else:
            return self.heb_distribution_uk

    def getSeminaireVert(self, languageCode):
        if 'fr' in languageCode:
            return self.heb_seminaire_vert_fr
        elif 'nl' in languageCode:
            return self.heb_seminaire_vert_nl
        elif 'it' in languageCode:
            return self.heb_seminaire_vert_it
        elif 'de' in languageCode:
            return self.heb_seminaire_vert_de
        else:
            return self.heb_seminaire_vert_uk

    @classmethod
    def __declare_last__(cls):
        from gites.db.content import LinkHebergementEpis
        from gites.db.content import Province
        from gites.db.content import Commune
        from gites.db.content import MaisonTourisme
        from gites.db.content import Metadata
        from gites.db.content import LinkHebergementMetadata
        from gites.db.content import ReservationProprio

        cls.type = relation(TypeHebergement, lazy=True)

        cls.proprio = relation(Proprio, lazy=True, backref='hebergements')

        cls.reservations = relation(ReservationProprio, lazy=True, backref='hebergement')

        cls.charge = relation(Charge, lazy=True)

        cls.commune = relation(Commune, lazy=True)

        cls.epis = relation(LinkHebergementEpis, lazy=True)

        cls.province = relation(Province,
                                secondary=Commune.__tablename__,
                                lazy=True)

        cls.maisonTourisme = relation(MaisonTourisme,
                                      secondary=Commune.__tablename__,
                                      lazy=True)

        cls.activeMetadatas = relation(Metadata,
                                       secondary=LinkHebergementMetadata.__tablename__,
                                       primaryjoin=sqlalchemy.and_(Hebergement.heb_pk == LinkHebergementMetadata.heb_fk,
                                                                   LinkHebergementMetadata.link_met_value == True),
                                       lazy=True)

        cls.metadatas = relation(Metadata,
                                 secondary=LinkHebergementMetadata.__tablename__,
                                 primaryjoin=(Hebergement.heb_pk == LinkHebergementMetadata.heb_fk),
                                 lazy=True)
