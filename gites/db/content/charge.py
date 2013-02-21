# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the <+ LICENSE +> license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class Charge(GitesMappedClassBase):
    """
    Les charge d'un hebergement
    """
    __tablename__ = u'charge'

    cha_pk = sa.Column('cha_pk', sa.Integer, primary_key=True)

    cha_type_fr = sa.Column('cha_type_fr', sa.String())

    cha_type_en = sa.Column('cha_type_en', sa.String())

    cha_type_nl = sa.Column('cha_type_nl', sa.String())

    cha_type_de = sa.Column('cha_type_de', sa.String())

    cha_type_it = sa.Column('cha_type_it', sa.String())

    def getTitle(self, languageCode):
        if 'fr' in languageCode:
            return self.cha_type_fr
        elif 'nl' in languageCode:
            return self.cha_type_nl
        elif 'it' in languageCode:
            return self.cha_type_it
        elif 'de' in languageCode:
            return self.cha_type_de
        else:
            return self.cha_type_en
