# -*- coding: utf-8 -*-
import sqlalchemy as sa
from affinitic.db import mapper
from gites.db.mapper import GitesMappedClassBase


class Province(GitesMappedClassBase):
    __tablename__ = u'provinces'

    prov_pk = sa.Column('prov_pk', sa.Integer,
                        primary_key=True)

    prov_nom = sa.Column('prov_nom', sa.String())

    @mapper.RelationImport('gites.db.content:Hebergement',
                           'gites.db.content:Commune')
    @mapper.Relation
    def relatedHebergement(cls, Hebergement, Commune):
        return sa.orm.relation(Hebergement, lazy=True,
                               secondary=Commune.__table__)
