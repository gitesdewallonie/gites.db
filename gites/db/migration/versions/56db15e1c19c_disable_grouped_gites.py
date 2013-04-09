"""Disable grouped gites

Revision ID: 56db15e1c19c
Revises: 15a763628bf5
Create Date: 2013-04-09 10:28:24.519053

"""

# revision identifiers, used by Alembic.
revision = '56db15e1c19c'
down_revision = '15a763628bf5'

from alembic import op


def upgrade():
    print "... Disable all grouped gites"
    op.execute("UPDATE hebergement SET heb_site_public = '0' WHERE heb_typeheb_fk = 11")


def downgrade():
    print "... You don't want to go back, I promise !"
