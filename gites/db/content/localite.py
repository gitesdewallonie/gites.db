# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
import sqlalchemy
from zope.interface import implements
from affinitic.db import mapper
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.commune import Commune
from gites.db.interfaces import ILocalite
from OFS.Traversable import Traversable


class Localite(GitesMappedClassBase, Traversable):
    implements(ILocalite)
    """
    Table permettant de gérer les informations des localités attachées aux communes
    """
    __tablename__ = u'localite'

    localite_pk = sqlalchemy.Column('localite_pk', sqlalchemy.Integer,
                                    primary_key=True,
                                    doc=u"Numéro d'identifiant unique")

    localite_nom = sqlalchemy.Column('localite_nom', sqlalchemy.String(),
                                     doc=u"Nom de la localite")

    localite_cp = sqlalchemy.Column('localite_cp', sqlalchemy.String(),
                                    doc=u"Code postale de la localite")

    localite_ins = sqlalchemy.Column('localite_ins', sqlalchemy.String(),
                                     doc=u"""Il s'agit de l'attribution par l'Institut National de la Statistique
                                             d'un numéro de code, en 5 chiffres, à chaque commune.
                                                 Le premier chiffre désigne la province.
                                                 Le second désigne l'arrondissement administratif de cette province.
                                                 Les trois derniers chiffres varient selon les différentes communes d'un même arrondissement.""")

    localite_commune_fk = sqlalchemy.Column('localite_commune_fk', sqlalchemy.Integer,
                                            sqlalchemy.ForeignKey('commune.com_pk'),
                                            doc=u"Clé permettant de lier une localité à sa commune")


    @mapper.Relation
    def commune(cls):
        return sqlalchemy.orm.relation(Commune, lazy=True)
