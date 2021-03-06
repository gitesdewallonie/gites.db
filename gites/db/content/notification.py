# -*- coding: utf-8 -*-
import sqlalchemy as sa
from affinitic.db import mapper
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.notification_origin import NotificationOrigin


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

    @classmethod
    def get_untreated_notifications(cls, origin):
        """
        Return untreated or unapplied notifications depeding on the origin
        """
        query = cls._session().query(cls)
        query = query.filter(cls.origin == origin)
        query = query.filter(cls.treated == None)
        query = query.order_by(cls.table_pk, cls.date)
        return query.all()

    @classmethod
    def get_treated_notifications(cls, origin):
        """
        Return all notifications depending on the origin
        """
        query = cls._session().query(cls)
        query = query.filter(cls.origin == origin)
        query = query.filter(cls.treated != None)
        query = query.order_by(cls.table_pk, cls.date)
        return query.all()

    def treat(self, treated, user):
        """
        Treat notification
        """
        setattr(self, 'treated', treated)
        setattr(self, 'user', user)
        self.save()

    @mapper.Relation
    def notification_origin(cls):
        return sa.orm.relation(NotificationOrigin, lazy=True)
