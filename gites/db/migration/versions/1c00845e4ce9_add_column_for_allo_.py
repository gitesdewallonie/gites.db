"""Add column for Allo CH exclusion

Revision ID: 1c00845e4ce9
Revises: 1d026c5b13cb
Create Date: 2013-09-15 18:32:07.990987

"""

# revision identifiers, used by Alembic.
revision = '1c00845e4ce9'
down_revision = '1d026c5b13cb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    print "... Adding heb_desactivation_alloch column"
    op.add_column('hebergement',
                  sa.Column('heb_desactivation_alloch',
                            sa.Boolean(),
                            server_default="false"))


def downgrade():
    print "... Removing heb_desactivation_alloch column"
    op.drop_column('hebergement',
                   'heb_desactivation_alloch')
