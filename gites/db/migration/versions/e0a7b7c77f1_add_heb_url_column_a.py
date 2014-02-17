"""Add heb_url column and migrate pro_url URLs

Revision ID: e0a7b7c77f1
Revises: aeda2ec17de
Create Date: 2014-02-17 15:10:11.349201

"""

# revision identifiers, used by Alembic.
revision = 'e0a7b7c77f1'
down_revision = 'aeda2ec17de'

from alembic import op
import sqlalchemy as sa


def upgrade():
    print "... Add heb_url and heb_maj_url columns"
    op.add_column('hebergement',
                  sa.Column('heb_url', sa.String()))
    op.add_column('hebergement_maj',
                  sa.Column('heb_maj_url', sa.String()))
    print "... Fill hebergement.heb_url data from proprio.pro_url"
    op.execute("""UPDATE hebergement
                  SET heb_url = (SELECT pro_url
                                 FROM proprio
                                 WHERE hebergement.heb_pro_fk = proprio.pro_pk)
               """)


def downgrade():
    print "... Drop heb_url and heb_maj_url columns"
    op.drop_column('hebergement', 'heb_url')
    op.drop_column('hebergement_maj', 'heb_maj_url')
