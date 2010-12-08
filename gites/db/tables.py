# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by AFFINITIC sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from sqlalchemy import Table, Column, String, Integer, ForeignKey, Date, \
                       DateTime, Boolean, func, Sequence


def getTypeInfoPratique(metadata):
    autoload = False
    if metadata.bind.has_table('type_info_pratique'):
        autoload = True
    return Table('type_info_pratique', metadata,
                 Column('typinfoprat_pk', Integer, primary_key=True),
                 useexisting=True,
                 autoload=autoload)


def getTypeInfoTouristique(metadata):
    autoload = False
    if metadata.bind.has_table('type_info_touristique'):
        autoload = True
    return Table('type_info_touristique', metadata,
                 Column('typinfotour_pk', Integer, primary_key=True),
                 useexisting=True,
                 autoload=autoload)


def getInfoPratique(metadata):
    autoload = False
    if metadata.bind.has_table('info_pratique'):
        autoload = True
    return Table('info_pratique', metadata,
                 Column('infoprat_pk', Integer, primary_key=True),
                 useexisting=True,
                 autoload=autoload)


def getReservationProprio(metadata):
    autoload = False
    if metadata.bind.has_table('reservation_proprio'):
        autoload = True
    return Table('reservation_proprio', metadata,
                 Column('res_id', Integer, primary_key=True),
                 Column('res_date_cre', DateTime),
                 Column('res_date', DateTime, nullable=False),
                 Column('res_type', String(20), nullable=False),
                 Column('heb_fk', Integer, ForeignKey('hebergement.heb_pk'), nullable=False),
                 Column('pro_fk', Integer, ForeignKey('proprio.pro_pk')),
                 useexisting=True,
                 autoload=autoload)


def getCivilite(metadata):
    autoload = False
    if metadata.bind.has_table('civilite'):
        autoload = True
    return Table('civilite', metadata,
                 Column('civ_pk', Integer, primary_key=True),
                 Column('civ_titre', String()),
                 useexisting=True,
                 autoload=autoload)


def getLinkHebergementEpisTable(metadata):
    autoload = False
    if metadata.bind.has_table('link_hebergement_epis'):
        autoload = True
    return Table('link_hebergement_epis', metadata,
                 Column('heb_pk', Integer, ForeignKey('hebergement.heb_pk'),
                 primary_key=True),
                 Column('heb_nombre_epis', Integer, primary_key=True),
                 useexisting=True,
                 autoload=autoload)


def getCommune(metadata):
    autoload = False
    if metadata.bind.has_table('commune'):
        autoload = True
    return Table('commune', metadata,
          Column('com_pk', Integer, primary_key=True),
          Column('com_nom', String()),
          Column('com_cp', String()),
          Column('com_ins', String()),
          Column('com_reg_fk', Integer),
          Column('com_prov_fk', Integer,
                 ForeignKey('provinces.prov_pk')),
          Column('com_id', String()),
          Column('com_mais_fk', Integer,
                 ForeignKey('maison_tourisme.mais_pk')),
          useexisting=True,
          autoload=autoload)


def getProprio(metadata):
    autoload = False
    if metadata.bind.has_table('proprio'):
        autoload = True
    return Table('proprio', metadata,
          Column('pro_pk', Integer, primary_key=True),
          Column('pro_nom1', String()),
          Column('pro_nom2', String()),
          Column('pro_prenom1', String()),
          Column('pro_langue', String()),
          Column('pro_tel_priv', String()),
          Column('pro_fax_priv', String()),
          Column('pro_gsm1', String()),
          Column('pro_email', String()),
          Column('pro_url', String()),
          Column('pro_etat', Boolean()),
          Column('pro_maj_info_etat', String()),
          Column('pro_civ_fk', Integer,
                 ForeignKey('civilite.civ_pk')),
          Column('pro_com_fk', Integer,
                 ForeignKey('commune.com_pk')),
          useexisting=True,
          autoload=autoload)


