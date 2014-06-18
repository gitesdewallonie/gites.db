# -*- coding: utf-8 -*-
import sqlalchemy as sa
from zope.i18n import translate
from zope.interface import implements
from gites.db.interfaces import ITypeHebergement
from gites.db.mapper import GitesMappedClassBase
from OFS.Traversable import Traversable


class TypeHebergement(GitesMappedClassBase, Traversable):
    implements(ITypeHebergement)
    __tablename__ = u'type_heb'

    type_heb_pk = sa.Column('type_heb_pk', sa.Integer, primary_key=True)

    type_heb_code = sa.Column('type_heb_code', sa.String())

    type_heb_nom = sa.Column('type_heb_nom', sa.String())

    type_heb_id = sa.Column('type_heb_id', sa.String())

    type_heb_id_nl = sa.Column('type_heb_id_nl', sa.String())

    type_heb_id_de = sa.Column('type_heb_id_de', sa.String())

    type_heb_id_it = sa.Column('type_heb_id_it', sa.String())

    type_heb_id_uk = sa.Column('type_heb_id_uk', sa.String())

    type_heb_nom_nl = sa.Column('type_heb_nom_nl', sa.String())

    type_heb_nom_de = sa.Column('type_heb_nom_de', sa.String())

    type_heb_nom_it = sa.Column('type_heb_nom_it', sa.String())

    type_heb_nom_uk = sa.Column('type_heb_nom_uk', sa.String())

    type_heb_type = sa.Column('type_heb_type', sa.String())

    def getType(self):
        from zope.globalrequest import getRequest
        request = getRequest()
        return translate(self.type_heb_type, context=request, domain='gites')

    def getTitle(self, languageCode='fr'):
        """
        Get the id following the language (handle fr_BE, nl_BE ...)
        """
        if 'fr' in languageCode:
            return self.type_heb_nom
        elif 'nl' in languageCode:
            return self.type_heb_nom_nl
        elif 'it' in languageCode:
            return self.type_heb_nom_it
        elif 'de' in languageCode:
            return self.type_heb_nom_de
        else:
            return self.type_heb_nom_uk

    def getId(self, languageCode='fr'):
        """
        Get the id following the language (handle fr_BE, nl_BE ...)
        """
        if 'fr' in languageCode:
            return self.type_heb_id
        elif 'nl' in languageCode:
            return self.type_heb_id_nl
        elif 'it' in languageCode:
            return self.type_heb_id_it
        elif 'de' in languageCode:
            return self.type_heb_id_de
        else:
            return self.type_heb_id_uk