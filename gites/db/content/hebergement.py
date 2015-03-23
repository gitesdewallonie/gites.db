# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from z3c.sqlalchemy.mapper import MappedClassBase
from gites.db.interfaces import IHebergement
from zope.interface import implements
from Acquisition import Implicit
from Globals import InitializeClass


class Hebergement(Implicit, MappedClassBase):
    implements(IHebergement)

    c = None

    def Title(self):
        language = self.REQUEST.get('LANGUAGE', 'en')
        typeHeb = self.type.getTitle(language)
        return u"%s - %s - %s" % (typeHeb, self.heb_nom, self.heb_localite)

    def getVignette(self):
        return "%s00.jpg" % (self.heb_code_gdw)

    def getProprioName(self):
        return self.proprio.pro_nom1

    proprioName = property(getProprioName)

    def getMaisonTourisme(self):
        return self.maisonTourisme[0]

    def getSituation(self, languageCode):
        if 'fr' in languageCode:
            return self.heb_pointfort_fr
        elif 'nl' in languageCode:
            return self.heb_pointfort_nl
        elif 'it' in languageCode:
            return self.heb_pointfort_it
        elif 'de' in languageCode:
            return self.heb_pointfort_de
        else:
            return self.heb_pointfort_uk

    def getDescription(self, languageCode):
        if 'fr' in languageCode:
            return self.heb_descriptif_fr
        elif 'nl' in languageCode:
            return self.heb_descriptif_nl
        elif 'it' in languageCode:
            return self.heb_descriptif_it
        elif 'de' in languageCode:
            return self.heb_descriptif_de
        else:
            return self.heb_descriptif_uk

    def getDistribution(self, languageCode):
        if 'fr' in languageCode:
            return self.heb_distribution_fr
        elif 'nl' in languageCode:
            return self.heb_distribution_nl
        elif 'it' in languageCode:
            return self.heb_distribution_it
        elif 'de' in languageCode:
            return self.heb_distribution_de
        else:
            return self.heb_distribution_uk

    def getSeminaireVert(self, languageCode):
        if 'fr' in languageCode:
            return self.heb_seminaire_vert_fr
        elif 'nl' in languageCode:
            return self.heb_seminaire_vert_nl
        elif 'it' in languageCode:
            return self.heb_seminaire_vert_it
        elif 'de' in languageCode:
            return self.heb_seminaire_vert_de
        else:
            return self.heb_seminaire_vert_uk

InitializeClass(Hebergement)


class HebergementBase(Implicit, MappedClassBase):
    pass
