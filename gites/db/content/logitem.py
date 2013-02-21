# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import sqlalchemy
from z3c.sqlalchemy.mapper import MappedClassBase
from gites.db import DeclarativeBase


class LogItem(DeclarativeBase, MappedClassBase):
    __tablename__ = u'log'

    log_pk = sqlalchemy.Column('log_pk', sqlalchemy.Integer(),
                               sqlalchemy.Sequence('log_log_pk_seq'),
                               primary_key=True)

    log_date = sqlalchemy.Column('log_date', sqlalchemy.DateTime(), nullable=False)

    log_path = sqlalchemy.Column('log_path', sqlalchemy.String(), nullable=False)

    log_hebid = sqlalchemy.Column('log_hebid', sqlalchemy.String(), nullable=False)

    log_hebpk = sqlalchemy.Column('log_hebpk', sqlalchemy.Integer(),
                                  sqlalchemy.ForeignKey('hebergement.heb_pk'))

    log_host = sqlalchemy.Column('log_host', sqlalchemy.String())

    log_agent = sqlalchemy.Column('log_agent', sqlalchemy.String())

    log_website = sqlalchemy.Column('log_website', sqlalchemy.String())
