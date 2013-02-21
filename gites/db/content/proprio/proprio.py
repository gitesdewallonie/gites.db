# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy.orm import relation
from affinitic.caching import cache
from gites.db import session
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.proprio.civilite import Civilite
from gites.db.content.commune import Commune


class Proprio(GitesMappedClassBase):
    __tablename__ = u'proprio'

    pro_pk = sqlalchemy.Column('pro_pk', sqlalchemy.Integer, primary_key=True)

    pro_nom1 = sqlalchemy.Column('pro_nom1', sqlalchemy.String())

    pro_nom2 = sqlalchemy.Column('pro_nom2', sqlalchemy.String())

    pro_pernom1 = sqlalchemy.Column('pro_prenom1', sqlalchemy.String())

    pro_langue = sqlalchemy.Column('pro_langue', sqlalchemy.String())

    pro_tel_priv = sqlalchemy.Column('pro_tel_priv', sqlalchemy.String())

    pro_fax_priv = sqlalchemy.Column('pro_fax_priv', sqlalchemy.String())

    pro_gsm1 = sqlalchemy.Column('pro_gsm1', sqlalchemy.String())

    pro_email = sqlalchemy.Column('pro_email', sqlalchemy.String())

    pro_url = sqlalchemy.Column('pro_url', sqlalchemy.String())

    pro_etat = sqlalchemy.Column('pro_etat', sqlalchemy.Boolean())

    pro_maj_info_etat = sqlalchemy.Column('pro_maj_info_etat',
                                          sqlalchemy.String())

    pro_civ_fk = sqlalchemy.Column('pro_civ_fk', sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('civilite.civ_pk'))

    pro_com_fk = sqlalchemy.Column('pro_com_fk', sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('commune.com_pk'))

    pro_reactivation_hash = sqlalchemy.Column('pro_reactivation_hash',
                                              sqlalchemy.String())

    @classmethod
    @cache(lambda x, y, z: z, dependencies=['pgsql'])
    def get(cls, heb_pk):
        sess = session()
        return sess.query(cls).get(heb_pk)

    @classmethod
    def __declare_last__(cls):
        cls.civilite = relation(Civilite)

        cls.commune = relation(Commune)
