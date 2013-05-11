# -*- coding: utf-8 -*-
import sqlalchemy as sa
from zope.interface import implements
from affinitic.db import mapper
from gites.db.interfaces import IProprioMaj
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.proprio.civilite import Civilite
from gites.db.content.commune import Commune


class ProprioMaj(GitesMappedClassBase):
    implements(IProprioMaj)
    __tablename__ = u'proprio_maj'

    pro_maj_pk = sa.Column('pro_maj_pk', sa.Integer, primary_key=True)

    pro_maj_propk = sa.Column('pro_maj_propk', sa.Integer())

    pro_maj_nom1 = sa.Column('pro_maj_nom1', sa.String())

    pro_maj_nom2 = sa.Column('pro_maj_nom2', sa.String())

    pro_maj_prenom1 = sa.Column('pro_maj_prenom1', sa.String())

    pro_maj_prenom2 = sa.Column('pro_maj_prenom2', sa.String())

    pro_maj_societe = sa.Column('pro_maj_societe', sa.String())

    pro_maj_adresse = sa.Column('pro_maj_adresse', sa.String())

    pro_maj_langue = sa.Column('pro_maj_langue', sa.String())

    pro_maj_tel_priv = sa.Column('pro_maj_tel_priv', sa.String())

    pro_maj_fax_priv = sa.Column('pro_maj_fax_priv', sa.String())

    pro_maj_gsm1 = sa.Column('pro_maj_gsm1', sa.String())

    pro_maj_email = sa.Column('pro_maj_email', sa.String())

    pro_maj_url = sa.Column('pro_maj_url', sa.String())

    pro_maj_date_crea = sa.Column('pro_maj_date_crea', sa.Date(),
                                  default=sa.func.current_timestamp())

    pro_maj_civ_fk = sa.Column('pro_maj_civ_fk', sa.Integer,
                               sa.ForeignKey('civilite.civ_pk'))

    pro_maj_com_fk = sa.Column('pro_maj_com_fk', sa.Integer,
                               sa.ForeignKey('commune.com_pk'))

    @mapper.Relation
    def civilite(cls):
        return sa.orm.relation(Civilite)

    @mapper.Relation
    def commune(cls):
        return sa.orm.relation(Commune)
