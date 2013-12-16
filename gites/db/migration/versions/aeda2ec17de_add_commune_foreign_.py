# -*- coding: utf-8 -*-

"""Add commune foreign key

Revision ID: aeda2ec17de
Revises: 589720778844
Create Date: 2013-12-16 11:41:07.773703

"""

# revision identifiers, used by Alembic.
revision = 'aeda2ec17de'
down_revision = '589720778844'

from alembic import op


def upgrade():
    print "Add foreign key to heb_com_fk..."
    op.execute("""ALTER TABLE hebergement ADD CONSTRAINT hebebergement_commune_fk FOREIGN KEY (heb_com_fk) REFERENCES commune (com_pk) MATCH FULL;""")


def downgrade():
    print "Remove foreign key to heb_com_fk..."
    op.execute("""ALTER TABLE hebergement DROP CONSTRAINT hebebergement_commune_fk;""")
