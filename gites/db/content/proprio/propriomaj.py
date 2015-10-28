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
    """
    Table contenant toutes les informations mise à jour relatives à un propriétaire
    """

    __tablename__ = u'proprio_maj'

    pro_maj_pk = sa.Column('pro_maj_pk', sa.Integer,
                           primary_key=True,
                           doc=u"Numéro d'identifiant unique")

    pro_maj_propk = sa.Column('pro_maj_propk', sa.Integer(),
                              doc=u"Numéro d'identifiant unique vers la table proprio")

    pro_maj_nom1 = sa.Column('pro_maj_nom1', sa.String(),
                             doc=u"Nom 1 du propriétaire")

    pro_maj_nom2 = sa.Column('pro_maj_nom2', sa.String(),
                             doc=u"Nom 2 du propriétaire")

    pro_maj_prenom1 = sa.Column('pro_maj_prenom1', sa.String(),
                                doc=u"Prénom 1 du propriétaire")

    pro_maj_prenom2 = sa.Column('pro_maj_prenom2', sa.String(),
                                doc=u"Prénom 2 du propriétaire")

    pro_maj_societe = sa.Column('pro_maj_societe', sa.String(),
                                doc=u"Nom de la société du propriétaire")

    pro_maj_adresse = sa.Column('pro_maj_adresse', sa.String(),
                                doc=u"Adresse du propriétaire")

    pro_maj_langue = sa.Column('pro_maj_langue', sa.String(),
                               doc=u"Langue parlée par le propriétaire")

    pro_maj_tel_priv = sa.Column('pro_maj_tel_priv', sa.String(),
                                 doc=u"Téléphone privé du propriétaire")

    pro_maj_fax_priv = sa.Column('pro_maj_fax_priv', sa.String(),
                                 doc=u"Fax privé du propriétaire")

    pro_maj_gsm1 = sa.Column('pro_maj_gsm1', sa.String(),
                             doc=u"GSM 1 du propriétaire")

    pro_maj_email = sa.Column('pro_maj_email', sa.String(),
                              doc=u"E-Mail du propriétaire")

    pro_maj_date_crea = sa.Column('pro_maj_date_crea', sa.Date(),
                                  default=sa.func.current_timestamp(),
                                  doc=u"Date de création de la mise à jour des informations du propriétaire")

    pro_maj_civ_fk = sa.Column('pro_maj_civ_fk', sa.Integer,
                               sa.ForeignKey('civilite.civ_pk'),
                               doc=u"Numéro d'identifiant unique vers la table civilité")

    pro_maj_com_fk = sa.Column('pro_maj_com_fk', sa.Integer,
                               sa.ForeignKey('commune.com_pk'),
                               doc=u"Numéro d'identifiant unique vers la table commune")

    pro_maj_date_naiss = sa.Column('pro_maj_date_naiss', sa.Date(),
                                   doc=u"Date de naissance du proprio")

    @mapper.Relation
    def civilite(cls):
        return sa.orm.relation(Civilite)

    @mapper.Relation
    def commune(cls):
        return sa.orm.relation(Commune)
