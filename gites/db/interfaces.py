# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from zope.interface import Interface


class IHebergement(Interface):
    """
    Describe an Hebergement
    """


class ICommune(Interface):
    """
    A commune
    """


class ITypeHebergement(Interface):
    """
    A type of Hebergement
    """


class IInfoTouristique(Interface):
    """
    List of infos touristiques
    """


class IMaisonTourisme(Interface):
    """
    Describe a maison du tourisme
    """


class IProprioMaj(Interface):
    """
    mise à jour des infos proprio by the prorpio
    """


class IHebergementMaj(Interface):
    """
    mise à jour des infos hebergement by the prorpio
    """