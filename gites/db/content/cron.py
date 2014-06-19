# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class Cron(GitesMappedClassBase):
    __tablename__ = u'cron'

    cron_pk = sa.Column('cron_pk',
                        sa.Integer(),
                        primary_key=True,
                        unique=True)

    cron_script = sa.Column('cron_script',
                            sa.String(),
                            nullable=False)

    cron_start_date = sa.Column('cron_start_date',
                                sa.DateTime(),
                                nullable=False)

    cron_end_date = sa.Column('cron_end_date',
                              sa.DateTime())

    @classmethod
    def getLastFinished(cls, script):
        """
        Get last finished script
        """
        pass
