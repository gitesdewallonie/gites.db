"""Add sort order on metadata types

Revision ID: 117acbc43638
Revises: 7503ac31724
Create Date: 2013-07-17 12:20:27.884046

"""

# revision identifiers, used by Alembic.
revision = '117acbc43638'
down_revision = '7503ac31724'

from alembic import op
import sqlalchemy as sa


def upgrade():
    print "... Adding and filling column met_typ_sort_ord on metadata_type"
    op.add_column('metadata_type', sa.Column('met_typ_sort_ord', sa.Integer(), unique=True))
    op.execute("UPDATE metadata_type SET met_typ_sort_ord = 1 WHERE met_typ_id = 'informations'")
    op.execute("UPDATE metadata_type SET met_typ_sort_ord = 2 WHERE met_typ_id = 'autorisations'")
    op.execute("UPDATE metadata_type SET met_typ_sort_ord = 3 WHERE met_typ_id = 'confort'")
    op.execute("UPDATE metadata_type SET met_typ_sort_ord = 4 WHERE met_typ_id = 'activites'")
    op.execute("UPDATE metadata_type SET met_typ_sort_ord = 5 WHERE met_typ_id = 'gitesplus'")
    op.execute("UPDATE metadata_type SET met_typ_sort_ord = 6 WHERE met_typ_id = 'themes'")
    op.execute("UPDATE metadata_type SET met_typ_sort_ord = 7 WHERE met_typ_id = 'tablehote'")
    op.execute("UPDATE metadata_type SET met_typ_sort_ord = 8 WHERE met_typ_id = 'autres'")


def downgrade():
    print "... Removing column met_typ_sort_ord from metadata_type"
    op.drop_column('metadata_type', 'met_typ_sort_ord')
