"""Change type_heb_type from gites to gite

Revision ID: 12d330dedc11
Revises: 212bf3d91b4a
Create Date: 2013-04-10 12:18:53.756207

"""

# revision identifiers, used by Alembic.
revision = '12d330dedc11'
down_revision = '212bf3d91b4a'

from alembic import op


def upgrade():
    op.execute("""UPDATE type_heb SET type_heb_type = 'gite' WHERE type_heb_type = 'gites'""")


def downgrade():
    op.execute("""UPDATE type_heb SET type_heb_type = 'gites' WHERE type_heb_type = 'gite'""")
