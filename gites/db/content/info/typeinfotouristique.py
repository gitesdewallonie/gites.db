# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase
from zope.interface import implements
from gites.db.interfaces import ITypeInfoTouristique


class TypeInfoTouristique(GitesMappedClassBase):
    implements(ITypeInfoTouristique)
    __tablename__ = u'type_info_touristique'

    typinfotour_pk = sa.Column('typinfotour_pk', sa.Integer, primary_key=True)

    typinfotour_nom_fr = sa.Column('typinfotour_nom_fr', sa.String())

    typinfotour_nom_nl = sa.Column('typinfotour_nom_nl', sa.String())

    typinfotour_nom_en = sa.Column('typinfotour_nom_en', sa.String())

    typinfotour_nom_it = sa.Column('typinfotour_nom_it', sa.String())

    typinfotour_nom_de = sa.Column('typinfotour_nom_de', sa.String())

    def getName(self, languageCode='fr'):
        """
        Get the name following the language (handle fr_BE, nl_BE ...)
        """
        if 'fr' in languageCode:
            return self.typinfotour_nom_fr
        elif 'nl' in languageCode:
            return self.typinfotour_nom_nl
        elif 'it' in languageCode:
            return self.typinfotour_nom_it
        elif 'de' in languageCode:
            return self.typinfotour_nom_de
        else:
            return self.typinfotour_nom_en
