"""Create geometry objects for infos pratiques

Revision ID: 44e362c75192
Revises: 2d8ddc77fd89
Create Date: 2013-04-04 00:34:20.675818

"""

# revision identifiers, used by Alembic.
revision = '44e362c75192'
down_revision = '2d8ddc77fd89'

from alembic import op
import sqlalchemy as sa
import geoalchemy
import progressbar
from geoalchemy import GeometryExtensionColumn, Geometry
from gites.db.content import InfoPratique


def upgrade():
    connection = op.get_bind()
    op.add_column('info_pratique', GeometryExtensionColumn('infoprat_location',
                                                           Geometry(dimension=2,
                                                                    srid=3447)))
    infopratique = InfoPratique.__table__
    query = sa.select([infopratique.c.infoprat_pk,
                       infopratique.c.infoprat_gps_lat,
                       infopratique.c.infoprat_gps_long])
    query.append_whereclause(sa.and_(infopratique.c.infoprat_gps_lat != None,
                                     infopratique.c.infoprat_gps_long != None))
    infos = connection.execute(query).fetchall()
    i = 0
    pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(),
                                            progressbar.Bar()],
                                   maxval=len(infos)).start()
    for info in infos:
        point = 'POINT(%s %s)' % (info.infoprat_gps_long, info.infoprat_gps_lat)
        point = geoalchemy.base.WKTSpatialElement(point, srid=3447)
        op.execute(
            infopratique.update().
            where(infopratique.c.infoprat_pk == info.infoprat_pk).
            values({'infoprat_location': point}))
        pbar.update(i)
        i += 1
    pbar.finish()


def downgrade():
    op.drop_column('info_pratique', 'infoprat_location')
