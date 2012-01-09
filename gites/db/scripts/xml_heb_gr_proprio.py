#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# MEURANT ALain AFFINITIC
#
# Avril 2010
#
# Projet Gites de Wallonie
#
# extraction complete des donnees de postgresql
# sqlalchemy - postgresql
#
# extraction des donnees pour les type GR MT GRECR GG GF GC GR MV
# derniere utilisation : Avril 2010 extration pour carte proprio de Mike
#
# python2.6 sqlalchemy_xml_heb_gr_proprio_2008.py
#

from sqlalchemy import create_engine


def ouverture_connection():
    """
    ouverture de la connection db
    """
    #driver://username:password@host:port/database
    pg_db = create_engine('postgresql://alain:nostromos@localhost:5432/gites_wallons',
                          convert_unicode=True,
                          encoding='utf-8')
    connection = pg_db.connect()
    hebergements = connection.execute(" \
        select \
            hebergement.heb_pk, \
            hebergement.heb_adresse, \
            hebergement.heb_localite, \
            hebergement.heb_cgt_cap_min, \
            hebergement.heb_cgt_cap_max, \
            hebergement.heb_cgt_nbre_chmbre, \
            link_hebergement_epis.heb_nombre_epis, \
            hebergement.heb_lit_1p, \
            hebergement.heb_lit_2p, \
            hebergement.heb_lit_sup, \
            hebergement.heb_lit_enf, \
            type_heb.type_heb_nom, \
            hebergement.heb_coordonnee, \
            proprio.pro_prenom1, \
            proprio.pro_prenom2, \
            proprio.pro_nom1, \
            proprio.pro_nom2, \
            hebergement.heb_nom, \
            hebergement.heb_gid_activite_nature, \
            hebergement.heb_gid_theme_equestre, \
            hebergement.heb_gid_peche, \
            hebergement.heb_gid_panda, \
            hebergement.heb_gid_patrimoine, \
            hebergement.heb_gid_antiallergique, \
            hebergement.heb_gid_access_tous, \
            hebergement.heb_gid_bebe_tendresse, \
            hebergement.heb_gid_beau_jardin, \
            hebergement.heb_gid_eco_gite, \
            proprio.pro_tel_priv, \
            proprio.pro_gsm1, \
            commune.com_nom, \
            commune.com_cp, \
            proprio.pro_email, \
            hebergement.heb_tarif_we_bs, \
            hebergement.heb_tarif_we_ms, \
            hebergement.heb_tarif_we_hs, \
            hebergement.heb_tarif_sem_bs, \
            hebergement.heb_tarif_sem_ms, \
            hebergement.heb_tarif_sem_hs, \
            hebergement.heb_fumeur, \
            hebergement.heb_animal \
        from \
            hebergement left outer join link_hebergement_epis on link_hebergement_epis.heb_pk = hebergement.heb_pk, \
            commune, \
            type_heb, \
            proprio \
        where \
            hebergement.heb_typeheb_fk in (1,2,3,4,7,10) \
            and \
            commune.com_pk=hebergement.heb_com_fk \
            and \
            type_heb.type_heb_pk=hebergement.heb_typeheb_fk \
            and \
            proprio.pro_pk=hebergement.heb_pro_fk \
            and \
            proprio.pro_etat=True \
            and \
            hebergement.heb_site_public = '1' \
        order by \
            hebergement.heb_localite, \
            proprio.pro_nom1, \
            hebergement.heb_nom")
    return hebergements


def creer_fichier(nom_file):
    """creation du fichier xml de destination
      ecriture de la phrase d'entete xml
      fermeture fichier
    """
    fichier = open(nom_file, 'w')
    fichier.write("<?xml version='1.0' encoding='UTF-8' standalone='yes'?>\n")
    fichier.close()


def ouvrir_fichier(nom_file):
    """ouverture du fichier en mode ajout"""
    fichier_xml = open(nom_file, 'a')
    return fichier_xml


def fermer_fichier(nom_file):
    """fermeture du fichier"""
    nom_file.close()


def main():
    print
    print
    print '======================================================'
    print '*** DEBUT GENERATION DU FICHIER XML GR GF MH  ***'
    print '------------------------------------------------------'

    nom_file = 'gdw_gr_gf_mt.xml'
    creer_fichier(nom_file)
    file = ouvrir_fichier(nom_file)
    file.write('<gites_wallons>\n')

    #execution de la requete SQL
    hebergement = ouverture_connection()

    compteur = 0

    if hebergement:
        for elem in hebergement:
            compteur = compteur + 1
            #print compteur, '>>',elem.heb_code_gdw, elem.heb_nom
            file.write('<hebergement>\n')
            localite = elem.heb_localite
            print elem
            file.write('\t<localite>%s</localite>\n' % localite)
            file.write('\t<coordonnee>%s</coordonnee>\n' % elem.heb_coordonnee)
            file.write('\t<proprio_prenom1>%s</proprio_prenom1>\n' % elem.pro_prenom1)
            file.write('\t<proprio_prenom2>%s</proprio_prenom2>\n' % elem.pro_prenom2)
            file.write('\t<proprio_nom1>%s</proprio_nom1>\n' % elem.pro_nom1)
            print elem.pro_prenom1
            print elem.pro_prenom2
            print elem.pro_nom1
            print compteur
            print '---------------------------------------------------------------------------------'
            file.write('\t<proprio_email>%s</proprio_email>\n' % elem.pro_email)
            file.write('\t<id>%s</id>\n' % elem.heb_pk)
            file.write('\t<cap_min>%s</cap_min>\n' % elem.heb_cgt_cap_min)
            file.write('\t<cap_max>%s</cap_max>\n' % elem.heb_cgt_cap_max)
            file.write('\t<proprio_gsm>%s</proprio_gsm>\n' % elem.pro_gsm1)
            file.write('\t<proprio_tel>%s</proprio_tel>\n' % elem.pro_tel_priv)
            #recherche du & et remplacement par espace
            nom = elem.heb_nom
            if nom:
                if '&' in nom:
                    nom = nom.replace('&', ' et ')
                    #print nom
            file.write('\t<nom>%s</nom>\n' % nom)
            file.write('\t<tarif_we_bs>%s</tarif_we_bs>\n' % elem.heb_tarif_we_bs)
            file.write('\t<tarif_we_ms>%s</tarif_we_ms>\n' % elem.heb_tarif_we_ms)
            file.write('\t<tarif_we_hs>%s</tarif_we_hs>\n' % elem.heb_tarif_we_hs)
            file.write('\t<tarif_sem_bs>%s</tarif_sem_bs>\n' % elem.heb_tarif_sem_bs)
            file.write('\t<tarif_sem_ms>%s</tarif_sem_ms>\n' % elem.heb_tarif_sem_ms)
            file.write('\t<tarif_sem_hs>%s</tarif_sem_hs>\n' % elem.heb_tarif_sem_hs)
            file.write('\t<epis>%s</epis>\n' % elem.heb_nombre_epis)
            file.write('\t<type>%s</type>\n' % elem.type_heb_nom)
            file.write('</hebergement>\n')
    file.write('</gites_wallons>\n')
    #fermer_fichier(nom_file)
    file.close()

    #nombre de record de la selection
    print
    print "**** Nombre d'hebergements extraits : %i ***" % compteur

    print '------------------------------------------------------'
    print "*** GENERATION DU FICHIER XML TERMINEE GR GF MH ***"
    print '======================================================'

if __name__ == "__main__":
    main()
