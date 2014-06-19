"""create cron table

Revision ID: c68797cf085
Revises: 24a246dee1d1
Create Date: 2014-06-18 15:41:51.417946

"""

# revision identifiers, used by Alembic.
revision = 'c68797cf085'
down_revision = '24a246dee1d1'

from alembic import op
from sqlalchemy import Column, Integer, String, DateTime


def upgrade():
    print "... Create TABLE cron"
    op.create_table(
        'cron',
        Column('cron_pk', Integer(), primary_key=True, unique=True),
        Column('cron_script', String(), nullable=False),
        Column('cron_start_date', DateTime(), nullable=False),
        Column('cron_end_date', DateTime()),
    )


def downgrade():
    print "... Drop TABLE cron"
    op.drop_table('cron')
