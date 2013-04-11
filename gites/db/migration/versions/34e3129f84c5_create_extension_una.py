"""CREATE EXTENSION unaccent

Revision ID: 34e3129f84c5
Revises: 12d330dedc11
Create Date: 2013-04-11 13:03:09.999076

"""

# revision identifiers, used by Alembic.
revision = '34e3129f84c5'
down_revision = '12d330dedc11'

from alembic import op


def upgrade():
    print "... creating extension unaccent"
    op.execute("""CREATE EXTENSION unaccent""")


def downgrade():
    print "... dropping extension unaccent"
    op.execute("""DROP EXTENSION unaccent""")
