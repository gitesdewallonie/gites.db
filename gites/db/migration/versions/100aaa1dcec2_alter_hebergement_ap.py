"""Alter hebergement_app add columns heb_app_groupement_angle_start and heb_app_groupement_line_length

Revision ID: 100aaa1dcec2
Revises: 1a024e3a77bd
Create Date: 2014-03-31 17:29:42.055158

"""

# revision identifiers, used by Alembic.
revision = '100aaa1dcec2'
down_revision = '1a024e3a77bd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    print "... Adds heb_app_groupement_line_length and heb_app_groupement_angle_start columns"
    op.add_column('hebergement_app',
                  sa.Column('heb_app_groupement_line_length', sa.Integer()))
    op.add_column('hebergement_app',
                  sa.Column('heb_app_groupement_angle_start', sa.Float()))


def downgrade():
    print "... Removes heb_app_groupement_line_length and heb_app_groupement_angle_start columns"
    op.drop_column('hebergement_app', 'heb_app_groupement_line_length')
    op.drop_column('hebergement_app', 'heb_app_groupement_angle_start')
