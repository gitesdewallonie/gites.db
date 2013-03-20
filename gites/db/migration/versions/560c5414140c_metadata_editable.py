"""empty message

Revision ID: 560c5414140c
Revises: 40bd317d027c
Create Date: 2013-03-20 16:30:32.330027

"""

# revision identifiers, used by Alembic.
revision = '560c5414140c'
down_revision = '40bd317d027c'

from alembic import op


editable_columns = (
    'heb_confort_congelateur',
    'heb_confort_ecran',
    'heb_confort_feu_ouvert',
    'heb_confort_flipchart',
    'heb_confort_internet',
    'heb_confort_jacuzzi',
    'heb_confort_projecteur',
    'heb_equitation',
    'heb_animal',
    'heb_tabhot_gourmand',
    'heb_tabhot_gastronomique',
    'heb_tabhot_repas_familial',
    'heb_fumeur',
    'heb_confort_micro_onde',
    'heb_confort_sauna',
    'heb_confort_seche_linge',
    'heb_confort_terrasse',
    'heb_confort_tv',
    'heb_piscine',
    'heb_peche',
    'heb_rando',
    'heb_ravel',
    'heb_sky',
    'heb_nautisme',
    'heb_tenis',
    'heb_vtt',
    'heb_velo',
    'heb_confort_jardin',
    'heb_confort_lave_linge',
    'heb_confort_lave_vaiselle')


def upgrade():
    print "... Updates the editable parameter for metadata"
    op.execute('UPDATE metadata set met_editable = false')
    query = "UPDATE metadata set met_editable = true where met_id = '%s'"
    for column in editable_columns:
        op.execute(query % column)


def downgrade():
    print "... Reverts the editable parameter for metadata"
    op.execute('UPDATE metadata set met_editable = false')
