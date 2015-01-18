# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class LinkHebergementEpis(GitesMappedClassBase):
    """
    Table de jointure permettant de gérer nombre d'épis d'un hébergement.
    """

    __tablename__ = u'link_hebergement_epis'

    heb_pk = sa.Column('heb_pk', sa.Integer,
                       sa.ForeignKey('hebergement.heb_pk'),
                       primary_key=True,
                       doc=u"Numéro d'identifiant unique vers la table hébergement")

    heb_nombre_epis = sa.Column('heb_nombre_epis', sa.Integer,
                                primary_key=True,
                                doc=u"Nombre d'épis de hébergement")
