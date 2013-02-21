# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.hebergement.hebergement import Hebergement


class BlockingHistory(GitesMappedClassBase):
    __tablename__ = u'blockinghistory'

    heb_pk = sa.Column('heb_pk', sa.Integer,
                       sa.ForeignKey('hebergement.heb_pk'),
                       primary_key=True)

    block_start = sa.Column('block_start', sa.DateTime,
                            primary_key=True)

    block_end = sa.Column('block_end', sa.DateTime,
                          primary_key=True)

    @classmethod
    def __declare_last__(cls):
        cls.hebergement = sa.orm.relation(Hebergement,
                                          backref='blockinghistory')
