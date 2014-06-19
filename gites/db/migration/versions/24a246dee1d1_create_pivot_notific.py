"""create pivot notification table

Revision ID: 24a246dee1d1
Revises: 100aaa1dcec2
Create Date: 2014-06-18 14:43:31.414658

"""

# revision identifiers, used by Alembic.
revision = '24a246dee1d1'
down_revision = '100aaa1dcec2'

from alembic import op
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.sql import table, column


def upgrade():
    print "... Create TABLE notification_origin"
    op.create_table(
        'notification_origin',
        Column('pk', String, primary_key=True, unique=True),
    )

    print "... Insert into notification_origin:"
    print "... PIVOT, GDW"
    pivot_origin_table = table('notification_origin', column('pk', String))
    op.bulk_insert(pivot_origin_table, [{'pk': 'GDW'}, {'pk': 'PIVOT'}])

    print "... Create TABLE notification"
    op.create_table(
        'notification',
        Column('pk', Integer, primary_key=True, unique=True),
        Column('origin', String, ForeignKey('notification_origin.pk'),
               nullable=False),
        Column('table', String, nullable=False),
        Column('column', String, nullable=False),
        Column('table_pk', String, nullable=False),
        Column('old_value', String),
        Column('new_value', String),
        Column('date', DateTime, nullable=False),
        Column('treated', Boolean),
        Column('cmt', String),
        Column('user', String),
    )


def downgrade():
    print "... Drop TABLE notification"
    op.drop_table('notification')
    print "... Drop TABLE notification_origin"
    op.drop_table('notification_origin')
