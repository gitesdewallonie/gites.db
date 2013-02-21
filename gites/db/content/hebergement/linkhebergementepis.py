# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class LinkHebergementEpis(GitesMappedClassBase):
    __tablename__ = u'link_hebergement_epis'

    heb_pk = sa.Column('heb_pk', sa.Integer,
                       sa.ForeignKey('hebergement.heb_pk'), primary_key=True)

    heb_nombre_epis = sa.Column('heb_nombre_epis', sa.Integer,
                                primary_key=True)
