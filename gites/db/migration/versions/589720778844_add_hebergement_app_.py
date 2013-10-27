"""Add hebergement_app table

Revision ID: 589720778844
Revises: 56b83e00a285
Create Date: 2013-10-27 19:25:25.648436

"""

# revision identifiers, used by Alembic.
revision = '589720778844'
down_revision = '56b83e00a285'

from alembic import op
from sqlalchemy import select, func, Column, Integer, ForeignKey

from gites.db.content import Hebergement


def upgrade():
    print "... Create TABLE hebergement_app"
    op.create_table(
        'hebergement_app',
        Column('heb_app_pk', Integer, primary_key=True, unique=True,
               nullable=False),
        Column('heb_app_sort_order', Integer),
        Column('heb_app_heb_fk', Integer, ForeignKey('hebergement.heb_pk'))
    )

    print "... Fill hebergement_app with random sort_order values"
    connection = op.get_bind()
    hebTable = Hebergement.__table__

    query = select([hebTable.c.heb_pk],
                   order_by=[func.random()])
    hebs = connection.execute(query).fetchall()
    index = 1
    for heb in hebs:
        pk = heb.heb_pk
        op.execute("INSERT INTO hebergement_app (heb_app_heb_fk, heb_app_sort_order) VALUES (%s, %s)" % (pk, index))
        index += 1


def downgrade():
    print "... Drop TABLE hebergement_app"
    op.drop_table('hebergement_app')
