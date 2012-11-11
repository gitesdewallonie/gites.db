# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from z3c.sqlalchemy.mapper import MappedClassBase


class Package(MappedClassBase):

    c = None

    def getDetail(self, languageCode):
        detailProperty = 'detail_%s' % languageCode.lower()
        return getattr(self, detailProperty, None)
