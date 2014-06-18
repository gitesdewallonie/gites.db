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
    print "... Create TABLE pivot_origin"
    op.create_table(
        'pivot_origin',
        Column('origin_pk', String(), primary_key=True, unique=True),
    )

    print "... Insert into pivot_origin:"
    print "... PIVOT, GDW"
    pivot_origin_table = table('pivot_origin',
                               column('origin_pk', String()))
    op.bulk_insert(pivot_origin_table,
                   [
                       {'origin_pk': 'GDW'},
                       {'origin_pk': 'PIVOT'},
                   ])

    print "... Create TABLE pivot_notification"
    op.create_table(
        'pivot_notification',
        Column('notf_pk', Integer(), primary_key=True, unique=True),
        Column('notf_origin', String(), ForeignKey('pivot_origin.origin_pk'), nullable=False),
        Column('notf_table', String(), nullable=False),
        Column('notf_old_value', String(), nullable=False),
        Column('notf_new_value', String(), nullable=False),
        Column('notf_date', DateTime(), nullable=False),
        Column('notf_treated', Boolean()),
        Column('notf_applied', Boolean()),
        Column('notf_cmt', String()),
        Column('notf_user', String()),
    )


def downgrade():
    print "... Drop TABLE pivot_notification"
    op.drop_table('pivot_notification')
    print "... Drop TABLE pivot_origin"
    op.drop_table('pivot_origin')
