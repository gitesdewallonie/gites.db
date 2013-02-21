# -*- coding: utf-8 -*-
import sqlalchemy as sa
from sqlalchemy.orm import relation
from gites.db.mapper import GitesMappedClassBase


class Province(GitesMappedClassBase):
    __tablename__ = u'provinces'

    prov_pk = sa.Column('prov_pk', sa.Integer,
                        primary_key=True)

    prov_nom = sa.Column('prov_nom', sa.String())

    @classmethod
    def __declare_last__(cls):
        from gites.db.content import Hebergement
        from gites.db.content import Commune

        cls.relatedHebergement = relation(Hebergement, lazy=True,
                                          secondary=Commune.__table__)
