# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from z3c.sqlalchemy.mapper import MappedClassBase
from zope.interface import implements
from gites.db.interfaces import IMaisonTourisme


class MaisonTourisme(MappedClassBase):
    implements(IMaisonTourisme)

    def getCommunesName(self):
        return [commune.com_nom for commune in self.commune]

    com_nom = property(getCommunesName)
