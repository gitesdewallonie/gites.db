"""Activity metatadas migration

Revision ID: 1d026c5b13cb
Revises: 117acbc43638
Create Date: 2013-07-11 22:48:21.165448

"""

# revision identifiers, used by Alembic.
revision = '1d026c5b13cb'
down_revision = '117acbc43638'

import os

from alembic import op


def upgrade():
    print "... Modification des metadata des activites "
    op.execute("UPDATE link_hebergement_metadata set link_met_value=False where metadata_fk in (1,2,3,4,5,6,7,8,9,10)")
    nomsFichiers = ['activite_peche.sql', 'activite_ravel.sql', 'activite_velo.sql',
                    'activite_equitation.sql', 'activite_piscine.sql',
                    'activite_sky.sql', 'activite_vtt.sql',
                    'activite_nautisme.sql', 'activite_rando.sql', 'activite_tenis.sql']
    directory = os.getcwd()
    for nomFichier in nomsFichiers:
        fichier = os.path.join(directory, 'devel', 'gites.db', 'gites', 'db', 'migration', 'versions', nomFichier)
        f = open(fichier, 'r')
        for requete in f.readlines():
            op.execute(requete)
        f.close()


def downgrade():
    pass
