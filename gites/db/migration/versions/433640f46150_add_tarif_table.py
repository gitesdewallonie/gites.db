"""add tarif table

Revision ID: 433640f46150
Revises: 20e25ec923db
Create Date: 2014-06-19 16:57:40.069477

"""

# revision identifiers, used by Alembic.
revision = '433640f46150'
down_revision = '20e25ec923db'

from alembic import op
import sqlalchemy as sa


def upgrade():
    print "... Create table tarifs_type"
    op.create_table(
        'tarifs_type',
        sa.Column('type', sa.String, primary_key=True, nullable=False),
        sa.Column('subtype', sa.String, primary_key=True, nullable=False),
    )
    tarifs_type_table = sa.sql.table('tarifs_type',
                                     sa.sql.column('type', sa.String),
                                     sa.sql.column('subtype', sa.String))

    values = [
        {'type': 'LOW_SEASON', 'subtype': 'WEEK'},
        {'type': 'LOW_SEASON', 'subtype': 'WEEKEND'},
        {'type': 'MEDIUM_SEASON', 'subtype': 'WEEK'},
        {'type': 'MEDIUM_SEASON', 'subtype': 'WEEKEND'},
        {'type': 'HIGH_SEASON', 'subtype': 'WEEK'},
        {'type': 'HIGH_SEASON', 'subtype': 'WEEKEND'},
        {'type': 'FEAST_WEEKEND', 'subtype': '3_NIGHTS'},
        {'type': 'FEAST_WEEKEND', 'subtype': '4_NIGHTS'},
        {'type': 'OTHER', 'subtype': 'END_OF_YEAR'},
        {'type': 'OTHER', 'subtype': 'GUARANTEE'},
        {'type': 'OTHER', 'subtype': 'OTHER'},
        {'type': 'OTHER', 'subtype': 'SOJOURN_TAX'},
        {'type': 'CHARGES', 'subtype': 'ACCORDING_TO_CONSUMPTION'},
        {'type': 'CHARGES', 'subtype': 'INCLUDED'},
        {'type': 'CHARGES', 'subtype': 'INCLUSIVE'},
        {'type': 'ROOM', 'subtype': '1_PERSON'},
        {'type': 'ROOM', 'subtype': '2_PERSONS'},
        {'type': 'ROOM', 'subtype': 'PERSON_SUP'},
        {'type': 'OTHER', 'subtype': 'WITHOUT_BREAKFAST'},
        {'type': 'OTHER', 'subtype': 'TABLE_HOTES'},
        # {'type': 'CLEANING', 'subtype': 'INCLUDED'},
        # {'type': 'CLEANING', 'subtype': 'INCLUSIVE'},
        # {'type': 'CLEANING', 'subtype': 'BY_TENANT_OR'},
        # {'type': 'LOW_SEASON', 'subtype': 'MID_WEEK'},
        # {'type': 'MEDIUM_SEASON', 'subtype': 'MID_WEEK'},
        # {'type': 'HIGH_SEASON', 'subtype': 'MID_WEEK'},
        # {'type': 'FEAST_WEEKEND', 'subtype': 'NORMAL'},
    ]

    op.bulk_insert(tarifs_type_table, values)

    print "... Create table tarifs"
    op.create_table(
        'tarifs',
        sa.Column('pk', sa.Integer, primary_key=True, unique=True),
        sa.Column('heb_pk', sa.Integer,
                  sa.ForeignKey('hebergement.heb_pk'), nullable=False),
        sa.Column('type', sa.String, nullable=False),
        sa.Column('subtype', sa.String, nullable=False),
        sa.Column('date', sa.DateTime, nullable=False),
        sa.Column('user', sa.String, nullable=False),
        sa.Column('min', sa.Float),
        sa.Column('max', sa.Float),
        sa.Column('cmt', sa.String),
        sa.Column('valid', sa.Boolean),
        sa.ForeignKeyConstraint(['type', 'subtype'],
                                ['tarifs_type.type', 'tarifs_type.subtype'])
    )


def downgrade():
    print "... Drop table tarifs"
    op.drop_table('tarifs')
    print "... Drop table tarifs_type"
    op.drop_table('tarifs_type')