def getProprioMaj(metadata):
    autoload = False
    if metadata.bind.has_table('proprio_maj'):
        autoload = True
    return Table('proprio_maj', metadata,
          Column('pro_maj_pk', Integer, primary_key=True),
          Column('pro_maj_propk', Integer()),
          Column('pro_maj_nom1', String()),
          Column('pro_maj_nom2', String()),
          Column('pro_maj_prenom1', String()),
          Column('pro_maj_prenom2', String()),
          Column('pro_maj_societe', String()),
          Column('pro_maj_adresse', String()),
          Column('pro_maj_langue', String()),
          Column('pro_maj_tel_priv', String()),
          Column('pro_maj_fax_priv', String()),
          Column('pro_maj_gsm1', String()),
          Column('pro_maj_email', String()),
          Column('pro_maj_url', String()),
          Column('pro_maj_date_crea', Date(), default=func.current_timestamp()),
          Column('pro_maj_civ_fk', Integer,
              ForeignKey('civilite.civ_pk')),
          Column('pro_maj_com_fk', Integer,
              ForeignKey('commune.com_pk')),
          useexisting=True,
          autoload=autoload)


def getCharge(metadata):
    autoload = False
    if metadata.bind.has_table('charge'):
        autoload = True
    return Table('charge', metadata,
          Column('cha_pk', Integer, primary_key=True),
          Column('cha_type_fr', String()),
          Column('cha_type_en', String()),
          Column('cha_type_nl', String()),
          Column('cha_type_de', String()),
          Column('cha_type_it', String()),
          useexisting=True,
          autoload=autoload)


def getHebergementTable(metadata):
    autoload = False
    if metadata.bind.has_table('hebergement'):
        autoload = True
    return Table('hebergement', metadata,
             Column('heb_pk', Integer, primary_key=True),
             Column('heb_nom', String()),
             Column('heb_code_gdw', String()),
             Column('heb_code_gdw', String()),
             Column('heb_site_public', String()),
             Column('heb_calendrier_proprio', String()),
             Column('heb_charge_fk', Integer,
                    ForeignKey('charge.cha_pk')),
             Column('heb_com_fk', Integer,
                    ForeignKey('commune.com_pk')),
             Column('heb_typeheb_fk', Integer,
                    ForeignKey('type_heb.type_heb_pk')),
             Column('heb_pro_fk', Integer,
                    ForeignKey('proprio.pro_pk')),
             Column('heb_calendrier_proprio_date_maj', Date),
             useexisting=True,
             autoload=autoload)


def getTypeHebergementTable(metadata):
    autoload = False
    if metadata.bind.has_table('type_heb'):
        autoload = True
    return Table('type_heb', metadata,
                 Column('type_heb_pk', Integer, primary_key=True),
                 Column('type_heb_code', String()),
                 Column('type_heb_nom', String()),
                 Column('type_heb_id', String()),
                 Column('type_heb_id_nl', String()),
                 Column('type_heb_id_de', String()),
                 Column('type_heb_id_it', String()),
                 Column('type_heb_id_uk', String()),
                 Column('type_heb_nom_nl', String()),
                 Column('type_heb_nom_de', String()),
                 Column('type_heb_nom_it', String()),
                 Column('type_heb_nom_uk', String()),
                 useexisting=True,
                 autoload=autoload)


