# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from z3c.sqlalchemy.mapper import MappedClassBase


class Package(MappedClassBase):

    c = None

    def Title(self):
        language = self.request.get('LANGUAGE', 'en')
        # typeHeb = self.type.getTitle(language)
        # return u"%s - %s - %s" % (typeHeb, self.heb_nom, self.heb_localite)

    # proprioName = property(getProprioName)
