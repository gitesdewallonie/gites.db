#NOCHECK
# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from z3c.sqlalchemy.mapper import MappedClassBase
from charge import Charge
from commune import Commune
from hebergement import Hebergement
from infotouristique import InfoTouristique
from maisontourisme import MaisonTourisme
from typehebergement import TypeHebergement


class Proprio(MappedClassBase):
    c = None


class Civilite(MappedClassBase):
    c = None


class Province(MappedClassBase):
    c = None


class TableHote(MappedClassBase):
    c = None


class TypeTableHoteOfHebergement(MappedClassBase):
    c = None


class LinkHebergementEpis(object):
    pass
