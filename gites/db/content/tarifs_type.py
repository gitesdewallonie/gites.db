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
    __tablename__ = 'tarifs_type'

    type = sa.Column('type', sa.String, primary_key=True, nullable=False)

    subtype = sa.Column('subtype', sa.String, primary_key=True, nullable=False)
