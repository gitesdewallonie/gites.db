# -*- coding: utf-8 -*-
import sqlalchemy
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.tablehote import TableHote


class TypeTableHoteOfHebergement(GitesMappedClassBase):
    __tablename__ = u'heb_tab_hote'

    hebhot_maj_heb_fk = sqlalchemy.Column('hebhot_heb_fk',
                                          sqlalchemy.Integer,
                                          sqlalchemy.ForeignKey('hebergement.heb_pk'),
                                          primary_key=True)

    hebhot_maj_tabho_fk = sqlalchemy.Column('hebhot_tabho_fk',
                                            sqlalchemy.Integer,
                                            sqlalchemy.ForeignKey('table_hote.tabho_pk'),
                                            primary_key=True)
