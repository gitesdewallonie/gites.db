# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase
from zope.interface import implements
from gites.db.interfaces import ITypeInfoPratique


class TypeInfoPratique(GitesMappedClassBase):
    implements(ITypeInfoPratique)
    __tablename__ = u'type_info_pratique'

    typinfoprat_pk = sa.Column('typinfoprat_pk', sa.Integer, primary_key=True)

    typinfoprat_nom_fr = sa.Column('typinfoprat_nom_fr', sa.String())

    typinfoprat_nom_nl = sa.Column('typinfoprat_nom_nl', sa.String())

    typinfoprat_nom_en = sa.Column('typinfoprat_nom_en', sa.String())

    typinfoprat_nom_it = sa.Column('typinfoprat_nom_it', sa.String())

    typinfoprat_nom_de = sa.Column('typinfoprat_nom_de', sa.String())

    def getName(self, languageCode='fr'):
        """
        Get the name following the language (handle fr_BE, nl_BE ...)
        """
        if 'fr' in languageCode:
            return self.typinfoprat_nom_fr
        elif 'nl' in languageCode:
            return self.typinfoprat_nom_nl
        elif 'it' in languageCode:
            return self.typinfoprat_nom_it
        elif 'de' in languageCode:
            return self.typinfoprat_nom_de
        else:
            return self.typinfoprat_nom_en
