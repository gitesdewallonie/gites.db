# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class HebergementMaj(GitesMappedClassBase):
    """
    Table intermédiaire utilisée lors de la mise à jour d'un hébergement par un propriétaire
    """

    __tablename__ = u'hebergement_maj'

    heb_maj_pk = sa.Column('heb_maj_pk', sa.Integer,
                           primary_key=True,
                           doc=u"Identifiant unique pour une mise à jour")

    heb_maj_hebpk = sa.Column('heb_maj_hebpk', sa.Integer(),
                              doc=u"Identifiant unique pour un hébergement mis à jour")

    heb_maj_nom = sa.Column('heb_maj_nom', sa.String(),
                            doc=u"Nom de l'hébergement")

    heb_maj_url = sa.Column('heb_maj_url', sa.String(),
                            doc=u"Url du site privé de l'hébergement")

    heb_maj_adresse = sa.Column('heb_maj_adresse', sa.String(),
                                doc=u"Adresse postale de l'hébergement")

    heb_maj_localite = sa.Column('heb_maj_localite', sa.String(),
                                 doc=u"Localité de l'hébergement")

    heb_maj_tarif_we_bs = sa.Column('heb_maj_tarif_we_bs', sa.String(),
                                    doc=u"Tarif week-end basse saison de l'hébergement")

    heb_maj_tarif_we_ms = sa.Column('heb_maj_tarif_we_ms', sa.String(),
                                    doc=u"Tarif week-end moyenne saison de l'hébergement")

    heb_maj_tarif_we_hs = sa.Column('heb_maj_tarif_we_hs', sa.String(),
                                    doc=u"Tarif week-end haute saison de l'hébergement")

    heb_maj_tarif_sem_bs = sa.Column('heb_maj_tarif_sem_bs', sa.String(),
                                     doc=u"Tarif semaine basse saison de l'hébergement")

    heb_maj_tarif_sem_ms = sa.Column('heb_maj_tarif_sem_ms', sa.String(),
                                     doc=u"Tarif semaine moyenne saison de l'hébergement")

    heb_maj_tarif_sem_hs = sa.Column('heb_maj_tarif_sem_hs', sa.String(),
                                     doc=u"Tarif semaine haute saison de l'hébergement")

    heb_maj_tarif_garantie = sa.Column('heb_maj_tarif_garantie', sa.String(),
                                       doc=u"Tarif garantie de location de l'hébergement")

    heb_maj_tarif_divers = sa.Column('heb_maj_tarif_divers', sa.String(),
                                     doc=u"Tarif divers de l'hébergement")

    heb_maj_descriptif_fr = sa.Column('heb_maj_descriptif_fr', sa.String(),
                                      doc=u"Description francophone de l'hébergement")

    heb_maj_pointfort_fr = sa.Column('heb_maj_pointfort_fr', sa.String(),
                                     doc=u"Point fort francophone de l'hébergement")

    heb_maj_taxe_montant = sa.Column('heb_maj_taxe_montant', sa.String(),
                                     doc=u"Montant de la taxe de séjour de l'hébergement")

    heb_maj_forfait_montant = sa.Column('heb_maj_forfait_montant', sa.String(),
                                        doc=u"Montant du forfait de l'hébergement")

    heb_maj_tarif_we_3n = sa.Column('heb_maj_tarif_we_3n', sa.String(),
                                    doc=u"Tarif week-end 3eme nuitée de l'hébergement")

    heb_maj_tarif_we_4n = sa.Column('heb_maj_tarif_we_4n', sa.String(),
                                    doc=u"Tarif week-end 4eme nuitée de l'hébergement")

    heb_maj_tarif_semaine_fin_annee = sa.Column('heb_maj_tarif_semaine_fin_annee', sa.String(),
                                                doc=u"Tarif semaine fin d'année de l'hébergement")

    heb_maj_lit_1p = sa.Column('heb_maj_lit_1p', sa.String(),
                               doc=u"Nombre de lit de 1 personne dans l'hébergement")

    heb_maj_lit_2p = sa.Column('heb_maj_lit_2p', sa.String(),
                               doc=u"Nombre de lit de 2 personnes dans l'hébergement")

    heb_maj_lit_sup = sa.Column('heb_maj_lit_sup', sa.String(),
                                doc=u"Nombre de lit superposé dans l'hébergement")

    heb_maj_lit_enf = sa.Column('heb_maj_lit_enf', sa.String(),
                                doc=u"Nombre de lit enfant dans l'hébergement")

    heb_maj_distribution_fr = sa.Column('heb_maj_distribution_fr', sa.String(),
                                        doc=u"Distribution du matériel dans l'hébergement")

    heb_maj_tarif_chmbr_avec_dej_1p = sa.Column('heb_maj_tarif_chmbr_avec_dej_1p', sa.String(),
                                                doc=u"Tarif d'une chambre pour une personne avec petit déjeuner")

    heb_maj_tarif_chmbr_avec_dej_2p = sa.Column('heb_maj_tarif_chmbr_avec_dej_2p', sa.String(),
                                                doc=u"Tarif d'une chambre pour deux personnes avec petit déjeuner")

    heb_maj_tarif_chmbr_avec_dej_3p = sa.Column('heb_maj_tarif_chmbr_avec_dej_3p', sa.String(),
                                                doc=u"Tarif d'une chambre pour trois personnes avec petit déjeuner")

    heb_maj_tarif_chmbr_sans_dej_1p = sa.Column('heb_maj_tarif_chmbr_sans_dej_1p', sa.String(),
                                                doc=u"Tarif d'une chambre pour une personne sans petit déjeuner")

    heb_maj_tarif_chmbr_sans_dej_2p = sa.Column('heb_maj_tarif_chmbr_sans_dej_2p', sa.String(),
                                                doc=u"Tarif d'une chambre pour deux personnes sans petit déjeuner")

    heb_maj_tarif_chmbr_sans_dej_3p = sa.Column('heb_maj_tarif_chmbr_sans_dej_3p', sa.String(),
                                                doc=u"Tarif d'une chambre pour trois personnes sans petit déjeuner")

    heb_maj_tarif_chmbr_table_hote_1p = sa.Column('heb_maj_tarif_chmbr_table_hote_1p', sa.String(),
                                                  doc=u"Tarif d'une chambre pour une personne avec table d'hôte")

    heb_maj_tarif_chmbr_table_hote_2p = sa.Column('heb_maj_tarif_chmbr_table_hote_2p', sa.String(),
                                                  doc=u"Tarif d'une chambre pour deux personnes avec table d'hôte")

    heb_maj_tarif_chmbr_table_hote_3p = sa.Column('heb_maj_tarif_chmbr_table_hote_3p', sa.String(),
                                                  doc=u"Tarif d'une chambre pour trois personnes avec table d'hôte")

    heb_maj_tarif_chmbr_autre_1p = sa.Column('heb_maj_tarif_chmbr_autre_1p', sa.String(),
                                             doc=u"Tarif d'une autre chambre pour une personne")

    heb_maj_tarif_chmbr_autre_2p = sa.Column('heb_maj_tarif_chmbr_autre_2p', sa.String(),
                                             doc=u"Tarif d'une autre chambre pour deux personnes")

    heb_maj_tarif_chmbr_autre_3p = sa.Column('heb_maj_tarif_chmbr_autre_3p', sa.String(),
                                             doc=u"Tarif d'une autre chambre pour trois personnes")

    heb_maj_date_crea = sa.Column('heb_maj_date_crea', sa.Date(),
                                  default=sa.func.current_timestamp(),
                                  doc=u"Date de création de la mise à jour de l'hébergement")

    heb_maj_charge_fk = sa.Column('heb_maj_charge_fk', sa.Integer(),
                                  doc=u"Numéro d'identifiant unique vers la table charge de l'hébergement")
