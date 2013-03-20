# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase


class HebergementMaj(GitesMappedClassBase):
    __tablename__ = u'hebergement_maj'

    heb_maj_pk = sa.Column('heb_maj_pk', sa.Integer, primary_key=True)

    heb_maj_hebpk = sa.Column('heb_maj_hebpk', sa.Integer())

    heb_maj_nom = sa.Column('heb_maj_nom', sa.String())

    heb_maj_adresse = sa.Column('heb_maj_adresse', sa.String())

    heb_maj_localite = sa.Column('heb_maj_localite', sa.String())

    heb_maj_tarif_we_bs = sa.Column('heb_maj_tarif_we_bs', sa.String())

    heb_maj_tarif_we_ms = sa.Column('heb_maj_tarif_we_ms', sa.String())

    heb_maj_tarif_we_hs = sa.Column('heb_maj_tarif_we_hs', sa.String())

    heb_maj_tarif_sem_bs = sa.Column('heb_maj_tarif_sem_bs', sa.String())

    heb_maj_tarif_sem_ms = sa.Column('heb_maj_tarif_sem_ms', sa.String())

    heb_maj_tarif_sem_hs = sa.Column('heb_maj_tarif_sem_hs', sa.String())

    heb_maj_tarif_garantie = sa.Column('heb_maj_tarif_garantie', sa.String())

    heb_maj_tarif_divers = sa.Column('heb_maj_tarif_divers', sa.String())

    heb_maj_descriptif_fr = sa.Column('heb_maj_descriptif_fr', sa.String())

    heb_maj_pointfort_fr = sa.Column('heb_maj_pointfort_fr', sa.String())

    heb_maj_taxe_montant = sa.Column('heb_maj_taxe_montant', sa.String())

    heb_maj_forfait_montant = sa.Column('heb_maj_forfait_montant', sa.String())

    heb_maj_tarif_we_3n = sa.Column('heb_maj_tarif_we_3n', sa.String())

    heb_maj_tarif_we_4n = sa.Column('heb_maj_tarif_we_4n', sa.String())

    heb_maj_tarif_semaine_fin_annee = sa.Column('heb_maj_tarif_semaine_fin_annee', sa.String())

    heb_maj_lit_1p = sa.Column('heb_maj_lit_1p', sa.String())

    heb_maj_lit_2p = sa.Column('heb_maj_lit_2p', sa.String())

    heb_maj_lit_sup = sa.Column('heb_maj_lit_sup', sa.String())

    heb_maj_lit_enf = sa.Column('heb_maj_lit_enf', sa.String())

    heb_maj_distribution_fr = sa.Column('heb_maj_distribution_fr', sa.String())

    heb_maj_tarif_chmbr_avec_dej_1p = sa.Column('heb_maj_tarif_chmbr_avec_dej_1p', sa.String())

    heb_maj_tarif_chmbr_avec_dej_2p = sa.Column('heb_maj_tarif_chmbr_avec_dej_2p', sa.String())

    heb_maj_tarif_chmbr_avec_dej_3p = sa.Column('heb_maj_tarif_chmbr_avec_dej_3p', sa.String())

    heb_maj_tarif_chmbr_sans_dej_1p = sa.Column('heb_maj_tarif_chmbr_sans_dej_1p', sa.String())

    heb_maj_tarif_chmbr_sans_dej_2p = sa.Column('heb_maj_tarif_chmbr_sans_dej_2p', sa.String())

    heb_maj_tarif_chmbr_sans_dej_3p = sa.Column('heb_maj_tarif_chmbr_sans_dej_3p', sa.String())

    heb_maj_tarif_chmbr_table_hote_1p = sa.Column('heb_maj_tarif_chmbr_table_hote_1p', sa.String())

    heb_maj_tarif_chmbr_table_hote_2p = sa.Column('heb_maj_tarif_chmbr_table_hote_2p', sa.String())

    heb_maj_tarif_chmbr_table_hote_3p = sa.Column('heb_maj_tarif_chmbr_table_hote_3p', sa.String())

    heb_maj_tarif_chmbr_autre_1p = sa.Column('heb_maj_tarif_chmbr_autre_1p', sa.String())

    heb_maj_tarif_chmbr_autre_2p = sa.Column('heb_maj_tarif_chmbr_autre_2p', sa.String())

    heb_maj_tarif_chmbr_autre_3p = sa.Column('heb_maj_tarif_chmbr_autre_3p', sa.String())

    heb_maj_date_crea = sa.Column('heb_maj_date_crea', sa.Date(),
                                  default=sa.func.current_timestamp())

    heb_maj_charge_fk = sa.Column('heb_maj_charge_fk', sa.Integer())
