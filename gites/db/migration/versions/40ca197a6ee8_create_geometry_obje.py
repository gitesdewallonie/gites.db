"""Create geometry objects for maisontourisme

Revision ID: 40ca197a6ee8
Revises: 23810dbe4901
Create Date: 2013-04-04 00:12:55.488276

"""

# revision identifiers, used by Alembic.
revision = '40ca197a6ee8'
down_revision = '23810dbe4901'

from alembic import op
import sqlalchemy as sa
from geoalchemy import GeometryExtensionColumn, Geometry
import progressbar
import geoalchemy
from gites.db.content import MaisonTourisme


def upgrade():
    connection = op.get_bind()
    op.add_column('maison_tourisme', GeometryExtensionColumn('mais_location',
                                                             Geometry(dimension=2,
                                                                      srid=3447)))

    maison = MaisonTourisme.__table__
    query = sa.select([maison.c.mais_pk,
                       maison.c.mais_gps_lat,
                       maison.c.mais_gps_long])
    maisons = connection.execute(query).fetchall()
    i = 0
    pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(),
                                            progressbar.Bar()],
                                   maxval=len(maisons)).start()
    for mais in maisons:
        point = 'POINT(%s %s)' % (mais.mais_gps_long, mais.mais_gps_lat)
        point = geoalchemy.base.WKTSpatialElement(point, srid=3447)
        op.execute(
            maison.update().
            where(maison.c.mais_pk == mais.mais_pk).
            values({'mais_location': point}))
        pbar.update(i)
        i += 1
    pbar.finish()


def downgrade():
    op.drop_column('maison_tourisme', 'mais_location')
