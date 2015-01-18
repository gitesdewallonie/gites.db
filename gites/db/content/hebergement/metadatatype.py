# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class MetadataType(GitesMappedClassBase):
    """
    Table décrivant les différents types de métadata en plusieurs longues
    """

    __tablename__ = u'metadata_type'

    met_typ_id = sa.Column('met_typ_id', sa.String(),
                           nullable=False,
                           primary_key=True,
                           unique=True,
                           doc=u"Identifiant unique pour un type de métadata")

    met_typ_titre = sa.Column('met_typ_titre', sa.String(),
                              nullable=False,
                              doc=u"Type de la métadata")

    met_typ_sort_ord = sa.Column('met_typ_sort_ord', sa.Integer(),
                                 nullable=False,
                                 unique=True,
                                 doc=u"Tri du type de la métadata")
