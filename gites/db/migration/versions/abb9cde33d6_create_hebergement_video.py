"""Create hebergement_video

Revision ID: abb9cde33d6
Revises: 34e3129f84c5
Create Date: 2013-05-13 10:17:39.917681

"""

# revision identifiers, used by Alembic.
revision = 'abb9cde33d6'
down_revision = '34e3129f84c5'

from alembic import op
from sqlalchemy import func, Date, Column, Integer, String, ForeignKey


def upgrade():
    print "... Create TABLE hebergement_video"
    op.create_table(
        'hebergement_video',
        Column('heb_vid_pk', Integer, primary_key=True, unique=True,
               nullable=False),
        Column('heb_vid_url', String()),
        Column('heb_vid_date', Date(), default=func.current_timestamp()),
        Column('heb_vid_heb_fk', Integer, ForeignKey('hebergement.heb_pk'))
    )


def downgrade():
    print "... Drop TABLE hebergement_video"
    op.drop_table('hebergement_video')
