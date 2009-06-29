# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from z3c.sqlalchemy.mapper import MappedClassBase
from zope.interface import implements
from gites.db.interfaces import IInfoTouristique


class InfoTouristique(MappedClassBase):
    implements(IInfoTouristique)

    def getInfoTourisqueName(self):
        """
        get the name of ze info touristique
        """
        return self.info_touristique.infotour_nom

    def getInfoTouristiqueUrl(self):
        """
        get the url of ze info touristique
        """
        return self.info_touristique.infotour_url
