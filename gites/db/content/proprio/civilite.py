# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class Civilite(GitesMappedClassBase):
    __tablename__ = u'civilite'

    civ_pk = sa.Column('civ_pk', sa.Integer, primary_key=True)

    civ_titre = sa.Column('civ_titre', sa.String())
