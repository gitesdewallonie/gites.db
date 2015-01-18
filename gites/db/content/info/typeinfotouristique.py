# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase
from zope.interface import implements
from gites.db.interfaces import ITypeInfoTouristique


class TypeInfoTouristique(GitesMappedClassBase):
    implements(ITypeInfoTouristique)
    """
    Table permettant de gérer les types d'informations toursitiques
    """

    __tablename__ = u'type_info_touristique'

    typinfotour_pk = sa.Column('typinfotour_pk', sa.Integer,
                               primary_key=True,
                               doc=u"Numéro d'identifiant unique")

    typinfotour_nom_fr = sa.Column('typinfotour_nom_fr', sa.String(),
                                   doc=u"Nom de l'information touristique version française")

    typinfotour_nom_nl = sa.Column('typinfotour_nom_nl', sa.String(),
                                   doc=u"Nom de l'information touristique version néerlandaise")

    typinfotour_nom_en = sa.Column('typinfotour_nom_en', sa.String(),
                                   doc=u"Nom de l'information touristique version anglaise")

    typinfotour_nom_it = sa.Column('typinfotour_nom_it', sa.String(),
                                   doc=u"Nom de l'information touristique version italienne")

    typinfotour_nom_de = sa.Column('typinfotour_nom_de', sa.String(),
                                   doc=u"Nom de l'information touristique version allemande")

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
