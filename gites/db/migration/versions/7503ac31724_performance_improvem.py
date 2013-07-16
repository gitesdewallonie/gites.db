"""performance_improvement

Revision ID: 7503ac31724
Revises: 5ad88f4593f7
Create Date: 2013-07-16 14:14:57.554631

"""

# revision identifiers, used by Alembic.
revision = '7503ac31724'
down_revision = '5ad88f4593f7'

from alembic import op


def upgrade():
    op.create_index('heb_public_idx', 'hebergement', ['heb_site_public'])
    op.create_index('heb_public_group_idx', 'hebergement', ['heb_site_public', 'heb_groupement_pk'])
    op.create_index('pro_etat_idx', 'proprio', ['pro_etat'])


def downgrade():
    op.drop_index('heb_public_idx', 'hebergement')
    op.drop_index('pro_etat_idx', 'proprio')
