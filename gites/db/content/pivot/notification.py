# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class PivotNotification(GitesMappedClassBase):
    __tablename__ = u'pivot_notification'

    notf_pk = sa.Column('notf_pk',
                        sa.Integer(),
                        primary_key=True,
                        unique=True)

    notf_origin = sa.Column('notf_origin',
                            sa.String(),
                            sa.ForeignKey('pivot_origin.origin_pk'),
                            nullable=False)

    notf_table = sa.Column('notf_table',
                           sa.String(),
                           nullable=False)

    notf_old_value = sa.Column('notf_old_value',
                               sa.String(),
                               nullable=False)

    notf_new_value = sa.Column('notf_new_value',
                               sa.String(),
                               nullable=False)

    notf_date = sa.Column('notf_date',
                          sa.DateTime(),
                          nullable=False)

    notf_treated = sa.Column('notf_treated',
                             sa.Boolean())

    notf_applied = sa.Column('notf_applied',
                             sa.Boolean())

    notf_cmt = sa.Column('notf_cmt',
                         sa.String())

    notf_user = sa.Column('notf_user',
                          sa.String())

    blacklist_pk = sa.Column('blacklist_pk',
                             sa.Integer(),
                             primary_key=True,
                             unique=True)

    def getUntreatedNotifications(self, origin):
        """
        Return untreated or unapplied notifications depeding on the origin
        """
        pass

    def getNotifications(self, origin):
        """
        Return all notifications depending on the origin
        """
        pass

    def treatNotification(self, pk, cmt, user):
        """
        Treat notification
        """
        pass
