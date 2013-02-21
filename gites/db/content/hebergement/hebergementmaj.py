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

    heb_maj_tenis = sa.Column('heb_maj_tenis', sa.String())

    heb_maj_nautisme = sa.Column('heb_maj_nautisme', sa.String())

    heb_maj_sky = sa.Column('heb_maj_sky', sa.String())

    heb_maj_rando = sa.Column('heb_maj_rando', sa.String())

    heb_maj_piscine = sa.Column('heb_maj_piscine', sa.String())

    heb_maj_peche = sa.Column('heb_maj_peche', sa.String())

    heb_maj_equitation = sa.Column('heb_maj_equitation', sa.String())

    heb_maj_velo = sa.Column('heb_maj_velo', sa.String())

    heb_maj_vtt = sa.Column('heb_maj_vtt', sa.String())

    heb_maj_ravel = sa.Column('heb_maj_ravel', sa.String())

    heb_maj_animal = sa.Column('heb_maj_animal', sa.String())

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

    heb_maj_fumeur = sa.Column('heb_maj_fumeur', sa.String())

    heb_maj_tenis_distance = sa.Column('heb_maj_tenis_distance', sa.String())

    heb_maj_nautisme_distance = sa.Column('heb_maj_nautisme_distance', sa.String())

    heb_maj_sky_distance = sa.Column('heb_maj_sky_distance', sa.String())

    heb_maj_rando_distance = sa.Column('heb_maj_rando_distance', sa.String())

    heb_maj_piscine_distance = sa.Column('heb_maj_piscine_distance', sa.String())

    heb_maj_peche_distance = sa.Column('heb_maj_peche_distance', sa.String())

    heb_maj_equitation_distance = sa.Column('heb_maj_equitation_distance', sa.String())

    heb_maj_velo_distance = sa.Column('heb_maj_velo_distance', sa.String())

    heb_maj_vtt_distance = sa.Column('heb_maj_vtt_distance', sa.String())

    heb_maj_ravel_distance = sa.Column('heb_maj_ravel_distance', sa.String())

    heb_maj_confort_tv = sa.Column('heb_maj_confort_tv', sa.String())

    heb_maj_confort_feu_ouvert = sa.Column('heb_maj_confort_feu_ouvert', sa.String())

    heb_maj_confort_lave_vaiselle = sa.Column('heb_maj_confort_lave_vaiselle', sa.String())

    heb_maj_confort_micro_onde = sa.Column('heb_maj_confort_micro_onde', sa.String())

    heb_maj_confort_lave_linge = sa.Column('heb_maj_confort_lave_linge', sa.String())

    heb_maj_confort_seche_linge = sa.Column('heb_maj_confort_seche_linge', sa.String())

    heb_maj_confort_congelateur = sa.Column('heb_maj_confort_congelateur', sa.String())

    heb_maj_confort_internet = sa.Column('heb_maj_confort_internet', sa.String())

    heb_maj_taxe_sejour = sa.Column('heb_maj_taxe_sejour', sa.String())

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

    heb_maj_commerce = sa.Column('heb_maj_commerce', sa.String())

    heb_maj_restaurant = sa.Column('heb_maj_restaurant', sa.String())

    heb_maj_gare = sa.Column('heb_maj_gare', sa.String())

    heb_maj_gare_distance = sa.Column('heb_maj_gare_distance', sa.String())

    heb_maj_restaurant_distance = sa.Column('heb_maj_restaurant_distance', sa.String())

    heb_maj_commerce_distance = sa.Column('heb_maj_commerce_distance', sa.String())

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
