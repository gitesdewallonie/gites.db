# encoding: utf-8
"""
gites.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from gites.db.mapper import GitesMappedClassBase
import sqlalchemy as sa


class TarifsType(GitesMappedClassBase):
    """
    Table permettant de gérer les types de tarif.
    """

    __tablename__ = 'tarifs_type'

    type = sa.Column('type', sa.String,
                     primary_key=True,
                     nullable=False,
                     doc=u"Type de tarif")

    subtype = sa.Column('subtype', sa.String,
                        primary_key=True,
                        nullable=False,
                        doc=u"Sous-type de tarif")

    gite = sa.Column('gite', sa.Boolean,
                     nullable=False,
                     doc=u"Tarif applicable au type 'gite' (True/False)")

    chambre = sa.Column('chambre', sa.Boolean,
                        nullable=False,
                        doc=u"Tarif applicable au type 'chambre' (True/False)")
