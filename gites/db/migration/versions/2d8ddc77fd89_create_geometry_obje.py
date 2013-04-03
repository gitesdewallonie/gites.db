"""Create geometry objects for infos touristiques

Revision ID: 2d8ddc77fd89
Revises: 40ca197a6ee8
Create Date: 2013-04-04 00:23:06.034121

"""

# revision identifiers, used by Alembic.
revision = '2d8ddc77fd89'
down_revision = '40ca197a6ee8'

from alembic import op
import sqlalchemy as sa
import geoalchemy
import progressbar
from geoalchemy import GeometryExtensionColumn, Geometry
from gites.db.content import InfoTouristique


def upgrade():
    connection = op.get_bind()
    op.add_column('info_touristique', GeometryExtensionColumn('infotour_location',
                                                              Geometry(dimension=2,
                                                                       srid=3447)))
    infotouristique = InfoTouristique.__table__
    query = sa.select([infotouristique.c.infotour_pk,
                       infotouristique.c.infotour_gps_lat,
                       infotouristique.c.infotour_gps_long])
    query.append_whereclause(sa.and_(infotouristique.c.infotour_gps_lat != None,
                                     infotouristique.c.infotour_gps_long != None))
    infos = connection.execute(query).fetchall()
    i = 0
    pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(),
                                            progressbar.Bar()],
                                   maxval=len(infos)).start()
    for info in infos:
        point = 'POINT(%s %s)' % (info.infotour_gps_long, info.infotour_gps_lat)
        point = geoalchemy.base.WKTSpatialElement(point, srid=3447)
        op.execute(
            infotouristique.update().
            where(infotouristique.c.infotour_pk == info.infotour_pk).
            values({'infotour_location': point}))
        pbar.update(i)
        i += 1
    pbar.finish()


def downgrade():
    op.drop_column('info_touristique', 'infotour_location')
