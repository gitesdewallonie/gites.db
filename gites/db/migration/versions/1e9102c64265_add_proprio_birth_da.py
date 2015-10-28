"""Add proprio birth date

Revision ID: 1e9102c64265
Revises: 1de3a443694f
Create Date: 2015-10-28 11:58:56.563965

"""

# revision identifiers, used by Alembic.
revision = '1e9102c64265'
down_revision = '1de3a443694f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    print "... Add prod_date_naiss to proprio and proprio_maj"
    op.add_column('proprio',
                  sa.Column('pro_date_naiss', sa.Date))
    op.add_column('proprio_maj',
                  sa.Column('pro_maj_date_naiss', sa.Date))


def downgrade():
    print "... Drop pro_date_naiss to proprio and proprio_maj"
    op.drop_column('proprio', 'pro_date_naiss')
    op.drop_column('proprio_maj', 'pro_maj_date_naiss')
