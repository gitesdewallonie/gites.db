# -*- coding: utf-8 -*-
import sqlalchemy
from gites.db.interfaces import ITypeTableHoteOfHebergementMaj
from gites.db.mapper import GitesMappedClassBase
from zope.interface import implements


class TypeTableHoteOfHebergementMaj(GitesMappedClassBase):
    implements(ITypeTableHoteOfHebergementMaj)
    """
    Table permettant de gérer la mise à jour du type de tables d'hôte
    """

    __tablename__ = u'heb_tab_hote_maj'

    hebhot_heb_fk = sqlalchemy.Column('hebhot_maj_heb_fk', sqlalchemy.Integer,
                                      primary_key=True,
                                      doc=u"Numéro d'identifiant unique vers la table hébergement")

    hebhot_tabho_fk = sqlalchemy.Column('hebhot_maj_tabho_fk', sqlalchemy.Integer,
                                        primary_key=True,
                                        doc=u"Numéro d'identifiant unique vers la table type table d'hôte")
