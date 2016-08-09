"""create table localite

Revision ID: 377e48618f00
Revises: 456da77fc955
Create Date: 2016-08-09 00:48:56.424086

"""

# revision identifiers, used by Alembic.
revision = '377e48618f00'
down_revision = '456da77fc955'


from alembic import op
from sqlalchemy import Column, Integer, String, ForeignKey


def upgrade():
    print "... Create TABLE localite"
    op.create_table(
        'localite',
        Column('localite_pk', Integer, primary_key=True, unique=True,
               nullable=False),
        Column('localite_nom', String()),
        Column('localite_cp', String()),
        Column('localite_ins', String()),
        Column('localite_commune_fk', Integer, ForeignKey('commune.com_pk'))
    )


def downgrade():
    print "... Drop TABLE localite"
    op.drop_table('localite')