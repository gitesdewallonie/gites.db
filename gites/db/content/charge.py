# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the <+ LICENSE +> license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from z3c.sqlalchemy.mapper import MappedClassBase
from Acquisition import Implicit
from Globals import InitializeClass


class Charge(Implicit, MappedClassBase):
    """
    Les charge d'un hebergement
    """

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

InitializeClass(Charge)
