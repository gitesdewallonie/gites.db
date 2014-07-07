# encoding: utf-8
"""
gites.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from affinitic.db import mapper
from gites.db.content.hebergement.hebergement import Hebergement
from gites.db.content.tarifs_type import TarifsType
from gites.db.mapper import GitesMappedClassBase
import sqlalchemy as sa

TarifsType  # Pyflakes


class Tarifs(GitesMappedClassBase):
    __tablename__ = u'tarifs'
    __table_args__ = (
        sa.ForeignKeyConstraint(['type', 'subtype'],
                                ['tarifs_type.type', 'tarifs_type.subtype']),
    )

    pk = sa.Column('pk', sa.Integer, primary_key=True, unique=True)

    heb_pk = sa.Column('heb_pk', sa.Integer, nullable=False)

    type = sa.Column('type', sa.String, nullable=False)

    subtype = sa.Column('subtype', sa.String, nullable=False)

    date = sa.Column('date', sa.DateTime, nullable=False)

    user = sa.Column('user', sa.String, nullable=False)

    min = sa.Column('min', sa.Float)

    max = sa.Column('max', sa.Float)

    cmt = sa.Column('cmt', sa.String)

    valid = sa.Column('valid', sa.Boolean)

    @mapper.Relation
    def hebergement(cls):
        return sa.orm.relation(
            Hebergement, uselist=False,
            foreign_keys=[Hebergement.heb_pk],
            primaryjoin=cls.heb_pk == Hebergement.heb_pk,
            backref=sa.orm.backref('tarifs', uselist=True,
                                   foreign_keys=[Hebergement.heb_pk],
                                   primaryjoin=Hebergement.heb_pk == cls.heb_pk))

    @classmethod
    def _tarifs_pks(cls, heb_pk):
        query = cls._session().query(
            sa.func.max(cls.pk))
        query = query.filter(cls.heb_pk == heb_pk)
        query = query.filter(cls.type != 'CHARGES')
        query = query.filter(cls.valid == True)
        query = query.group_by(cls.type, cls.subtype)
        pks = query.all()

        query = cls._session().query(
            sa.func.max(cls.pk))
        query = query.filter(cls.heb_pk == heb_pk)
        query = query.filter(cls.type == 'CHARGES')
        query = query.filter(cls.valid == True)
        pks2 = query.all()

        pks_all = pks + pks2
        return pks_all

    @classmethod
    def get_hebergement_tarifs(cls, heb_pk):
        """
        Get all actual valid tarifs for an hebergement
        """
        pks_all = cls._tarifs_pks(heb_pk)

        query = cls._session().query(cls)
        query = query.filter(cls.pk.in_(pks_all))
        return query.all()

    @classmethod
    def get_tarifs_to_confirm(cls):
        """
        Get all heb_pk of tarifs that need to be confirmed
        """
        query = cls._session().query(cls.heb_pk)
        query = query.filter(cls.valid == None)
        query = query.group_by(cls.heb_pk)
        query = query.order_by(cls.heb_pk)
        return query.all()

    @classmethod
    def get_hebergement_tarif_to_confirm(cls, heb_pk, type, subtype=None):
        """
        Get tarifs that need to be confirmed for one specific heb and type
        """
        query = cls._session().query(cls)
        query = query.filter(cls.valid == None)
        query = query.filter(cls.heb_pk == heb_pk)
        query = query.filter(cls.type == type)
        if subtype:
            query = query.filter(cls.subtype == subtype)
        query = query.order_by(cls.pk)
        result = query.first()
        return result

    @classmethod
    def get_hebergement_tarif_to_confirm_with_value(cls, heb_pk, type, subtype, min, max, cmt):
        """
        Get all heb with tarifs that need to be confirmed
        """
        query = cls._session().query(cls)
        query = query.filter(cls.valid == None)
        query = query.filter(cls.heb_pk == heb_pk)
        query = query.filter(cls.type == type)
        query = query.filter(cls.subtype == subtype)
        query = query.filter(cls.min == min)
        query = query.filter(cls.max == max)
        query = query.filter(cls.cmt == cmt)
        query = query.order_by(cls.pk)
        result = query.first()
        return result

    @classmethod
    def exists_tarifs(cls, heb_pk, type, subtype, min, max, cmt):
        """
        Verify if that tarif with same value exists
        """
        pks_all = cls._tarifs_pks(heb_pk)

        query = cls._session().query(cls)
        query = query.filter(cls.pk.in_(pks_all))
        query = query.filter(cls.type == type)
        query = query.filter(cls.subtype == subtype)
        query = query.filter(cls.min == min)
        query = query.filter(cls.max == max)
        query = query.filter(cls.cmt == cmt)
        query = query.filter(cls.valid == True)
        return query.count() > 0

    @classmethod
    def get_last_changes(cls, date, session=None, cgt_not_empty=False):
        """Return the modified lines since the given date"""
        if not session:
            session = cls._session()
        query = session.query(cls).join("hebergement")
        query = query.filter(cls.date >= date)
        query = query.filter(cls.valid == True)
        if cgt_not_empty:
            query = query.filter(Hebergement.heb_code_cgt != u'')
        return query.all()
