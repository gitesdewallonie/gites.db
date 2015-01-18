# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase
from zope.interface import implements
from gites.db.interfaces import ITypeInfoPratique


class TypeInfoPratique(GitesMappedClassBase):
    implements(ITypeInfoPratique)
    """
    Table permettant de gérer les types d'informations pratiques
    """

    __tablename__ = u'type_info_pratique'

    typinfoprat_pk = sa.Column('typinfoprat_pk', sa.Integer,
                               primary_key=True,
                               doc=u"Numéro d'identifiant unique")

    typinfoprat_nom_fr = sa.Column('typinfoprat_nom_fr', sa.String(),
                                   doc=u"Nom de l'information pratique version française")

    typinfoprat_nom_nl = sa.Column('typinfoprat_nom_nl', sa.String(),
                                   doc=u"Nom de l'information pratique version néerlandaise")

    typinfoprat_nom_en = sa.Column('typinfoprat_nom_en', sa.String(),
                                   doc=u"Nom de l'information pratique version anglaise")

    typinfoprat_nom_it = sa.Column('typinfoprat_nom_it', sa.String(),
                                   doc=u"Nom de l'information pratique version italienne")

    typinfoprat_nom_de = sa.Column('typinfoprat_nom_de', sa.String(),
                                   doc=u"Nom de l'information pratique version allemande")

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
