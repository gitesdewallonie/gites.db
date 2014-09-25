"""Split OTHER columns

Revision ID: 59a12a2f90c0
Revises: 3d69b33f687a
Create Date: 2014-09-25 11:22:48.564026

"""

# revision identifiers, used by Alembic.
revision = '59a12a2f90c0'
down_revision = '3d69b33f687a'

from alembic import op


def upgrade():

    print "... Add OTHER_CLEAN subtype"
    op.execute("""INSERT INTO tarifs_type (type, subtype, gite, chambre)
               VALUES ('OTHER', 'OTHER_CLEAN', true, true);""")

    print "... Migrate tarifs"
    op.execute("""UPDATE tarifs SET subtype = 'OTHER_CLEAN' WHERE subtype = 'OTHER' AND type = 'OTHER';""")

    print "... Remove OTHER subtype"
    op.execute("""DELETE FROM tarifs_type WHERE "type" = 'OTHER' AND "subtype" = 'OTHER';""")


def downgrade():

    print "... Add OTHER subtype"
    op.execute("""INSERT INTO tarifs_type (type, subtype, gite, chambre)
               VALUES ('OTHER', 'OTHER', true, true);""")

    print "... Migrate tarifs"
    op.execute("""UPDATE tarifs SET subtype = 'OTHER' WHERE subtype = 'OTHER_CLEAN' AND type = 'OTHER';""")

    print "... Remove OTHER_CLEAN subtype"
    op.execute("""DELETE FROM tarifs_type WHERE "type" = 'OTHER' AND "subtype" = 'OTHER_CLEAN';""")
