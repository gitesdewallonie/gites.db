# -*- coding: utf-8 -*-
"""add heb_groupement_pk

Revision ID: 15a763628bf5
Revises: 44e362c75192
Create Date: 2013-04-08 13:06:47.948666

"""

# revision identifiers, used by Alembic.
revision = '15a763628bf5'
down_revision = '44e362c75192'

from alembic import op
from geoalchemy.postgis import pg_functions
import sqlalchemy as sa

from gites.db.content import Hebergement

GROUPING_DISTANCE_METERS = 500


def upgrade():
    addColumn()
    fillColumn()


def downgrade():
    print "... Removing column heb_groupement_pk"
    op.drop_column('hebergement', 'heb_groupement_pk')


def addColumn():
    print "... Creating column heb_groupement_pk"
    op.add_column('hebergement', sa.Column('heb_groupement_pk', sa.Integer()))


def fillColumn():
    print "... Filling column heb_groupement_pk"
    connection = op.get_bind()
    hebTable = Hebergement.__table__

    # Exemple d'hebs groupes : heb_pk = 130
    query = sa.select([hebTable.c.heb_pk,
                       hebTable.c.heb_location.label('heb_location'),
                       hebTable.c.heb_pro_fk,
                       hebTable.c.heb_cgt_cap_max,
                       hebTable.c.heb_nom],
                      order_by=[hebTable.c.heb_pro_fk, hebTable.c.heb_cgt_cap_max.desc()])
    hebs = connection.execute(query).fetchall()

    groupementPk = 1
    groupedHebsPk = []

    for heb in hebs:
        if heb.heb_pk not in groupedHebsPk:

            groupedHebs = getGroupedHebs(heb, groupedHebsPk)
            if groupedHebs:
                #add this one to the list to update
                groupedHebs.append(heb)

                print "Setting groupement_pk %s to %s for proprio %s" % (
                    groupementPk,
                    [str(obj.heb_pk) + ' ' + obj.heb_nom for obj in groupedHebs],
                    heb.heb_pro_fk)

                setGroupementPk(groupedHebs, groupementPk)
                groupedHebsPk.extend([obj.heb_pk for obj in groupedHebs])
                groupementPk += 1


def getGroupedHebs(heb, groupedHebsPk):
    """
    get all hebs near heb from the same proprio
    Exclude groupedHebsPk (already grouped)
    """
    connection = op.get_bind()
    hebTable = Hebergement.__table__

    query = sa.select([hebTable.c.heb_pk,
                       hebTable.c.heb_nom],
                      sa.and_(pg_functions.distance_sphere(hebTable.c.heb_location, heb.heb_location) < GROUPING_DISTANCE_METERS,
                              hebTable.c.heb_pro_fk == heb.heb_pro_fk,
                              hebTable.c.heb_pk != heb.heb_pk,
                              sa.not_(hebTable.c.heb_pk.in_(groupedHebsPk))))
    return connection.execute(query).fetchall()


def setGroupementPk(hebs, groupementPk):
    """
    fill heb_groupement_pk for hebs by heb_pk
    """
    hebTable = Hebergement.__table__
    op.execute(
        hebTable.update().
        where(hebTable.c.heb_pk.in_([heb.heb_pk for heb in hebs])).
        values({'heb_groupement_pk': groupementPk}))
