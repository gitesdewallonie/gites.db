"""Insert into map_provider table

Revision ID: 40bd317d027c
Revises: 4e47ca1dde9f
Create Date: 2013-03-20 14:22:29.488681

"""

# revision identifiers, used by Alembic.
revision = '40bd317d027c'
down_revision = '4e47ca1dde9f'

from alembic import op
from sqlalchemy import String
from sqlalchemy.sql import table, column

def upgrade():
    print "... Insert into map_provider:"
    print "... resto.be / quefaire.be / google"
    map_provider_table = table('map_provider',
        column('provider_pk', String()))
    op.bulk_insert(map_provider_table,
                   [
                        {'provider_pk': 'resto.be'},
                        {'provider_pk': 'quefaire.be'},
                        {'provider_pk': 'google'},
                   ]
                  )

def downgrade():
    print "... Delete from map_provider"
    op.execute('delete from map_provider')
