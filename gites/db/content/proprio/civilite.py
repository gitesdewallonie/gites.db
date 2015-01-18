# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class Civilite(GitesMappedClassBase):
    """
    Table permettant de gérer les civilités à l'intetion des propriétaires
    """
    __tablename__ = u'civilite'

    civ_pk = sa.Column('civ_pk', sa.Integer,
                       primary_key=True,
                       doc=u"Numéro d'indentification unique")

    civ_titre = sa.Column('civ_titre', sa.String(),
                          doc=u"Titre de la civilité à l'intention du propriétaire")
