"""Create map_blacklist table
Create map_provider table
Revision ID: 2c5d0d558739
Revises: 33ea541f63ed
Create Date: 2013-03-05 14:32:00.434955

"""

# revision identifiers, used by Alembic.
revision = '2c5d0d558739'
down_revision = '33ea541f63ed'

from alembic import op
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
import sqlalchemy as sa


def upgrade():
    print "... Create TABLE map_provider"
    op.create_table(
        'map_provider',
        Column('provider_pk', String(), primary_key=True, unique=True),
    )

    print "... Create TABLE map_blacklist"
    op.create_table(
        'map_blacklist',
        Column('blacklist_pk', Integer(), primary_key=True, unique=True),
        Column('blacklist_id', String(), nullable=False),
        Column('blacklist_name', String(), nullable=False),
        Column('blacklist_description', String(), nullable=False),
        Column('blacklist_provider_pk', String(), ForeignKey('map_provider.provider_pk'), nullable=False),
        UniqueConstraint('blacklist_id', 'blacklist_provider_pk', name='unique_id_provider'),
    )

def downgrade():
    print "... Drop TABLE map_blacklist"
    op.drop_table('map_blacklist')
    print "... Drop TABLE map_provider"
    op.drop_table('map_provider')
