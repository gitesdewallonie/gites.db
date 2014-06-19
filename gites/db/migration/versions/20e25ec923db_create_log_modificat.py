"""create log_modification table

Revision ID: 20e25ec923db
Revises: c68797cf085
Create Date: 2014-06-19 11:36:09.071369

"""

# revision identifiers, used by Alembic.
revision = '20e25ec923db'
down_revision = 'c68797cf085'

from alembic import op
import sqlalchemy as sa


def upgrade():
    print "... Create table log_modification"
    op.create_table(
        'log_modification',
        sa.Column('pk', sa.Integer, primary_key=True, unique=True),
        sa.Column('date', sa.DateTime, nullable=False),
        sa.Column('user', sa.String),
        sa.Column('table', sa.String, nullable=False),
        sa.Column('column', sa.String, nullable=False),
        sa.Column('table_pk', sa.String, nullable=False),
        sa.Column('old_value', sa.String),
        sa.Column('new_value', sa.String),
    )


def downgrade():
    print "... Drop table log_modification"
    op.drop_table('log_modification')
