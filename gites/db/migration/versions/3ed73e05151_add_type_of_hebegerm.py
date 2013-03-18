"""Add type of hebegerment type

Revision ID: 3ed73e05151
Revises: 2c5d0d558739
Create Date: 2013-03-18 14:47:17.279665

"""

# revision identifiers, used by Alembic.
revision = '3ed73e05151'
down_revision = '2c5d0d558739'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


def upgrade():
    op.add_column('type_heb', sa.Column('type_heb_type', sa.String()))
    type_heb = table('type_heb',
                     column('type_heb_code', sa.String),
                     column('type_heb_type', sa.String))
    CHAMBRES = ['CH', 'MH', 'CHECR']
    GITES = ['GR', 'GF', 'MT', 'GC', 'MV', 'GRECR', 'GG']
    op.execute(
        type_heb.update().
        where(type_heb.c.type_heb_code.in_(CHAMBRES)).
        values({'type_heb_type': op.inline_literal('chambre')}))
    op.execute(
        type_heb.update().
        where(type_heb.c.type_heb_code.in_(GITES)).
        values({'type_heb_type': op.inline_literal('gites')}))


def downgrade():
    op.drop_column('type_heb', 'type_heb_type')
