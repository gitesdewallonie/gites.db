# encoding: utf-8
"""
gites.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from gites.db.mapper import GitesMappedClassBase
import sqlalchemy as sa


class LogModification(GitesMappedClassBase):
    __tablename__ = u'log_modification'

    pk = sa.Column('pk', sa.Integer, primary_key=True, unique=True)

    date = sa.Column('date', sa.DateTime, nullable=False)

    user = sa.Column('user', sa.String)

    table = sa.Column('table', sa.String, nullable=False)

    column = sa.Column('column', sa.String, nullable=False)

    table_pk = sa.Column('table_pk', sa.String, nullable=False),

    old_value = sa.Column('old_value', sa.String)

    new_value = sa.Column('new_value', sa.String)
