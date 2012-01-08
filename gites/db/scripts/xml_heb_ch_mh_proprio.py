#!usr/bin/env python
#
# MEURANT ALain
#
# Fevrier 2008
#
# Projet Gites de Wallonie
#
# extraction completes des donnees de postgresql
# sqlalchemy - postgresql
#
# extraction des donnees pour les type CH MH CHECR
#                                      6  5  9
# derniere utilisation : janvier 2012 extraction pour les cartes de proprios de Mike
#
# sous linux
# python sqlalchemy_xml_heb_ch_mh_proprio_2008.py
# ou
# python2.6 sqlalchemy_xml_heb_ch_mh_proprio_2008.py

#

from sqlalchemy import *


def ouverture_connection(requete):
    """ouverture de la connection db"""
    #driver://username:password@host:port/database
    pg_db = create_engine('postgresql://alain:nostromos@localhost:5432/gites_wallons')
    connection=pg_db.connect()
    data=connection.execute(requete)
    return data


def creer_fichier(nom_file):
    """
    creation du fichier xml de destination
    ecriture de la phrase d'entete xml
    fermeture fichier
    """
    fichier=open(nom_file, 'w')
    fichier.write("<?xml version='1.0' encoding='UTF-8' standalone='yes'?>\n")
    fichier.close()


def ouvrir_fichier(nom_file):
    """
    ouverture du fichier en mode ajout
    """
    fichier_xml=open(nom_file, 'a')
    return fichier_xml


def fermer_fichier(nom_file):
    """
    fermeture du fichier
    """
    nom_file.close()


def table_hote(heb_pk):
    requete_table_hote=" \
        SELECT \
            heb_code_gdw, \
            tabho_type_fr, \
            heb_pk \
        FROM \
            heb_tab_hote, \
            table_hote, \
            hebergement \
        WHERE \
            (hebhot_tabho_fk = tabho_pk \
            AND \
            hebhot_heb_fk = heb_pk) \
            AND \
            ((heb_pk= %s))"%(heb_pk)
    return requete_table_hote


def table_hebergement():
    requete_hebergement=" \
    select \
        hebergement.heb_pk, \
        hebergement.heb_localite, \
        hebergement.heb_coordonnee, \
        hebergement.heb_nom, \
        hebergement.heb_cgt_nbre_chmbre, \
        link_hebergement_epis.heb_nombre_epis, \
        hebergement.heb_adresse, \
        commune.com_cp, \
        commune.com_nom, \
        hebergement.heb_tarif_chmbr_avec_dej_2p, \
        proprio.pro_prenom1, \
        proprio.pro_prenom2, \
        proprio.pro_nom1, \
        proprio.pro_nom2, \
        proprio.pro_tel_priv, \
        proprio.pro_gsm1, \
        proprio.pro_email, \
        hebergement.heb_tarif_chmbr_table_hote_1p, \
        hebergement.heb_tarif_chmbr_table_hote_2p, \
        hebergement.heb_tarif_chmbr_table_hote_3p \
    from \
        hebergement left outer join link_hebergement_epis on link_hebergement_epis.heb_pk = hebergement.heb_pk, \
        commune, \
        type_heb, \
        proprio \
    where \
        hebergement.heb_typeheb_fk in (5,6,9) \
        and \
        commune.com_pk = hebergement.heb_com_fk \
        and \
        type_heb.type_heb_pk = hebergement.heb_typeheb_fk \
        and \
        proprio.pro_pk = hebergement.heb_pro_fk \
        and \
        proprio.pro_etat = True\
        and \
        hebergement.heb_site_public = '1'\
    order by \
        hebergement.heb_localite, \
        proprio.pro_nom1"
    return requete_hebergement

if __name__=="__main__":
    print
    print
    print '======================================================'
    print '*** DEBUT GENERATION DU FICHIER XML CH MH ***'
    print '------------------------------------------------------'
    nom_file='gdw_ch_mh.xml'
    creer_fichier(nom_file)
    file=ouvrir_fichier(nom_file)
    file.write('<gites_wallons>\n')

    #execution de la requete SQL
    requete_hebergement=table_hebergement()
    hebergement=ouverture_connection(requete_hebergement)

    #for table in table_hoteviv :
    #    print table.heb_code_gdw, table.tabho_type_fr


    compteur=1
    if hebergement:
        for elem in hebergement:
            #print '>>%s. %s - %s - %s'%(compteur, elem.heb_pk, elem.heb_code_gdw, elem.heb_nom)
            file.write('<hebergement>\n')
            file.write('\t<localite>%s</localite>\n'%(elem.heb_localite))
            file.write('\t<coordonnee>%s</coordonnee>\n'%(elem.heb_coordonnee))
            file.write('\t<proprio_prenom1>%s</proprio_prenom1>\n'%(elem.pro_prenom1))
            file.write('\t<proprio_prenom2>%s</proprio_prenom2>\n'%(elem.pro_prenom2))
            file.write('\t<proprio_nom1>%s</proprio_nom1>\n'%(elem.pro_nom1))
            file.write('\t<proprio_tel>%s</proprio_tel>\n'%(elem.pro_tel_priv))
            file.write('\t<proprio_gsm>%s</proprio_gsm>\n'%(elem.pro_gsm1))
            file.write('\t<adresse>%s</adresse>\n'%(elem.heb_adresse))
            file.write('\t<code_postal>%s</code_postal>\n'%(elem.com_cp))
            file.write('\t<entite>%s</entite>\n'%(elem.com_nom))
            file.write('\t<id>%s</id>\n'%(elem.heb_pk))
            file.write('\t<nbre_chambre>%s</nbre_chambre>\n'%(elem.heb_cgt_nbre_chmbre))
            file.write('\t<bloc_table_hote>\n')
            requete_table=table_hote(elem.heb_pk)
            table=ouverture_connection(requete_table)
            #hebgdw=elem.heb_code_gdw
            compt=1
            for tab in table:
                #print '%s :: %s'%(tab.heb_code_gdw, tab.tabho_type_fr )
                file.write('\t\t<tarif_chambre_table_hote_%sp>%s</tarif_chambre_table_hote_%sp>\n'%(compt, tab[1], compt))
                compt=compt+1
            file.write('\t</bloc_table_hote>\n')
            file.write('\t<proprio_email>%s</proprio_email>\n'%(elem.pro_email))
            #recherche du & et remplacement par espace
            c=elem.heb_nom
            if c:
                if '&' in c:
                    c=c.replace('&', ' et ')
                    #print c
            file.write('\t<nom>%s</nom>\n'%c)
            file.write('\t<tarif_chambre_avec_dej_2p>%s</tarif_chambre_avec_dej_2p>\n'%(elem.heb_tarif_chmbr_avec_dej_2p))
            file.write('\t<epis>%s</epis>\n'%(elem.heb_nombre_epis))
            file.write('</hebergement>\n')
            compteur=compteur+1
    file.write('</gites_wallons>\n')
    #fermer_fichier(nom_file)
    file.close()

    #nombre de record de la selection
    #print
    print "**** Nombre d'hebergement extraits : %i ***"%(compteur-1)

    print '------------------------------------------------------'
    print "*** GENERATION DU FICHIER XML TERMINEE ***"
    print '======================================================'
