"""Migrate metadata

Revision ID: 535e4fbc6bed
Revises: None
Create Date: 2013-02-13 16:51:40.867726

"""

from sqlalchemy import select, MetaData
from gites.db.tables import getHebergementTable


metadatas = [
]


# revision identifiers, used by Alembic.
revision = '535e4fbc6bed'
down_revision = None

from alembic import op


def fakeHasTable(param):
    return False


def upgrade():
    print "... Create all metadata records"
    for metadata in metadatas:
        op.execute("""
            INSERT INTO metadata (met_id, met_titre_fr, met_titre_en,
                                  met_titre_nl, met_titre_it, met_titre_de,
                                  met_filterable)
                   VALUES ('%s', '%s', '%s', '%s', '%s', '%s', %s);
            """ % (metadata['id'], metadata['titre_fr'], metadata['titre_nl'],
                   metadata['titre_en'], metadata['titre_it'],
                   metadata['titre_de'], metadata['filterable']))

    print "... Migrate existing metadata data"
    connection = op.get_bind()
    adHocMetadata = MetaData()
    adHocMetadata.bind = connection.engine
    adHocMetadata.bind.has_table = fakeHasTable

    hebergementTable = getHebergementTable(adHocMetadata)

    query = select([hebergementTable.c.heb_pk],
                   order_by=hebergementTable.c.heb_pk)
    result = connection.execute(query).fetchall()
    hebsPks = [r.heb_pk for r in result]

    for pk in hebsPks:
        pass


def downgrade():
    print "... Impossible to downgrade, too hard ;-)"
