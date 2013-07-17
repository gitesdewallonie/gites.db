# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class MetadataType(GitesMappedClassBase):
    __tablename__ = u'metadata_type'

    met_typ_id = sa.Column('met_typ_id', sa.String(),
                           nullable=False, primary_key=True, unique=True)

    met_typ_titre = sa.Column('met_typ_titre', sa.String(),
                              nullable=False)

    met_typ_sort_ord = sa.Column('met_typ_sort_ord', sa.Integer(),
                                 nullable=False, unique=True)
