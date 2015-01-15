"""empty message

Revision ID: 1de3a443694f
Revises: 291ea26db693
Create Date: 2015-01-15 18:34:59.219932

"""

# revision identifiers, used by Alembic.
revision = '1de3a443694f'
down_revision = '291ea26db693'

from alembic import op


def upgrade():
    print '... Update the tarifs view'
    op.execute("""
        CREATE OR REPLACE VIEW tarifs_view AS
        SELECT * from tarifs
        where pk in (select max(pk)
                     from tarifs
                     where valid = True
                       and type != 'CHARGES'
                     group by "type", subtype, heb_pk)
        union all
        SELECT * from tarifs
        where pk in (select max(pk)
                     from tarifs
                     where valid = True
                       and type = 'CHARGES'
                     group by heb_pk)
        """)


def downgrade():
    raise ValueError('Impossible to downgrade this revision')
