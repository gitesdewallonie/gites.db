"""Create geometry objects for map_external_data

Revision ID: 212bf3d91b4a
Revises: 56db15e1c19c
Create Date: 2013-04-09 16:11:53.278722

"""

# revision identifiers, used by Alembic.
revision = '212bf3d91b4a'
down_revision = '56db15e1c19c'

from alembic import op
import sqlalchemy as sa
import geoalchemy
from geoalchemy import GeometryExtensionColumn, Geometry
import progressbar
from gites.db.content import MapExternalData


def upgrade():
    connection = op.get_bind()
    op.add_column('map_external_data', GeometryExtensionColumn('ext_data_location',
                                                               Geometry(dimension=2,
                                                                        srid=3447)))
    mapExternalData = MapExternalData.__table__
    query = sa.select([mapExternalData.c.ext_data_pk,
                       mapExternalData.c.ext_data_latitude,
                       mapExternalData.c.ext_data_longitude])
    query.append_whereclause(sa.and_(mapExternalData.c.ext_data_latitude != None,
                                     mapExternalData.c.ext_data_longitude != None))
    mapExternalDatas = connection.execute(query).fetchall()
    i = 0
    if len(mapExternalDatas) == 0:
        return
    pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(),
                                            progressbar.Bar()],
                                   maxval=len(mapExternalDatas)).start()
    for extData in mapExternalDatas:
        point = 'POINT(%s %s)' % (extData.ext_data_longitude, extData.ext_data_latitude)
        point = geoalchemy.base.WKTSpatialElement(point, srid=3447)
        op.execute(
            mapExternalData.update().
            where(mapExternalData.c.ext_data_pk == extData.ext_data_pk).
            values({'ext_data_location': point}))
        pbar.update(i)
        i += 1
    pbar.finish()


def downgrade():
    op.drop_column('map_external_data', 'ext_data_location')
