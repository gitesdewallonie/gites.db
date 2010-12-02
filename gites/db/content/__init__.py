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
from proprio_maj import ProprioMaj
from hebergement_maj import HebergementMaj
from typetablehoteofhebergementmaj import TypeTableHoteOfHebergementMaj
from blockinghistory import HebergementBlockingHistory, BlockingHistory
from logitem import LogItem


class Proprio(MappedClassBase):
    c = None


class ProprioMaj(MappedClassBase):
    c = None


class hebergementMaj(MappedClassBase):
    c = None


class Civilite(MappedClassBase):
    c = None


class Province(MappedClassBase):
    c = None


class TableHote(MappedClassBase):
    c = None


class TypeTableHoteOfHebergement(MappedClassBase):
    c = None


class TypeTableHoteOfHebergementMaj(MappedClassBase):
    c = None


class LinkHebergementEpis(object):
    pass


class ReservationProprio(object):
    c = None