def getHebergementMajTable(metadata):
    autoload = False
    if metadata.bind.has_table('hebergement_maj'):
        autoload = True
    return Table('hebergement_maj', metadata,
                    Column('heb_maj_pk', Integer, primary_key=True),
                    Column('heb_maj_hebpk', Integer()),
                    Column('heb_maj_nom', String()),
                    Column('heb_maj_adresse', String()),
                    Column('heb_maj_localite', String()),
                    Column('heb_maj_tenis', String()),
                    Column('heb_maj_nautisme', String()),
                    Column('heb_maj_sky', String()),
                    Column('heb_maj_rando', String()),
                    Column('heb_maj_piscine', String()),
                    Column('heb_maj_peche', String()),
                    Column('heb_maj_equitation', String()),
                    Column('heb_maj_velo', String()),
                    Column('heb_maj_vtt', String()),
                    Column('heb_maj_ravel', String()),
                    Column('heb_maj_animal', String()),
                    Column('heb_maj_tarif_we_bs', String()),
                    Column('heb_maj_tarif_we_ms', String()),
                    Column('heb_maj_tarif_we_hs', String()),
                    Column('heb_maj_tarif_sem_bs', String()),
                    Column('heb_maj_tarif_sem_ms', String()),
                    Column('heb_maj_tarif_sem_hs', String()),
                    Column('heb_maj_tarif_garantie', String()),
                    Column('heb_maj_tarif_divers', String()),
                    Column('heb_maj_descriptif_fr', String()),
                    Column('heb_maj_pointfort_fr', String()),
                    Column('heb_maj_fumeur', String()),
                    Column('heb_maj_tenis_distance', String()),
                    Column('heb_maj_nautisme_distance', String()),
                    Column('heb_maj_sky_distance', String()),
                    Column('heb_maj_rando_distance', String()),
                    Column('heb_maj_piscine_distance', String()),
                    Column('heb_maj_peche_distance', String()),
                    Column('heb_maj_equitation_distance', String()),
                    Column('heb_maj_velo_distance', String()),
                    Column('heb_maj_vtt_distance', String()),
                    Column('heb_maj_ravel_distance', String()),
                    Column('heb_maj_confort_tv', String()),
                    Column('heb_maj_confort_feu_ouvert', String()),
                    Column('heb_maj_confort_lave_vaiselle', String()),
                    Column('heb_maj_confort_micro_onde', String()),
                    Column('heb_maj_confort_lave_linge', String()),
                    Column('heb_maj_confort_seche_linge', String()),
                    Column('heb_maj_confort_congelateur', String()),
                    Column('heb_maj_confort_internet', String()),
                    Column('heb_maj_taxe_sejour', String()),
                    Column('heb_maj_taxe_montant', String()),
                    Column('heb_maj_forfait_montant', String()),
                    Column('heb_maj_tarif_we_3n', String()),
                    Column('heb_maj_tarif_we_4n', String()),
                    Column('heb_maj_tarif_semaine_fin_annee', String()),
                    Column('heb_maj_lit_1p', String()),
                    Column('heb_maj_lit_2p', String()),
                    Column('heb_maj_lit_sup', String()),
                    Column('heb_maj_lit_enf', String()),
                    Column('heb_maj_distribution_fr', String()),
                    Column('heb_maj_commerce', String()),
                    Column('heb_maj_restaurant', String()),
                    Column('heb_maj_gare', String()),
                    Column('heb_maj_gare_distance', String()),
                    Column('heb_maj_restaurant_distance', String()),
                    Column('heb_maj_commerce_distance', String()),
                    Column('heb_maj_tarif_chmbr_avec_dej_1p', String()),
                    Column('heb_maj_tarif_chmbr_avec_dej_2p', String()),
                    Column('heb_maj_tarif_chmbr_avec_dej_3p', String()),
                    Column('heb_maj_tarif_chmbr_sans_dej_1p', String()),
                    Column('heb_maj_tarif_chmbr_sans_dej_2p', String()),
                    Column('heb_maj_tarif_chmbr_sans_dej_3p', String()),
                    Column('heb_maj_tarif_chmbr_table_hote_1p', String()),
                    Column('heb_maj_tarif_chmbr_table_hote_2p', String()),
                    Column('heb_maj_tarif_chmbr_table_hote_3p', String()),
                    Column('heb_maj_tarif_chmbr_autre_1p', String()),
                    Column('heb_maj_tarif_chmbr_autre_2p', String()),
                    Column('heb_maj_tarif_chmbr_autre_3p', String()),
                    Column('heb_maj_date_crea', Date(), default=func.current_timestamp()),
                    Column('heb_maj_charge_fk', Integer()),
                    useexisting=True,
                    autoload=autoload)


