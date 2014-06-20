# -*- coding: utf-8 -*-
import sqlalchemy as sa
from affinitic.db import mapper
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.pivot.origin import NotificationOrigin


class Notification(GitesMappedClassBase):
    __tablename__ = u'notification'

    pk = sa.Column('pk', sa.Integer, primary_key=True, unique=True)

    origin = sa.Column('origin', sa.String,
                       sa.ForeignKey('notification_origin.pk'),
                       nullable=False)

    table = sa.Column('table', sa.String, nullable=False)

    column = sa.Column('column', sa.String, nullable=False)

    table_pk = sa.Column('table_pk', sa.String, nullable=False)

    old_value = sa.Column('old_value', sa.String)

    new_value = sa.Column('new_value', sa.String)

    date = sa.Column('date', sa.DateTime, nullable=False)

    treated = sa.Column('treated', sa.Boolean)

    cmt = sa.Column('cmt', sa.String)

    user = sa.Column('user', sa.String)

    def get_untreated_notifications(self, origin):
        """
        Return untreated or unapplied notifications depeding on the origin
        """
        pass

    def get_notifications(self, origin):
        """
        Return all notifications depending on the origin
        """
        pass

    def treat_notification(self, pk, cmt, user):
        """
        Treat notification
        """
        pass

    @mapper.Relation
    def notification_origin(cls):
        return sa.orm.relation(NotificationOrigin, lazy=True)
