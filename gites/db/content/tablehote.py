# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class TableHote(GitesMappedClassBase):
    """
    Table permettant de gérer les types de tables d'hôtes
    """

    __tablename__ = u'table_hote'

    tabho_pk = sa.Column('tabho_pk', sa.Integer,
                         primary_key=True,
                         doc=u"Numéro d'identifiant unique")

    tabho_type_fr = sa.Column('tabho_type_fr', sa.String(),
                              doc=u"Nom du type de table d'hôte version francophone")
