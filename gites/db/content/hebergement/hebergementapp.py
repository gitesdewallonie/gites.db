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
    __tablename__ = u'hebergement_app'

    heb_app_pk = sqlalchemy.Column('heb_app_pk', sqlalchemy.Integer,
                                   primary_key=True, unique=True,
                                   nullable=False)

    heb_app_sort_order = sqlalchemy.Column('heb_app_sort_order',
                                           sqlalchemy.Integer)

    heb_app_heb_fk = sqlalchemy.Column('heb_app_heb_fk', sqlalchemy.Integer,
                                       sqlalchemy.ForeignKey('hebergement.heb_pk'))

    @mapper.Relation
    def hebergement(cls):
        return sqlalchemy.orm.relation(Hebergement, lazy=True, uselist=False,
                                       backref=sqlalchemy.orm.backref('app', uselist=False))
