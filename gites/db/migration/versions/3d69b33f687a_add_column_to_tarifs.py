"""add column to tarifs_type

Revision ID: 3d69b33f687a
Revises: 433640f46150
Create Date: 2014-06-24 12:36:52.162926

"""

# revision identifiers, used by Alembic.
revision = '3d69b33f687a'
down_revision = '433640f46150'

from alembic import op
import sqlalchemy as sa


def upgrade():
    print "... Add gite and chambre column to tarifs_type"
    op.add_column('tarifs_type',
                  sa.Column('gite', sa.Boolean, default=False))
    op.add_column('tarifs_type',
                  sa.Column('chambre', sa.Boolean, default=False))

    op.execute("""UPDATE tarifs_type SET gite = true, chambre = false
               WHERE "type" in ('LOW_SEASON', 'MEDIUM_SEASON', 'FEAST_WEEKEND', 'HIGH_SEASON', 'CHARGES');""")

    op.execute("""UPDATE tarifs_type SET gite = false, chambre = true
               WHERE "type" = 'ROOM';""")

    op.execute("""UPDATE tarifs_type SET gite = true, chambre = true
               WHERE "type" = 'OTHER';""")

    op.execute("ALTER TABLE tarifs_type ALTER COLUMN gite SET NOT NULL;")
    op.execute("ALTER TABLE tarifs_type ALTER COLUMN chambre SET NOT NULL;")


def downgrade():
    print "... Drop gite and chambre column to tarifs_type"
    op.drop_column('tarifs_type', 'gite')
    op.drop_column('tarifs_type', 'chambre')
