"""empty message

Revision ID: 5ad88f4593f7
Revises: abb9cde33d6
Create Date: 2013-06-25 09:47:27.305150

"""

# revision identifiers, used by Alembic.
revision = '5ad88f4593f7'
down_revision = 'abb9cde33d6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    print "... Add the heb_tarif_charge column in hebergement"
    op.add_column('hebergement', sa.Column('heb_tarif_charge', sa.String()))


def downgrade():
    print "... Remove the heb_tarif_charge column in hebergement"
    op.drop_column('hebergement', 'heb_tarif_charge')
