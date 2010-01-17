# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from z3c.sqlalchemy.mapper import MappedClassBase
from gites.db.interfaces import ITypeTableHoteOfHebergementMaj
from zope.interface import implements
from Acquisition import Implicit
from Globals import InitializeClass


class TypeTableHoteOfHebergementMaj(Implicit, MappedClassBase):
    implements(ITypeTableHoteOfHebergementMaj)

    c = None

InitializeClass(TypeTableHoteOfHebergementMaj)
