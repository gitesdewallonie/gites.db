"""revert lat long

Revert all latitude longitude informations in table

Revision ID: 515a04ee8cff
Revises: 3ed73e05151
Create Date: 2013-03-20 11:21:15.680143

"""

# revision identifiers, used by Alembic.
revision = '515a04ee8cff'
down_revision = '3541c34a3d30'

from alembic import op
from sqlalchemy import select

import progressbar
from gites.db.content import (Hebergement,
                              InfoTouristique,
                              InfoPratique,
                              MaisonTourisme)


def upgrade():
    """
    Revert latitude longitude from tables:
        hebergement
        info_touristique
        info_pratique
        maison_tourisme
    """
    print "... Inverting gps lat long"
    connection = op.get_bind()
    invertHebergement(connection)
    invertInfoTouristique(connection)
    invertInfoPratique(connection)
    invertMaisonTourisme(connection)


def downgrade():
    """
    Invert too like upgrade() to return to ancient version
    """
    print "... Downgrade inverting gps lat long"
    connection = op.get_bind()
    invertHebergement(connection)
    invertInfoTouristique(connection)
    invertInfoPratique(connection)
    invertMaisonTourisme(connection)


def invertHebergement(connection):
    print "...... Inverting hebergement lat long"
    hebergementTable = Hebergement.__table__
    query = select([hebergementTable.c.heb_pk,
                    hebergementTable.c.heb_gps_lat,
                    hebergementTable.c.heb_gps_long],
                   )
    hebergements = connection.execute(query).fetchall()

    pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(),
                                            progressbar.Bar()],
                                   maxval=len(hebergements)).start()

    i = 0
    for hebergement in hebergements:
        op.execute(hebergementTable.update().
                   where(hebergementTable.c.heb_pk == hebergement.heb_pk).
                   values({'heb_gps_lat': hebergement.heb_gps_long,
                           'heb_gps_long': hebergement.heb_gps_lat}))
        pbar.update(i)
        i += 1
    pbar.finish()


def invertInfoTouristique(connection):
    print "...... Inverting info_touristique lat long"
    infoTourTable = InfoTouristique.__table__
    query = select([infoTourTable.c.infotour_pk,
                    infoTourTable.c.infotour_gps_lat,
                    infoTourTable.c.infotour_gps_long],
                   )
    infoTours = connection.execute(query).fetchall()

    pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(),
                                            progressbar.Bar()],
                                   maxval=len(infoTours)).start()

    i = 0
    for infoTour in infoTours:
        op.execute(infoTourTable.update().
                   where(infoTourTable.c.infotour_pk == infoTour.infotour_pk).
                   values({'infotour_gps_lat': infoTour.infotour_gps_long,
                           'infotour_gps_long': infoTour.infotour_gps_lat}))
        pbar.update(i)
        i += 1
    pbar.finish()


def invertInfoPratique(connection):
    print "...... Inverting info_pratique lat long"
    infoPratTable = InfoPratique.__table__
    query = select([infoPratTable.c.infoprat_pk,
                    infoPratTable.c.infoprat_gps_lat,
                    infoPratTable.c.infoprat_gps_long],
                   )
    infoPrats = connection.execute(query).fetchall()

    pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(),
                                            progressbar.Bar()],
                                   maxval=len(infoPrats)).start()

    i = 0
    for infoPrat in infoPrats:
        op.execute(infoPratTable.update().
                   where(infoPratTable.c.infoprat_pk == infoPrat.infoprat_pk).
                   values({'infoprat_gps_lat': infoPrat.infoprat_gps_long,
                           'infoprat_gps_long': infoPrat.infoprat_gps_lat}))
        pbar.update(i)
        i += 1
    pbar.finish()


def invertMaisonTourisme(connection):
    print "...... Inverting maison_tourisme lat long"
    maisonTourTable = MaisonTourisme.__table__
    query = select([maisonTourTable.c.mais_pk,
                    maisonTourTable.c.mais_gps_lat,
                    maisonTourTable.c.mais_gps_long],
                   )
    maisonTours = connection.execute(query).fetchall()

    pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(),
                                            progressbar.Bar()],
                                   maxval=len(maisonTours)).start()

    i = 0
    for maisonTour in maisonTours:
        op.execute(maisonTourTable.update().
                   where(maisonTourTable.c.mais_pk == maisonTour.mais_pk).
                   values({'mais_gps_lat': maisonTour.mais_gps_long,
                           'mais_gps_long': maisonTour.mais_gps_lat}))
        pbar.update(i)
        i += 1
    pbar.finish()
