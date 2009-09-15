# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from sqlalchemy import Table, Column, String, Integer, ForeignKey


def getTypeInfoPratique(metadata):
    return Table('type_info_pratique', metadata, autoload=True)


def getTypeInfoTouristique(metadata):
    return Table('type_info_touristique', metadata, autoload=True)


def getInfoPratique(metadata):
    return Table('info_pratique', metadata, autoload=True)


def getReservationProprio(metadata):
    return Table('reservation_proprio', metadata, autoload=True)


def getCivilite(metadata):
    return Table('civilite', metadata,
                 Column('civ_pk', Integer, primary_key=True),
                 Column('civ_titre', String()), autoload=True)


def getLinkHebergementEpisTable(metadata):
    return Table('link_hebergement_epis', metadata,
                 Column('heb_pk', Integer, ForeignKey('hebergement.heb_pk'),
                 primary_key=True),
                 Column('heb_nombre_epis', Integer, primary_key=True))


def getCommune(metadata):
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
                 ForeignKey('maison_tourisme.mais_pk')), autoload=True)


def getProprio(metadata):
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
          Column('pro_civ_fk', Integer,
                 ForeignKey('civilite.civ_pk')),
          Column('pro_com_fk', Integer,
                 ForeignKey('commune.com_pk')), autoload=True)


def getCharge(metadata):
    return Table('charge', metadata,
          Column('cha_pk', Integer, primary_key=True),
          Column('cha_type_fr', String()),
          Column('cha_type_en', String()),
          Column('cha_type_nl', String()),
          Column('cha_type_de', String()),
          Column('cha_type_it', String()), autoload=True)


def getHebergementTable(metadata):
    autoload = False
    if metadata.bind.has_table('hebergement'):
        autoload = True
    return Table('hebergement', metadata,
             Column('heb_pk', Integer, primary_key=True),
             Column('heb_nom', String()),
             Column('heb_code_gdw', String()),
             Column('heb_charge_fk', Integer,
                    ForeignKey('charge.cha_pk')),
             Column('heb_com_fk', Integer,
                    ForeignKey('commune.com_pk')),
             Column('heb_typeheb_fk', Integer,
                    ForeignKey('type_heb.type_heb_pk')),
             Column('heb_pro_fk', Integer,
                    ForeignKey('proprio.pro_pk')), autoload=autoload,
                 useexisting=True)


def getTypeHebergementTable(metadata):
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
                 )


def getMaisonTourisme(metadata):
    return Table('maison_tourisme', metadata,
                 Column('mais_pk', Integer, primary_key=True),
                 Column('mais_nom', String()),
                 Column('mais_url', String()), autoload=True)


def getProvinces(metadata):
    return Table('provinces', metadata,
                 Column('prov_pk', Integer, primary_key=True),
                 Column('prov_nom', String()),
                 )


def getInfoTouristique(metadata):
    return Table('info_touristique', metadata,
                  Column('infotour_pk', Integer, primary_key=True),
                  Column('infotour_nom', String()),
                  Column('infotour_url', String()),
                  Column('infotour_localite', String()),
                  Column('infotour_commune_fk', Integer,
                          ForeignKey('commune.com_pk')),
                 autoload=True)


def getTableHote(metadata):
    return Table('table_hote', metadata,
                 Column('tabho_pk', Integer, primary_key=True),
                 Column('tabho_type_fr', String()),
                )


def getTypeTableHoteOfHebergement(metadata):
    return Table('heb_tab_hote', metadata,
                  Column('hebhot_heb_fk', Integer),
                  Column('hebhot_tabho_fk', Integer))
