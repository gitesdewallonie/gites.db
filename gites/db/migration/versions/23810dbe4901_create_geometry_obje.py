"""Create geometry objects for hebergement

Revision ID: 23810dbe4901
Revises: 1969b7af44c6
Create Date: 2013-04-03 16:58:26.030836

"""

# revision identifiers, used by Alembic.
revision = '23810dbe4901'
down_revision = '1969b7af44c6'

from alembic import op
import sqlalchemy as sa
import geoalchemy
from geoalchemy import GeometryExtensionColumn, Geometry
import progressbar
from gites.db.content import Hebergement


def upgrade():
    connection = op.get_bind()
    op.add_column('hebergement', GeometryExtensionColumn('heb_location',
                                                         Geometry(dimension=2,
                                                                  srid=3447)))
    hebergement = Hebergement.__table__
    query = sa.select([hebergement.c.heb_pk,
                       hebergement.c.heb_gps_lat,
                       hebergement.c.heb_gps_long])
    hebergements = connection.execute(query).fetchall()
    i = 0
    pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(),
                                            progressbar.Bar()],
                                   maxval=len(hebergements)).start()
    for heb in hebergements:
        point = 'POINT(%s %s)' % (heb.heb_gps_long, heb.heb_gps_lat)
        point = geoalchemy.base.WKTSpatialElement(point, srid=3447)
        op.execute(
            hebergement.update().
            where(hebergement.c.heb_pk == heb.heb_pk).
            values({'heb_location': point}))
        pbar.update(i)
        i += 1
    pbar.finish()


def downgrade():
    op.drop_column('hebergement', 'heb_location')
