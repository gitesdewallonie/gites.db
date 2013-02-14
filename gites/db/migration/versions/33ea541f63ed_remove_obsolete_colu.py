# -*- coding: utf-8 -*-

"""Remove obsolete columns

Revision ID: 33ea541f63ed
Revises: 535e4fbc6bed
Create Date: 2013-02-14 10:23:25.723896

"""

# revision identifiers, used by Alembic.
revision = '33ea541f63ed'
down_revision = '535e4fbc6bed'

from alembic import op


columns = ['heb_confort_congelateur',
           'heb_taxe_sejour',
           'heb_commerce',
           'heb_restaurant',
           'heb_gare',
           'heb_confort_projecteur',
           'heb_confort_flipchart',
           'heb_confort_ecran',
           'heb_tenis',
           'heb_nautisme',
           'heb_sky',
           'heb_rando',
           'heb_piscine',
           'heb_peche',
           'heb_equitation',
           'heb_velo',
           'heb_vtt',
           'heb_ravel',
           'heb_animal',
           'heb_fumeur',
           'heb_confort_tv',
           'heb_confort_feu_ouvert',
           'heb_confort_lave_vaiselle',
           'heb_confort_micro_onde',
           'heb_confort_lave_linge',
           'heb_confort_seche_linge',
           'heb_confort_internet',
           'heb_confort_terrasse',
           'heb_confort_jardin',
           'heb_confort_sauna',
           'heb_confort_jacuzzi',
           'heb_seminaire_vert',
           'heb_gid_bebe_tendresse',
           'heb_gid_access_tous',
           'heb_gid_antiallergique',
           'heb_gid_beau_jardin',
           'heb_gid_activite_nature',
           'heb_gid_panda',
           'heb_gid_theme_equestre',
           'heb_gid_peche',
           'heb_gid_patrimoine',
           'heb_gid_eco_gite']

unused_columns = ['heb_chmbre_divers',
                  'heb_chmbre_tarif',
                  'heb_animal_taxe',
                  'heb_tarif_charge']


def upgrade():
    print "... Remove obsolete columns"
    for column in columns:
        op.drop_column('hebergement', column)

    print "... Remove unused columns"
    for column in unused_columns:
        op.drop_column('hebergement', column)


def downgrade():
    print "... You don't want to go back, I promise !"
