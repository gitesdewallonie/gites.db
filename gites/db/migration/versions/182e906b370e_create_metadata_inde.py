"""Create metadata index

Revision ID: 182e906b370e
Revises: 560c5414140c
Create Date: 2013-03-21 11:26:46.936356

"""

# revision identifiers, used by Alembic.
revision = '182e906b370e'
down_revision = '560c5414140c'

from alembic import op


def upgrade():
    op.create_index('met_id_idx', 'metadata', ['met_id'])
    op.create_index('lnk_heb_fk_idx', 'link_hebergement_metadata',
                    ['heb_fk'])
    op.create_index('lnk_metadata_fk_idx', 'link_hebergement_metadata',
                    ['metadata_fk'])
    op.create_index('lnk_metadata_fk_value_idx', 'link_hebergement_metadata',
                    ['link_met_value', 'metadata_fk'])


def downgrade():
    op.drop_index('met_id_idx', 'metadata')
    op.drop_index('lnk_hb_fk_idx', 'link_hebergement_metadata')
    op.drop_index('lnk_metadata_fk_idx', 'link_hebergement_metadata')
    op.drop_index('lnk_metadata_fk_value_idx', 'link_hebergement_metadata')
