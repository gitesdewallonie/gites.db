# -*- coding: utf-8 -*-
import sqlalchemy
from affinitic.db import mapper
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.proprio.civilite import Civilite
from gites.db.content.commune import Commune


class Proprio(GitesMappedClassBase):
    """
    Table contenant toutes les informations relatives à un propriétaire
    """

    __tablename__ = u'proprio'

    pro_pk = sqlalchemy.Column('pro_pk', sqlalchemy.Integer,
                               primary_key=True,
                               doc=u"Numéro d'identifiant unique")

    pro_nom1 = sqlalchemy.Column('pro_nom1', sqlalchemy.String(),
                                 doc=u"Nom 1 du propriétaire")

    pro_nom2 = sqlalchemy.Column('pro_nom2', sqlalchemy.String(),
                                 doc=u"Nom 2 du propriétaire")

    pro_prenom1 = sqlalchemy.Column('pro_prenom1', sqlalchemy.String(),
                                    doc=u"Prénom 1 du propriétaire")

    pro_langue = sqlalchemy.Column('pro_langue', sqlalchemy.String(),
                                   doc=u"Langue parlée par le propriétaire")

    pro_tel_priv = sqlalchemy.Column('pro_tel_priv', sqlalchemy.String(),
                                     doc=u"Téléphone privé du propriétaire")

    pro_fax_priv = sqlalchemy.Column('pro_fax_priv', sqlalchemy.String(),
                                     doc=u"Fax privé du propriétaire")

    pro_gsm1 = sqlalchemy.Column('pro_gsm1', sqlalchemy.String(),
                                 doc=u"GSM 1 du propriétaire")

    pro_email = sqlalchemy.Column('pro_email', sqlalchemy.String(),
                                  doc=u"E-Mail du propriétaire")

    pro_etat = sqlalchemy.Column('pro_etat', sqlalchemy.Boolean(),
                                 doc=u"Etat du propriétaire par rapport au paiement de sa cotisation (True/False)")

    pro_maj_info_etat = sqlalchemy.Column('pro_maj_info_etat', sqlalchemy.String(),
                                          doc=u"Etat de mise à jour des infos du propriétaire (Confirmé/En attente de confirmation/null)")

    pro_civ_fk = sqlalchemy.Column('pro_civ_fk', sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('civilite.civ_pk'),
                                   doc=u"Numéro d'identifiant unique vers la table civilité")

    pro_com_fk = sqlalchemy.Column('pro_com_fk', sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('commune.com_pk'),
                                   doc=u"Numéro d'identifiant unique vers la table commune")

    pro_reactivation_hash = sqlalchemy.Column('pro_reactivation_hash', sqlalchemy.String(),
                                              doc=u"???")

    pro_date_modification = sqlalchemy.Column('pro_date_modification', sqlalchemy.DateTime(),
                                              doc=u"Dernière date de modification des données du propriétaire")

    @mapper.Relation
    def civilite(cls):
        return sqlalchemy.orm.relation(Civilite)

    @mapper.Relation
    def commune(cls):
        return sqlalchemy.orm.relation(Commune)

    @classmethod
    def get_last_changes(cls, date, session=None):
        """Return the modified lines since the given date"""
        if not session:
            session = cls._session()
        query = session.query(cls)
        query = query.filter(cls.pro_date_modification >= date)
        return query.all()
