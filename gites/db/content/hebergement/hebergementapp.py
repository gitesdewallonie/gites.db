# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import sqlalchemy
from affinitic.db import mapper
from gites.db.content.hebergement.hebergement import Hebergement
from gites.db.mapper import GitesMappedClassBase


class HebergementApp(GitesMappedClassBase):
    """
    Table permettant de gérer le dessin de localisation des groupements
    des hébergement sur la carte pour l'appli mobile ???
    """

    __tablename__ = u'hebergement_app'

    heb_app_pk = sqlalchemy.Column('heb_app_pk', sqlalchemy.Integer,
                                   primary_key=True,
                                   unique=True,
                                   nullable=False,
                                   doc=u"Identifiant unique pour un hébergement ???")

    heb_app_sort_order = sqlalchemy.Column('heb_app_sort_order',
                                           sqlalchemy.Integer,
                                           doc=u"Tri des hébergements ???")

    heb_app_heb_fk = sqlalchemy.Column('heb_app_heb_fk', sqlalchemy.Integer,
                                       sqlalchemy.ForeignKey('hebergement.heb_pk'),
                                       doc=u"Numéro d'identifiant unique vers la table hébergement")

    heb_app_groupement_line_length = sqlalchemy.Column('heb_app_groupement_line_length', sqlalchemy.Integer(),
                                                       doc=u"Longueur de la ligne dessinnée sur la carte ???")

    heb_app_groupement_angle_start = sqlalchemy.Column('heb_app_groupement_angle_start', sqlalchemy.Float(),
                                                       doc=u"Angle de la ligne pointant sur l'hébergement  ???")

    @mapper.Relation
    def hebergement(cls):
        return sqlalchemy.orm.relation(Hebergement, lazy=True, uselist=False,
                                       backref=sqlalchemy.orm.backref('app', uselist=False))
