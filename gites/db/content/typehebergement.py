# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from Acquisition import Implicit
from Globals import InitializeClass
from z3c.sqlalchemy.mapper import MappedClassBase
from zope.interface import implements
from gites.db.interfaces import ITypeHebergement


class TypeHebergement(Implicit, MappedClassBase):
    implements(ITypeHebergement)

    c = None

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

InitializeClass(TypeHebergement)
