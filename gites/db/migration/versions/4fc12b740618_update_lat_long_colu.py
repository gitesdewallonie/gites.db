"""update lat/long column

Revision ID: 4fc12b740618
Revises: 560c5414140c
Create Date: 2013-03-21 11:47:40.050199

"""

# revision identifiers, used by Alembic.
revision = '4fc12b740618'
down_revision = '182e906b370e'

from alembic import op
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, UniqueConstraint


def upgrade():
    print "... Drop TABLE map_external_data"
    op.drop_table('map_external_data')
    print "... Create TABLE map_external_data"
    op.create_table(
        'map_external_data',
        Column('ext_data_pk', Integer(), primary_key=True, unique=True),
        Column('ext_data_id', String(), nullable=False),
        Column('ext_data_title', String(), nullable=False),
        Column('ext_data_type', String()),
        Column('ext_data_date_begin', DateTime()),
        Column('ext_data_date_end', DateTime()),
        Column('ext_data_picture_url', String()),
        Column('ext_data_latitude', Float(), nullable=False),
        Column('ext_data_longitude', Float(), nullable=False),
        Column('ext_data_url', String(), nullable=False),
        Column('ext_data_provider_pk', String(), ForeignKey('map_provider.provider_pk'), nullable=False),
        UniqueConstraint('ext_data_id', 'ext_data_provider_pk', name='ext_data_unique_id_provider'),
    )


def downgrade():
    print "... Drop TABLE map_external_data"
    op.drop_table('map_external_data')
    print "... Create TABLE map_external_data"
    op.create_table(
        'map_external_data',
        Column('ext_data_pk', Integer(), primary_key=True, unique=True),
        Column('ext_data_id', String(), nullable=False),
        Column('ext_data_title', String(), nullable=False),
        Column('ext_data_type', String()),
        Column('ext_data_date_begin', DateTime()),
        Column('ext_data_date_end', DateTime()),
        Column('ext_data_picture_url', String()),
        Column('ext_data_latitude', String(), nullable=False),
        Column('ext_data_longitude', String(), nullable=False),
        Column('ext_data_url', String(), nullable=False),
        Column('ext_data_provider_pk', String(), ForeignKey('map_provider.provider_pk'), nullable=False),
        UniqueConstraint('ext_data_id', 'ext_data_provider_pk', name='ext_data_unique_id_provider'),
    )
