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
        query = query.filter(cls.valid == True)
        query = query.filter(cls.type != 'CHARGES')
        query = query.group_by(cls.type, cls.subtype)
        pks = query.all()

        query = cls._session().query(
            sa.func.max(cls.pk))
        query = query.filter(cls.heb_pk == heb_pk)
        query = query.filter(cls.valid == True)
        query = query.filter(cls.type == 'CHARGES')
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
        return query.all() and True or False
