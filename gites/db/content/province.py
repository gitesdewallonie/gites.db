# -*- coding: utf-8 -*-
import sqlalchemy as sa
from affinitic.db import mapper
from gites.db.mapper import GitesMappedClassBase


class Province(GitesMappedClassBase):
    """
    Table permettant de gérer les informations des provinces
    """

    __tablename__ = u'provinces'

    prov_pk = sa.Column('prov_pk', sa.Integer,
                        primary_key=True,
                        doc=u"Identifiant unique")

    prov_nom = sa.Column('prov_nom', sa.String(),
                         doc=u"Nom de la province")

    @mapper.RelationImport('gites.db.content:Hebergement',
                           'gites.db.content:Commune')
    @mapper.Relation
    def relatedHebergement(cls, Hebergement, Commune):
        return sa.orm.relation(Hebergement, lazy=True,
                               secondary=Commune.__table__)
