"""Create map_external_data table

Revision ID: 4e47ca1dde9f
Revises: 515a04ee8cff
Create Date: 2013-03-20 13:51:26.566105

"""

# revision identifiers, used by Alembic.
revision = '4e47ca1dde9f'
down_revision = '515a04ee8cff'

from alembic import op
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint


def upgrade():
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


def downgrade():
    print "... Drop TABLE map_external_data"
    op.drop_table('map_external_data')