def getMaisonTourisme(metadata):
    autoload = False
    if metadata.bind.has_table('maison_tourisme'):
        autoload = True
    return Table('maison_tourisme', metadata,
                 Column('mais_pk', Integer, primary_key=True),
                 Column('mais_nom', String()),
                 Column('mais_url', String()),
                 useexisting=True,
                 autoload=autoload)


def getProvinces(metadata):
    autoload = False
    if metadata.bind.has_table('provinces'):
        autoload = True
    return Table('provinces', metadata,
                 Column('prov_pk', Integer, primary_key=True),
                 Column('prov_nom', String()),
                 useexisting=True,
                 autoload=autoload)


def getInfoTouristique(metadata):
    autoload = False
    if metadata.bind.has_table('info_touristique'):
        autoload = True
    return Table('info_touristique', metadata,
                  Column('infotour_pk', Integer, primary_key=True),
                  Column('infotour_nom', String()),
                  Column('infotour_url', String()),
                  Column('infotour_localite', String()),
                  Column('infotour_commune_fk', Integer,
                          ForeignKey('commune.com_pk')),
                 useexisting=True,
                 autoload=autoload)


def getTableHote(metadata):
    autoload = False
    if metadata.bind.has_table('table_hote'):
        autoload = True
    return Table('table_hote', metadata,
                 Column('tabho_pk', Integer, primary_key=True),
                 Column('tabho_type_fr', String()),
                 useexisting=True,
                 autoload=autoload)


def getTypeTableHoteOfHebergement(metadata):
    autoload = False
    if metadata.bind.has_table('heb_tab_hote'):
        autoload = True
    return Table('heb_tab_hote', metadata,
                  Column('hebhot_heb_fk', Integer),
                  Column('hebhot_tabho_fk', Integer),
                  useexisting=True,
                  autoload=autoload)


def getTypeTableHoteOfHebergementMaj(metadata):
    return Table('heb_tab_hote_maj', metadata,
                  Column('hebhot_maj_heb_fk', Integer),
                  Column('hebhot_maj_tabho_fk', Integer))


def getHebBlockedHistory(metadata):
    return Table('heb_blocking_history', metadata,
                 Column('heb_blockhistory_id', Integer,
                        Sequence('heb_blockhistory_id_seq'), primary_key=True),
                 Column('heb_blockhistory_blocked_dte', Date, nullable=False),
                 Column('heb_blockhistory_activated_dte', Date, nullable=True),
                 Column('heb_blockhistory_heb_pk', Integer,
                        ForeignKey('hebergement.heb_pk'), nullable=False),
                 Column('heb_blockhistory_days', Integer, nullable=True))


def getBlockingHistory(metadata):
    return Table('blockinghistory', metadata,
                 Column('heb_pk', Integer, ForeignKey('hebergement.heb_pk'), primary_key=True),
                 Column('block_start', DateTime, primary_key=True),
                 Column('block_end', DateTime, primary_key=True))


def getLogTable(metadata):
    autoload = False
    if metadata.bind.has_table('log'):
        autoload = True
    return Table('log', metadata,
                 Column('log_pk', Integer(), Sequence('log_log_pk_seq'),
                        primary_key=True),
                 Column('log_date', DateTime(), nullable=False),
                 Column('log_path', String(), nullable=False),
                 Column('log_hebpk', Integer(), ForeignKey('hebergement.heb_pk')),
                 Column('log_host', String()),
                 Column('log_agent', String()),
                 Column('log_website', String()),
                 useexisting=True,
                 autoload=autoload)
