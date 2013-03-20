"""empty message

Revision ID: 3541c34a3d30
Revises: 597e9bc85819
Create Date: 2013-03-20 11:49:53.429701

"""

# revision identifiers, used by Alembic.
revision = '3541c34a3d30'
down_revision = '597e9bc85819'

from alembic import op
import sqlalchemy as sa


def upgrade():
    print "... Adds the editable column"
    op.add_column('metadata',
                  sa.Column('met_editable', sa.Boolean(), default=False))


def downgrade():
    print "... Removes the editable column"
    op.drop_column('metadata', 'met_editable')
