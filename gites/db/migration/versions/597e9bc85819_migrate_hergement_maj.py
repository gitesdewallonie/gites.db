"""migrate hebergement maj

Revision ID: 597e9bc85819
Revises: 3ed73e05151
Create Date: 2013-03-20 11:29:37.049057

"""

# revision identifiers, used by Alembic.
revision = '597e9bc85819'
down_revision = '3ed73e05151'

import sqlalchemy as sa
from alembic import op


obselete_columns = ['heb_maj_tenis',
                    'heb_maj_nautisme',
                    'heb_maj_sky',
                    'heb_maj_rando',
                    'heb_maj_piscine',
                    'heb_maj_peche',
                    'heb_maj_equitation',
                    'heb_maj_velo',
                    'heb_maj_vtt',
                    'heb_maj_ravel',
                    'heb_maj_animal',
                    'heb_maj_fumeur',
                    'heb_maj_tenis_distance',
                    'heb_maj_nautisme_distance',
                    'heb_maj_sky_distance',
                    'heb_maj_rando_distance',
                    'heb_maj_piscine_distance',
                    'heb_maj_peche_distance',
                    'heb_maj_equitation_distance',
                    'heb_maj_velo_distance',
                    'heb_maj_vtt_distance',
                    'heb_maj_ravel_distance',
                    'heb_maj_confort_tv',
                    'heb_maj_confort_feu_ouvert',
                    'heb_maj_confort_lave_vaiselle',
                    'heb_maj_confort_micro_onde',
                    'heb_maj_confort_lave_linge',
                    'heb_maj_confort_seche_linge',
                    'heb_maj_confort_congelateur',
                    'heb_maj_confort_internet',
                    'heb_maj_taxe_sejour',
                    'heb_maj_commerce',
                    'heb_maj_restaurant',
                    'heb_maj_gare',
                    'heb_maj_gare_distance',
                    'heb_maj_restaurant_distance',
                    'heb_maj_commerce_distance']


def upgrade():
    print "... Creates the link metadata update table"
    op.create_table(
        'link_hebergement_metadata_update',
        sa.Column('pk', sa.Integer, nullable=False, primary_key=True,
                  unique=True),
        sa.Column('link_met_fk', sa.Integer(),
                  sa.ForeignKey('link_hebergement_metadata.link_met_pk'),
                  nullable=False),
        sa.Column('metadata_fk', sa.Integer(),
                  sa.ForeignKey('metadata.met_pk'), nullable=False),
        sa.Column('link_met_value', sa.Boolean(), default=False),
        sa.Column('update_date', sa.DateTime(),
                  default=sa.func.current_timestamp()))

    print "... Remove obselete columns in hebergement_maj"
    for column in obselete_columns:
        op.drop_column('hebergement_maj', column)


def downgrade():
    print "... We can't go back!"
