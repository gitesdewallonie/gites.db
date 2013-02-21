# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class Metadata(GitesMappedClassBase):
    __tablename__ = u'metadata'

    met_pk = sa.Column('met_pk', sa.Integer, nullable=False, primary_key=True,
                       unique=True)

    met_id = sa.Column('met_id', sa.String(), nullable=False)

    met_titre_fr = sa.Column('met_titre_fr', sa.String(), nullable=False)

    met_titre_en = sa.Column('met_titre_en', sa.String(), nullable=False)

    met_titre_nl = sa.Column('met_titre_nl', sa.String(), nullable=False)

    met_titre_it = sa.Column('met_titre_it', sa.String(), nullable=False)

    met_titre_de = sa.Column('met_titre_de', sa.String(), nullable=False)

    met_filterable = sa.Column('met_filterable', sa.Boolean(), default=False)
