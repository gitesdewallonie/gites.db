# -*- coding: utf-8 -*-
import sqlalchemy as sa
from affinitic.db import mapper
from gites.db.content.hebergement.hebergement import Hebergement
from gites.db.mapper import GitesMappedClassBase


class HebergementBlockingHistory(GitesMappedClassBase):
    __tablename__ = u'heb_blocking_history'

    heb_blockhistory_id = sa.Column('heb_blockhistory_id', sa.Integer,
                                    sa.Sequence('heb_blockhistory_id_seq'),
                                    primary_key=True)

    heb_blockhistory_blocked_dte = sa.Column('heb_blockhistory_blocked_dte',
                                             sa.Date, nullable=False)

    heb_blockhistory_activated_dte = sa.Column('heb_blockhistory_activated_dte',
                                               sa.Date, nullable=True)

    heb_blockhistory_heb_pk = sa.Column('heb_blockhistory_heb_pk',
                                        sa.Integer,
                                        sa.ForeignKey('hebergement.heb_pk'),
                                        nullable=False)

    heb_blockhistory_days = sa.Column('heb_blockhistory_days', sa.Integer,
                                      nullable=True)

    @mapper.Relation
    def hebergement(cls):
        return sa.orm.relation(Hebergement, backref='hebblockinghistory')
