# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class ReservationProprio(GitesMappedClassBase):
    __tablename__ = u'reservation_proprio'

    res_id = sa.Column('res_id', sa.Integer, primary_key=True)

    res_date_cre = sa.Column('res_date_cre', sa.DateTime)

    res_date = sa.Column('res_date', sa.DateTime, nullable=False)

    res_type = sa.Column('res_type', sa.String(20), nullable=False)

    heb_fk = sa.Column('heb_fk', sa.Integer,
                       sa.ForeignKey('hebergement.heb_pk'),
                       nullable=False)

    pro_fk = sa.Column('pro_fk', sa.Integer,
                       sa.ForeignKey('proprio.pro_pk'))
