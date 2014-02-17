"""Remove unused pro_url and pro_maj_url columns

Revision ID: 42663b5d9f45
Revises: e0a7b7c77f1
Create Date: 2014-02-17 15:25:16.614122

"""

# revision identifiers, used by Alembic.
revision = '42663b5d9f45'
down_revision = 'e0a7b7c77f1'

from alembic import op


def upgrade():
    print "... Drop pro_url and pro_maj_url columns"
    op.drop_column('proprio', 'pro_url')
    op.drop_column('proprio_maj', 'pro_maj_url')


def downgrade():
    print "... Impossible to go back :-)"
