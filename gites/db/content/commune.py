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
from gites.db.content.province import Province
from gites.db.content.maisontourisme import MaisonTourisme
from gites.db.interfaces import ICommune
from OFS.Traversable import Traversable


class Commune(GitesMappedClassBase, Traversable):
    implements(ICommune)
    """
    Table permettant de gérer les informations des communes
    """
    __tablename__ = u'commune'

    com_pk = sqlalchemy.Column('com_pk', sqlalchemy.Integer,
                               primary_key=True,
                               doc=u"Numéro d'identifiant unique")

    com_nom = sqlalchemy.Column('com_nom', sqlalchemy.String(),
                                doc=u"Nom de la commune")

    com_cp = sqlalchemy.Column('com_cp', sqlalchemy.String(),
                               doc=u"Code postale de la commune")

    com_ins = sqlalchemy.Column('com_ins', sqlalchemy.String(),
                                doc=u"""Il s'agit de l'attribution par l'Institut National de la Statistique
                                        d'un numéro de code, en 5 chiffres, à chaque commune.
                                            Le premier chiffre désigne la province.
                                            Le second désigne l'arrondissement administratif de cette province.
                                            Les trois derniers chiffres varient selon les différentes communes d'un même arrondissement.""")

    com_reg_fk = sqlalchemy.Column('com_reg_fk', sqlalchemy.Integer,
                                   doc=u"Numéro d'identifiant unique vers la table des régions touristiques")

    com_prov_fk = sqlalchemy.Column('com_prov_fk', sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey('provinces.prov_pk'),
                                    doc=u"Numéro d'identifiant unique vers la table province")

    com_id = sqlalchemy.Column('com_id', sqlalchemy.String(),
                               doc=u"Identifiant de la commune")

    com_mais_fk = sqlalchemy.Column('com_mais_fk', sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey('maison_tourisme.mais_pk'),
                                    doc=u"Numéro d'identifiant unique vers la table maison du tourisme")

    def getId(self):
        return self.com_id

    @mapper.RelationImport('gites.db.content:Hebergement')
    @mapper.Relation
    def relatedHebergement(cls, Hebergement):
        return sqlalchemy.orm.relation(Hebergement, lazy=True)

    @mapper.Relation
    def province(cls):
        return sqlalchemy.orm.relation(Province, lazy=True)

    @mapper.Relation
    def maisonTourisme(cls):
        return sqlalchemy.orm.relation(MaisonTourisme, lazy=True)
