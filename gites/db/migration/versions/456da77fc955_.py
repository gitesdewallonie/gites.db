"""Add reservations columns

Revision ID: 456da77fc955
Revises: 57c82bea5928
Create Date: 2016-02-15 11:45:51.762206

"""

# revision identifiers, used by Alembic.
revision = '456da77fc955'
down_revision = '57c82bea5928'

from alembic import op


def upgrade():
    op.execute('DROP VIEW hebergement_view')
    op.execute('''
        CREATE VIEW hebergement_view AS
        SELECT hebergement.heb_pk,
               hebergement.heb_code_gdw,
               hebergement.heb_nom,
               hebergement.heb_adresse,
               hebergement.heb_localite,
               hebergement.heb_code_cgt,
               hebergement.heb_cgt_cap_min,
               hebergement.heb_cgt_cap_max,
               hebergement.heb_cgt_nbre_chmbre,
               hebergement.heb_etat,
               hebergement.heb_site_public,
               hebergement.heb_groupe,
               hebergement.heb_gdw,
               hebergement.heb_nbre_epis,
               hebergement.heb_descriptif_fr,
               hebergement.heb_descriptif_uk,
               hebergement.heb_descriptif_nl,
               hebergement.heb_descriptif_de,
               hebergement.heb_descriptif_it,
               hebergement.heb_pointfort_fr,
               hebergement.heb_pointfort_uk,
               hebergement.heb_pointfort_nl,
               hebergement.heb_pointfort_de,
               hebergement.heb_pointfort_it,
               hebergement.heb_equipement_fr,
               hebergement.heb_equipement_uk,
               hebergement.heb_equipement_nl,
               hebergement.heb_equipement_de,
               hebergement.heb_equipement_it,
               hebergement.heb_photo,
               hebergement.heb_com_fk,
               hebergement.heb_cgt_fk,
               hebergement.heb_typeheb_fk,
               hebergement.heb_pro_fk,
               hebergement.heb_theme_fk,
               hebergement.heb_label_fk,
               hebergement.heb_tenis_distance,
               hebergement.heb_nautisme_distance,
               hebergement.heb_sky_distance,
               hebergement.heb_rando_distance,
               hebergement.heb_piscine_distance,
               hebergement.heb_peche_distance,
               hebergement.heb_equitation_distance,
               hebergement.heb_velo_distance,
               hebergement.heb_vtt_distance,
               hebergement.heb_ravel_distance,
               hebergement.heb_lit_1p,
               hebergement.heb_lit_2p,
               hebergement.heb_lit_sup,
               hebergement.heb_lit_enf,
               hebergement.heb_distribution_fr,
               hebergement.heb_distribution_nl,
               hebergement.heb_distribution_it,
               hebergement.heb_distribution_uk,
               hebergement.heb_distribution_de,
               hebergement.heb_gare_distance,
               hebergement.heb_restaurant_distance,
               hebergement.heb_commerce_distance,
               hebergement.heb_coordonnee,
               hebergement.heb_charge_fk,
               hebergement.heb_gps_long,
               hebergement.heb_gps_lat,
               hebergement.heb_maison_tourisme_fk,
               hebergement.heb_id,
               hebergement.heb_ecr_date_ouverture,
               hebergement.heb_ecr_remarque,
               hebergement.heb_seminaire_vert_fr,
               hebergement.heb_seminaire_vert_nl,
               hebergement.heb_seminaire_vert_uk,
               hebergement.heb_seminaire_vert_de,
               hebergement.heb_seminaire_vert_it,
               hebergement.heb_calendrier_proprio,
               hebergement.heb_maj_info_etat,
               hebergement.heb_calendrier_proprio_date_maj,
               hebergement.heb_date_creation,
               hebergement.heb_date_modification,
               hebergement.heb_employe_modification,
               hebergement.heb_employe_creation,
               hebergement.heb_location,
               hebergement.heb_groupement_pk,
               hebergement.heb_desactivation_alloch,
               hebergement.heb_url,
               hebergement.heb_commercialisation_actif,
               hebergement.heb_commercialisation_id,
               CASE heb_tenis.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_tenis,
               CASE heb_nautisme.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_nautisme,
               CASE heb_sky.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_sky,
               CASE heb_rando.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_rando,
               CASE heb_piscine.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_piscine,
               CASE heb_peche.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_peche,
               CASE heb_equitation.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_equitation,
               CASE heb_velo.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_velo,
               CASE heb_vtt.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_vtt,
               CASE heb_ravel.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_ravel,
               CASE heb_animal.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_animal,
               CASE heb_fumeur.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_fumeur,
               CASE heb_confort_tv.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_tv,
               CASE heb_confort_feu_ouvert.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_feu_ouvert,
               CASE heb_confort_lave_vaiselle.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_lave_vaiselle,
               CASE heb_confort_micro_onde.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_micro_onde,
               CASE heb_confort_lave_linge.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_lave_linge,
               CASE heb_confort_seche_linge.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_seche_linge,
               CASE heb_confort_internet.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_internet,
               CASE heb_confort_terrasse.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_terrasse,
               CASE heb_confort_jardin.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_jardin,
               CASE heb_confort_sauna.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_sauna,
               CASE heb_confort_jacuzzi.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_jacuzzi,
               CASE heb_seminaire_vert.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_seminaire_vert,
               CASE heb_gid_bebe_tendresse.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_bebe_tendresse,
               CASE heb_gid_access_tous.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_access_tous,
               CASE heb_gid_antiallergique.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_antiallergique,
               CASE heb_gid_beau_jardin.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_beau_jardin,
               CASE heb_gid_eco_gite.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_eco_gite,
               CASE heb_gid_activite_nature.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_activite_nature,
               CASE heb_gid_panda.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_panda,
               CASE heb_gid_theme_equestre.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_theme_equestre,
               CASE heb_gid_peche.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_peche,
               CASE heb_gid_patrimoine.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_patrimoine,
               CASE heb_confort_congelateur.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_congelateur,
               CASE heb_commerce.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_commerce,
               CASE heb_restaurant.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_restaurant,
               CASE heb_gare.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gare,
               CASE heb_confort_projecteur.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_projecteur,
               CASE heb_confort_flipchart.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_flipchart,
               CASE heb_confort_ecran.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_ecran,
               CASE heb_tabhot_gourmand.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_tabhot_gourmand,
               CASE heb_tabhot_repas_familial.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_tabhot_repas_familial,
               CASE heb_tabhot_gastronomique.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_tabhot_gastronomique,
               CASE heb_bienvenu_velo.link_met_value WHEN true THEN 'oui' ELSE 'non' END as heb_bienvenu_velo,
               CASE heb_wallonie_qualite.link_met_value WHEN true THEN 'oui' ELSE 'non' END as heb_wallonie_qualite,
               CASE
                    WHEN heb_tarif_we_bs.max is null THEN coalesce(CAST(heb_tarif_we_bs.min AS TEXT), '0')
                    ELSE heb_tarif_we_bs.min || '/' || heb_tarif_we_bs.max
               END AS heb_tarif_we_bs,
               CASE
                    WHEN heb_tarif_sem_bs.max is null THEN coalesce(CAST(heb_tarif_sem_bs.min AS TEXT), '0')
                    ELSE heb_tarif_sem_bs.min || '/' || heb_tarif_sem_bs.max
               END AS heb_tarif_sem_bs,
               CASE
                    WHEN heb_tarif_we_ms.max is null THEN coalesce(CAST(heb_tarif_we_ms.min AS TEXT), '0')
                    ELSE heb_tarif_we_ms.min || '/' || heb_tarif_we_ms.max
               END AS heb_tarif_we_ms,
               CASE
                    WHEN heb_tarif_sem_ms.max is null THEN coalesce(CAST(heb_tarif_sem_ms.min AS TEXT), '0')
                    ELSE heb_tarif_sem_ms.min || '/' || heb_tarif_sem_ms.max
               END AS heb_tarif_sem_ms,
               CASE
                    WHEN heb_tarif_we_hs.max is null THEN coalesce(CAST(heb_tarif_we_hs.min AS TEXT), '0')
                    ELSE heb_tarif_we_hs.min || '/' || heb_tarif_we_hs.max
               END AS heb_tarif_we_hs,
               CASE
                    WHEN heb_tarif_sem_hs.max is null THEN coalesce(CAST(heb_tarif_sem_hs.min AS TEXT), '0')
                    ELSE heb_tarif_sem_hs.min || '/' || heb_tarif_sem_hs.max
               END AS heb_tarif_sem_hs,
               CASE
                    WHEN heb_tarif_we_3n.max is null THEN coalesce(CAST(heb_tarif_we_3n.min AS TEXT), '0')
                    ELSE heb_tarif_we_3n.min || '/' || heb_tarif_we_3n.max
               END AS heb_tarif_we_3n,
               CASE
                    WHEN heb_tarif_we_4n.max is null THEN coalesce(CAST(heb_tarif_we_4n.min AS TEXT), '0')
                    ELSE heb_tarif_we_4n.min || '/' || heb_tarif_we_4n.max
               END AS heb_tarif_we_4n,
               CASE
                    WHEN heb_tarif_semaine_fin_annee.max is null THEN coalesce(CAST(heb_tarif_semaine_fin_annee.min AS TEXT), '0')
                    ELSE heb_tarif_semaine_fin_annee.min || '/' || heb_tarif_semaine_fin_annee.max
               END AS heb_tarif_semaine_fin_annee,
               coalesce(heb_tarif_garantie.min, 0) as heb_tarif_garantie,
               CASE
                    WHEN heb_taxe_montant.min is null THEN ''
                    ELSE heb_taxe_montant.min || ' ' || heb_taxe_montant.cmt
               END AS heb_taxe_montant,
               heb_tarif_divers.cmt as heb_tarif_divers,
               coalesce(heb_tarif_chmbr_avec_dej_1p.min, 0) as heb_tarif_chmbr_avec_dej_1p,
               coalesce(heb_tarif_chmbr_avec_dej_2p.min, 0) as heb_tarif_chmbr_avec_dej_2p,
               CASE
                    WHEN heb_tarif_chmbr_avec_dej_2p.min is not null AND heb_tarif_chmbr_pers_sup.min is not null
                    THEN heb_tarif_chmbr_avec_dej_2p.min + heb_tarif_chmbr_pers_sup.min
                    ELSE '0'
               END AS heb_tarif_chmbr_avec_dej_3p,
               heb_tarif_divers.cmt AS heb_tarif_chmbr_autre_1p,
               coalesce(heb_tarif_chmbr_table_hote_1p.min, 0) AS heb_tarif_chmbr_table_hote_1p,
               provinces.prov_nom,
               provinces.prov_code
        FROM hebergement
        LEFT OUTER JOIN tarifs_view AS heb_tarif_we_bs
                     ON hebergement.heb_pk = heb_tarif_we_bs.heb_pk
                    AND heb_tarif_we_bs.type = 'LOW_SEASON'
                    AND heb_tarif_we_bs.subtype = 'WEEKEND'
                    AND heb_tarif_we_bs.valid = True
        LEFT OUTER JOIN tarifs_view as heb_tarif_sem_bs
                     ON hebergement.heb_pk = heb_tarif_sem_bs.heb_pk
                    AND heb_tarif_sem_bs.type = 'LOW_SEASON'
                    AND heb_tarif_sem_bs.subtype = 'WEEK'
                    AND heb_tarif_sem_bs.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_we_ms
                     ON hebergement.heb_pk = heb_tarif_we_ms.heb_pk
                    AND heb_tarif_we_ms.type = 'MEDIUM_SEASON'
                    AND heb_tarif_we_ms.subtype = 'WEEKEND'
                    AND heb_tarif_we_ms.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_sem_ms
                     ON hebergement.heb_pk = heb_tarif_sem_ms.heb_pk
                    AND heb_tarif_sem_ms.type = 'MEDIUM_SEASON'
                    AND heb_tarif_sem_ms.subtype = 'WEEK'
                    AND heb_tarif_sem_ms.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_we_hs
                     ON hebergement.heb_pk = heb_tarif_we_hs.heb_pk
                    AND heb_tarif_we_hs.type = 'HIGH_SEASON'
                    AND heb_tarif_we_hs.subtype = 'WEEKEND'
                    AND heb_tarif_we_hs.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_sem_hs
                     ON hebergement.heb_pk = heb_tarif_sem_hs.heb_pk
                    AND heb_tarif_sem_hs.type = 'HIGH_SEASON'
                    AND heb_tarif_sem_hs.subtype = 'WEEK'
                    AND heb_tarif_sem_hs.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_we_3n
                     ON hebergement.heb_pk = heb_tarif_we_3n.heb_pk
                    AND heb_tarif_we_3n.type = 'FEAST_WEEKEND'
                    AND heb_tarif_we_3n.subtype = '3_NIGHTS'
                    AND heb_tarif_we_3n.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_we_4n
                     ON hebergement.heb_pk = heb_tarif_we_4n.heb_pk
                    AND heb_tarif_we_4n.type = 'FEAST_WEEKEND'
                    AND heb_tarif_we_4n.subtype = '4_NIGHTS'
                    AND heb_tarif_we_4n.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_semaine_fin_annee
                     ON hebergement.heb_pk = heb_tarif_semaine_fin_annee.heb_pk
                    AND heb_tarif_semaine_fin_annee.type = 'OTHER'
                    AND heb_tarif_semaine_fin_annee.subtype = 'END_OF_YEAR'
                    AND heb_tarif_semaine_fin_annee.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_garantie
                     ON hebergement.heb_pk = heb_tarif_garantie.heb_pk
                    AND heb_tarif_garantie.type = 'OTHER'
                    AND heb_tarif_garantie.subtype = 'GUARANTEE'
                    AND heb_tarif_garantie.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_taxe_montant
                     ON hebergement.heb_pk = heb_taxe_montant.heb_pk
                    AND heb_taxe_montant.type = 'OTHER'
                    AND heb_taxe_montant.subtype = 'SOJOURN_TAX'
                    AND heb_taxe_montant.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_divers
                     ON hebergement.heb_pk = heb_tarif_divers.heb_pk
                    AND heb_tarif_divers.type = 'OTHER'
                    AND heb_tarif_divers.subtype = 'OTHER_CLEAN'
                    AND heb_tarif_divers.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_chmbr_avec_dej_1p
                     ON hebergement.heb_pk = heb_tarif_chmbr_avec_dej_1p.heb_pk
                    AND heb_tarif_chmbr_avec_dej_1p.type = 'ROOM'
                    AND heb_tarif_chmbr_avec_dej_1p.subtype = '1_PERSON'
                    AND heb_tarif_chmbr_avec_dej_1p.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_chmbr_avec_dej_2p
                     ON hebergement.heb_pk = heb_tarif_chmbr_avec_dej_2p.heb_pk
                    AND heb_tarif_chmbr_avec_dej_2p.type = 'ROOM'
                    AND heb_tarif_chmbr_avec_dej_2p.subtype = '2_PERSONS'
                    AND heb_tarif_chmbr_avec_dej_2p.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_chmbr_pers_sup
                     ON hebergement.heb_pk = heb_tarif_chmbr_pers_sup.heb_pk
                    AND heb_tarif_chmbr_pers_sup.type = 'ROOM'
                    AND heb_tarif_chmbr_pers_sup.subtype = 'PERSON_SUP'
                    AND heb_tarif_chmbr_pers_sup.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_chmbr_sans_dej
                     ON hebergement.heb_pk = heb_tarif_chmbr_sans_dej.heb_pk
                    AND heb_tarif_chmbr_sans_dej.type = 'OTHER'
                    AND heb_tarif_chmbr_sans_dej.subtype = 'WITHOUT_BREAKFAST'
                    AND heb_tarif_chmbr_sans_dej.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_chmbr_table_hote_1p
                     ON hebergement.heb_pk = heb_tarif_chmbr_table_hote_1p.heb_pk
                    AND heb_tarif_chmbr_table_hote_1p.type = 'OTHER'
                    AND heb_tarif_chmbr_table_hote_1p.subtype = 'TABLE_HOTES'
                    AND heb_tarif_chmbr_table_hote_1p.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_charge
                     ON hebergement.heb_pk = heb_tarif_charge.heb_pk
                    AND heb_tarif_charge.type = 'CHARGES'
                    AND heb_tarif_charge.valid = True
        LEFT JOIN link_hebergement_metadata AS heb_tenis
               ON heb_tenis.heb_fk = hebergement.heb_pk AND heb_tenis.metadata_fk = 1
        LEFT JOIN link_hebergement_metadata AS heb_nautisme
               ON heb_nautisme.heb_fk = hebergement.heb_pk AND heb_nautisme.metadata_fk = 2
        LEFT JOIN link_hebergement_metadata AS heb_sky
               ON heb_sky.heb_fk = hebergement.heb_pk AND heb_sky.metadata_fk = 3
        LEFT JOIN link_hebergement_metadata AS heb_rando
               ON heb_rando.heb_fk = hebergement.heb_pk AND heb_rando.metadata_fk = 4
        LEFT JOIN link_hebergement_metadata AS heb_piscine
               ON heb_piscine.heb_fk = hebergement.heb_pk AND heb_piscine.metadata_fk = 5
        LEFT JOIN link_hebergement_metadata AS heb_peche
               ON heb_peche.heb_fk = hebergement.heb_pk AND heb_peche.metadata_fk = 6
        LEFT JOIN link_hebergement_metadata AS heb_equitation
               ON heb_equitation.heb_fk = hebergement.heb_pk AND heb_equitation.metadata_fk = 7
        LEFT JOIN link_hebergement_metadata AS heb_velo
               ON heb_velo.heb_fk = hebergement.heb_pk AND heb_velo.metadata_fk = 8
        LEFT JOIN link_hebergement_metadata AS heb_vtt
               ON heb_vtt.heb_fk = hebergement.heb_pk AND heb_vtt.metadata_fk = 9
        LEFT JOIN link_hebergement_metadata AS heb_ravel
               ON heb_ravel.heb_fk = hebergement.heb_pk AND heb_ravel.metadata_fk = 10
        LEFT JOIN link_hebergement_metadata AS heb_animal
               ON heb_animal.heb_fk = hebergement.heb_pk AND heb_animal.metadata_fk = 11
        LEFT JOIN link_hebergement_metadata AS heb_fumeur
               ON heb_fumeur.heb_fk = hebergement.heb_pk AND heb_fumeur.metadata_fk = 12
        LEFT JOIN link_hebergement_metadata AS heb_confort_tv
               ON heb_confort_tv.heb_fk = hebergement.heb_pk AND heb_confort_tv.metadata_fk = 13
        LEFT JOIN link_hebergement_metadata AS heb_confort_feu_ouvert
               ON heb_confort_feu_ouvert.heb_fk = hebergement.heb_pk AND heb_confort_feu_ouvert.metadata_fk = 14
        LEFT JOIN link_hebergement_metadata AS heb_confort_lave_vaiselle
               ON heb_confort_lave_vaiselle.heb_fk = hebergement.heb_pk AND heb_confort_lave_vaiselle.metadata_fk = 15
        LEFT JOIN link_hebergement_metadata AS heb_confort_micro_onde
               ON heb_confort_micro_onde.heb_fk = hebergement.heb_pk AND heb_confort_micro_onde.metadata_fk = 16
        LEFT JOIN link_hebergement_metadata AS heb_confort_lave_linge
               ON heb_confort_lave_linge.heb_fk = hebergement.heb_pk AND heb_confort_lave_linge.metadata_fk = 17
        LEFT JOIN link_hebergement_metadata AS heb_confort_seche_linge
               ON heb_confort_seche_linge.heb_fk = hebergement.heb_pk AND heb_confort_seche_linge.metadata_fk = 18
        LEFT JOIN link_hebergement_metadata AS heb_confort_internet
               ON heb_confort_internet.heb_fk = hebergement.heb_pk AND heb_confort_internet.metadata_fk = 19
        LEFT JOIN link_hebergement_metadata AS heb_confort_terrasse
               ON heb_confort_terrasse.heb_fk = hebergement.heb_pk AND heb_confort_terrasse.metadata_fk = 20
        LEFT JOIN link_hebergement_metadata AS heb_confort_jardin
               ON heb_confort_jardin.heb_fk = hebergement.heb_pk AND heb_confort_jardin.metadata_fk = 21
        LEFT JOIN link_hebergement_metadata AS heb_confort_sauna
               ON heb_confort_sauna.heb_fk = hebergement.heb_pk AND heb_confort_sauna.metadata_fk = 22
        LEFT JOIN link_hebergement_metadata AS heb_confort_jacuzzi
               ON heb_confort_jacuzzi.heb_fk = hebergement.heb_pk AND heb_confort_jacuzzi.metadata_fk = 23
        LEFT JOIN link_hebergement_metadata AS heb_seminaire_vert
               ON heb_seminaire_vert.heb_fk = hebergement.heb_pk AND heb_seminaire_vert.metadata_fk = 24
        LEFT JOIN link_hebergement_metadata AS heb_gid_bebe_tendresse
               ON heb_gid_bebe_tendresse.heb_fk = hebergement.heb_pk AND heb_gid_bebe_tendresse.metadata_fk = 25
        LEFT JOIN link_hebergement_metadata AS heb_gid_access_tous
               ON heb_gid_access_tous.heb_fk = hebergement.heb_pk AND heb_gid_access_tous.metadata_fk = 26
        LEFT JOIN link_hebergement_metadata AS heb_gid_antiallergique
               ON heb_gid_antiallergique.heb_fk = hebergement.heb_pk AND heb_gid_antiallergique.metadata_fk = 27
        LEFT JOIN link_hebergement_metadata AS heb_gid_beau_jardin
               ON heb_gid_beau_jardin.heb_fk = hebergement.heb_pk AND heb_gid_beau_jardin.metadata_fk = 28
        LEFT JOIN link_hebergement_metadata AS heb_gid_eco_gite
               ON heb_gid_eco_gite.heb_fk = hebergement.heb_pk AND heb_gid_eco_gite.metadata_fk = 29
        LEFT JOIN link_hebergement_metadata AS heb_gid_activite_nature
               ON heb_gid_activite_nature.heb_fk = hebergement.heb_pk AND heb_gid_activite_nature.metadata_fk = 30
        LEFT JOIN link_hebergement_metadata AS heb_gid_panda
               ON heb_gid_panda.heb_fk = hebergement.heb_pk AND heb_gid_panda.metadata_fk = 31
        LEFT JOIN link_hebergement_metadata AS heb_gid_theme_equestre
               ON heb_gid_theme_equestre.heb_fk = hebergement.heb_pk AND heb_gid_theme_equestre.metadata_fk = 32
        LEFT JOIN link_hebergement_metadata AS heb_gid_peche
               ON heb_gid_peche.heb_fk = hebergement.heb_pk AND heb_gid_peche.metadata_fk = 33
        LEFT JOIN link_hebergement_metadata AS heb_gid_patrimoine
               ON heb_gid_patrimoine.heb_fk = hebergement.heb_pk AND heb_gid_patrimoine.metadata_fk = 34
        LEFT JOIN link_hebergement_metadata AS heb_confort_congelateur
               ON heb_confort_congelateur.heb_fk = hebergement.heb_pk AND heb_confort_congelateur.metadata_fk = 35
        LEFT JOIN link_hebergement_metadata AS heb_commerce
               ON heb_commerce.heb_fk = hebergement.heb_pk AND heb_commerce.metadata_fk = 36
        LEFT JOIN link_hebergement_metadata AS heb_restaurant
               ON heb_restaurant.heb_fk = hebergement.heb_pk AND heb_restaurant.metadata_fk = 37
        LEFT JOIN link_hebergement_metadata AS heb_gare
               ON heb_gare.heb_fk = hebergement.heb_pk AND heb_gare.metadata_fk = 38
        LEFT JOIN link_hebergement_metadata AS heb_confort_projecteur
               ON heb_confort_projecteur.heb_fk = hebergement.heb_pk AND heb_confort_projecteur.metadata_fk = 39
        LEFT JOIN link_hebergement_metadata AS heb_confort_flipchart
               ON heb_confort_flipchart.heb_fk = hebergement.heb_pk AND heb_confort_flipchart.metadata_fk = 40
        LEFT JOIN link_hebergement_metadata AS heb_confort_ecran
               ON heb_confort_ecran.heb_fk = hebergement.heb_pk AND heb_confort_ecran.metadata_fk = 41
        LEFT JOIN link_hebergement_metadata AS heb_tabhot_gourmand
               ON heb_tabhot_gourmand.heb_fk = hebergement.heb_pk AND heb_tabhot_gourmand.metadata_fk = 42
        LEFT JOIN link_hebergement_metadata AS heb_tabhot_repas_familial
               ON heb_tabhot_repas_familial.heb_fk = hebergement.heb_pk AND heb_tabhot_repas_familial.metadata_fk = 43
        LEFT JOIN link_hebergement_metadata AS heb_tabhot_gastronomique
               ON heb_tabhot_gastronomique.heb_fk = hebergement.heb_pk AND heb_tabhot_gastronomique.metadata_fk = 44
        LEFT JOIN link_hebergement_metadata AS heb_bienvenu_velo
               ON heb_bienvenu_velo.heb_fk = hebergement.heb_pk AND heb_bienvenu_velo.metadata_fk = 47
        LEFT JOIN link_hebergement_metadata AS heb_wallonie_qualite
               ON heb_wallonie_qualite.heb_fk = hebergement.heb_pk AND heb_wallonie_qualite.metadata_fk = 63
        LEFT JOIN commune
               ON hebergement.heb_com_fk = commune.com_pk
        LEFT JOIN provinces
               ON commune.com_prov_fk = provinces.prov_pk
    ''')


def downgrade():
    op.execute('DROP VIEW hebergement_view')
    op.execute('''
        CREATE VIEW hebergement_view AS
        SELECT hebergement.heb_pk,
               hebergement.heb_code_gdw,
               hebergement.heb_nom,
               hebergement.heb_adresse,
               hebergement.heb_localite,
               hebergement.heb_code_cgt,
               hebergement.heb_cgt_cap_min,
               hebergement.heb_cgt_cap_max,
               hebergement.heb_cgt_nbre_chmbre,
               hebergement.heb_etat,
               hebergement.heb_site_public,
               hebergement.heb_groupe,
               hebergement.heb_gdw,
               hebergement.heb_nbre_epis,
               hebergement.heb_descriptif_fr,
               hebergement.heb_descriptif_uk,
               hebergement.heb_descriptif_nl,
               hebergement.heb_descriptif_de,
               hebergement.heb_descriptif_it,
               hebergement.heb_pointfort_fr,
               hebergement.heb_pointfort_uk,
               hebergement.heb_pointfort_nl,
               hebergement.heb_pointfort_de,
               hebergement.heb_pointfort_it,
               hebergement.heb_equipement_fr,
               hebergement.heb_equipement_uk,
               hebergement.heb_equipement_nl,
               hebergement.heb_equipement_de,
               hebergement.heb_equipement_it,
               hebergement.heb_photo,
               hebergement.heb_com_fk,
               hebergement.heb_cgt_fk,
               hebergement.heb_typeheb_fk,
               hebergement.heb_pro_fk,
               hebergement.heb_theme_fk,
               hebergement.heb_label_fk,
               hebergement.heb_tenis_distance,
               hebergement.heb_nautisme_distance,
               hebergement.heb_sky_distance,
               hebergement.heb_rando_distance,
               hebergement.heb_piscine_distance,
               hebergement.heb_peche_distance,
               hebergement.heb_equitation_distance,
               hebergement.heb_velo_distance,
               hebergement.heb_vtt_distance,
               hebergement.heb_ravel_distance,
               hebergement.heb_lit_1p,
               hebergement.heb_lit_2p,
               hebergement.heb_lit_sup,
               hebergement.heb_lit_enf,
               hebergement.heb_distribution_fr,
               hebergement.heb_distribution_nl,
               hebergement.heb_distribution_it,
               hebergement.heb_distribution_uk,
               hebergement.heb_distribution_de,
               hebergement.heb_gare_distance,
               hebergement.heb_restaurant_distance,
               hebergement.heb_commerce_distance,
               hebergement.heb_coordonnee,
               hebergement.heb_charge_fk,
               hebergement.heb_gps_long,
               hebergement.heb_gps_lat,
               hebergement.heb_maison_tourisme_fk,
               hebergement.heb_id,
               hebergement.heb_ecr_date_ouverture,
               hebergement.heb_ecr_remarque,
               hebergement.heb_seminaire_vert_fr,
               hebergement.heb_seminaire_vert_nl,
               hebergement.heb_seminaire_vert_uk,
               hebergement.heb_seminaire_vert_de,
               hebergement.heb_seminaire_vert_it,
               hebergement.heb_calendrier_proprio,
               hebergement.heb_maj_info_etat,
               hebergement.heb_calendrier_proprio_date_maj,
               hebergement.heb_date_creation,
               hebergement.heb_date_modification,
               hebergement.heb_employe_modification,
               hebergement.heb_employe_creation,
               hebergement.heb_location,
               hebergement.heb_groupement_pk,
               hebergement.heb_desactivation_alloch,
               hebergement.heb_url,
               CASE heb_tenis.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_tenis,
               CASE heb_nautisme.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_nautisme,
               CASE heb_sky.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_sky,
               CASE heb_rando.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_rando,
               CASE heb_piscine.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_piscine,
               CASE heb_peche.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_peche,
               CASE heb_equitation.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_equitation,
               CASE heb_velo.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_velo,
               CASE heb_vtt.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_vtt,
               CASE heb_ravel.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_ravel,
               CASE heb_animal.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_animal,
               CASE heb_fumeur.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_fumeur,
               CASE heb_confort_tv.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_tv,
               CASE heb_confort_feu_ouvert.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_feu_ouvert,
               CASE heb_confort_lave_vaiselle.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_lave_vaiselle,
               CASE heb_confort_micro_onde.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_micro_onde,
               CASE heb_confort_lave_linge.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_lave_linge,
               CASE heb_confort_seche_linge.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_seche_linge,
               CASE heb_confort_internet.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_internet,
               CASE heb_confort_terrasse.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_terrasse,
               CASE heb_confort_jardin.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_jardin,
               CASE heb_confort_sauna.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_sauna,
               CASE heb_confort_jacuzzi.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_jacuzzi,
               CASE heb_seminaire_vert.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_seminaire_vert,
               CASE heb_gid_bebe_tendresse.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_bebe_tendresse,
               CASE heb_gid_access_tous.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_access_tous,
               CASE heb_gid_antiallergique.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_antiallergique,
               CASE heb_gid_beau_jardin.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_beau_jardin,
               CASE heb_gid_eco_gite.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_eco_gite,
               CASE heb_gid_activite_nature.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_activite_nature,
               CASE heb_gid_panda.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_panda,
               CASE heb_gid_theme_equestre.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_theme_equestre,
               CASE heb_gid_peche.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_peche,
               CASE heb_gid_patrimoine.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gid_patrimoine,
               CASE heb_confort_congelateur.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_congelateur,
               CASE heb_commerce.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_commerce,
               CASE heb_restaurant.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_restaurant,
               CASE heb_gare.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_gare,
               CASE heb_confort_projecteur.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_projecteur,
               CASE heb_confort_flipchart.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_flipchart,
               CASE heb_confort_ecran.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_confort_ecran,
               CASE heb_tabhot_gourmand.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_tabhot_gourmand,
               CASE heb_tabhot_repas_familial.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_tabhot_repas_familial,
               CASE heb_tabhot_gastronomique.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_tabhot_gastronomique,
               CASE heb_bienvenu_velo.link_met_value WHEN true THEN 'oui' ELSE 'non' END as heb_bienvenu_velo,
               CASE heb_wallonie_qualite.link_met_value WHEN true THEN 'oui' ELSE 'non' END as heb_wallonie_qualite,
               CASE
                    WHEN heb_tarif_we_bs.max is null THEN coalesce(CAST(heb_tarif_we_bs.min AS TEXT), '0')
                    ELSE heb_tarif_we_bs.min || '/' || heb_tarif_we_bs.max
               END AS heb_tarif_we_bs,
               CASE
                    WHEN heb_tarif_sem_bs.max is null THEN coalesce(CAST(heb_tarif_sem_bs.min AS TEXT), '0')
                    ELSE heb_tarif_sem_bs.min || '/' || heb_tarif_sem_bs.max
               END AS heb_tarif_sem_bs,
               CASE
                    WHEN heb_tarif_we_ms.max is null THEN coalesce(CAST(heb_tarif_we_ms.min AS TEXT), '0')
                    ELSE heb_tarif_we_ms.min || '/' || heb_tarif_we_ms.max
               END AS heb_tarif_we_ms,
               CASE
                    WHEN heb_tarif_sem_ms.max is null THEN coalesce(CAST(heb_tarif_sem_ms.min AS TEXT), '0')
                    ELSE heb_tarif_sem_ms.min || '/' || heb_tarif_sem_ms.max
               END AS heb_tarif_sem_ms,
               CASE
                    WHEN heb_tarif_we_hs.max is null THEN coalesce(CAST(heb_tarif_we_hs.min AS TEXT), '0')
                    ELSE heb_tarif_we_hs.min || '/' || heb_tarif_we_hs.max
               END AS heb_tarif_we_hs,
               CASE
                    WHEN heb_tarif_sem_hs.max is null THEN coalesce(CAST(heb_tarif_sem_hs.min AS TEXT), '0')
                    ELSE heb_tarif_sem_hs.min || '/' || heb_tarif_sem_hs.max
               END AS heb_tarif_sem_hs,
               CASE
                    WHEN heb_tarif_we_3n.max is null THEN coalesce(CAST(heb_tarif_we_3n.min AS TEXT), '0')
                    ELSE heb_tarif_we_3n.min || '/' || heb_tarif_we_3n.max
               END AS heb_tarif_we_3n,
               CASE
                    WHEN heb_tarif_we_4n.max is null THEN coalesce(CAST(heb_tarif_we_4n.min AS TEXT), '0')
                    ELSE heb_tarif_we_4n.min || '/' || heb_tarif_we_4n.max
               END AS heb_tarif_we_4n,
               CASE
                    WHEN heb_tarif_semaine_fin_annee.max is null THEN coalesce(CAST(heb_tarif_semaine_fin_annee.min AS TEXT), '0')
                    ELSE heb_tarif_semaine_fin_annee.min || '/' || heb_tarif_semaine_fin_annee.max
               END AS heb_tarif_semaine_fin_annee,
               coalesce(heb_tarif_garantie.min, 0) as heb_tarif_garantie,
               CASE
                    WHEN heb_taxe_montant.min is null THEN ''
                    ELSE heb_taxe_montant.min || ' ' || heb_taxe_montant.cmt
               END AS heb_taxe_montant,
               heb_tarif_divers.cmt as heb_tarif_divers,
               coalesce(heb_tarif_chmbr_avec_dej_1p.min, 0) as heb_tarif_chmbr_avec_dej_1p,
               coalesce(heb_tarif_chmbr_avec_dej_2p.min, 0) as heb_tarif_chmbr_avec_dej_2p,
               CASE
                    WHEN heb_tarif_chmbr_avec_dej_2p.min is not null AND heb_tarif_chmbr_pers_sup.min is not null
                    THEN heb_tarif_chmbr_avec_dej_2p.min + heb_tarif_chmbr_pers_sup.min
                    ELSE '0'
               END AS heb_tarif_chmbr_avec_dej_3p,
               heb_tarif_divers.cmt AS heb_tarif_chmbr_autre_1p,
               coalesce(heb_tarif_chmbr_table_hote_1p.min, 0) AS heb_tarif_chmbr_table_hote_1p,
               provinces.prov_nom,
               provinces.prov_code
        FROM hebergement
        LEFT OUTER JOIN tarifs_view AS heb_tarif_we_bs
                     ON hebergement.heb_pk = heb_tarif_we_bs.heb_pk
                    AND heb_tarif_we_bs.type = 'LOW_SEASON'
                    AND heb_tarif_we_bs.subtype = 'WEEKEND'
                    AND heb_tarif_we_bs.valid = True
        LEFT OUTER JOIN tarifs_view as heb_tarif_sem_bs
                     ON hebergement.heb_pk = heb_tarif_sem_bs.heb_pk
                    AND heb_tarif_sem_bs.type = 'LOW_SEASON'
                    AND heb_tarif_sem_bs.subtype = 'WEEK'
                    AND heb_tarif_sem_bs.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_we_ms
                     ON hebergement.heb_pk = heb_tarif_we_ms.heb_pk
                    AND heb_tarif_we_ms.type = 'MEDIUM_SEASON'
                    AND heb_tarif_we_ms.subtype = 'WEEKEND'
                    AND heb_tarif_we_ms.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_sem_ms
                     ON hebergement.heb_pk = heb_tarif_sem_ms.heb_pk
                    AND heb_tarif_sem_ms.type = 'MEDIUM_SEASON'
                    AND heb_tarif_sem_ms.subtype = 'WEEK'
                    AND heb_tarif_sem_ms.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_we_hs
                     ON hebergement.heb_pk = heb_tarif_we_hs.heb_pk
                    AND heb_tarif_we_hs.type = 'HIGH_SEASON'
                    AND heb_tarif_we_hs.subtype = 'WEEKEND'
                    AND heb_tarif_we_hs.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_sem_hs
                     ON hebergement.heb_pk = heb_tarif_sem_hs.heb_pk
                    AND heb_tarif_sem_hs.type = 'HIGH_SEASON'
                    AND heb_tarif_sem_hs.subtype = 'WEEK'
                    AND heb_tarif_sem_hs.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_we_3n
                     ON hebergement.heb_pk = heb_tarif_we_3n.heb_pk
                    AND heb_tarif_we_3n.type = 'FEAST_WEEKEND'
                    AND heb_tarif_we_3n.subtype = '3_NIGHTS'
                    AND heb_tarif_we_3n.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_we_4n
                     ON hebergement.heb_pk = heb_tarif_we_4n.heb_pk
                    AND heb_tarif_we_4n.type = 'FEAST_WEEKEND'
                    AND heb_tarif_we_4n.subtype = '4_NIGHTS'
                    AND heb_tarif_we_4n.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_semaine_fin_annee
                     ON hebergement.heb_pk = heb_tarif_semaine_fin_annee.heb_pk
                    AND heb_tarif_semaine_fin_annee.type = 'OTHER'
                    AND heb_tarif_semaine_fin_annee.subtype = 'END_OF_YEAR'
                    AND heb_tarif_semaine_fin_annee.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_garantie
                     ON hebergement.heb_pk = heb_tarif_garantie.heb_pk
                    AND heb_tarif_garantie.type = 'OTHER'
                    AND heb_tarif_garantie.subtype = 'GUARANTEE'
                    AND heb_tarif_garantie.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_taxe_montant
                     ON hebergement.heb_pk = heb_taxe_montant.heb_pk
                    AND heb_taxe_montant.type = 'OTHER'
                    AND heb_taxe_montant.subtype = 'SOJOURN_TAX'
                    AND heb_taxe_montant.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_divers
                     ON hebergement.heb_pk = heb_tarif_divers.heb_pk
                    AND heb_tarif_divers.type = 'OTHER'
                    AND heb_tarif_divers.subtype = 'OTHER_CLEAN'
                    AND heb_tarif_divers.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_chmbr_avec_dej_1p
                     ON hebergement.heb_pk = heb_tarif_chmbr_avec_dej_1p.heb_pk
                    AND heb_tarif_chmbr_avec_dej_1p.type = 'ROOM'
                    AND heb_tarif_chmbr_avec_dej_1p.subtype = '1_PERSON'
                    AND heb_tarif_chmbr_avec_dej_1p.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_chmbr_avec_dej_2p
                     ON hebergement.heb_pk = heb_tarif_chmbr_avec_dej_2p.heb_pk
                    AND heb_tarif_chmbr_avec_dej_2p.type = 'ROOM'
                    AND heb_tarif_chmbr_avec_dej_2p.subtype = '2_PERSONS'
                    AND heb_tarif_chmbr_avec_dej_2p.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_chmbr_pers_sup
                     ON hebergement.heb_pk = heb_tarif_chmbr_pers_sup.heb_pk
                    AND heb_tarif_chmbr_pers_sup.type = 'ROOM'
                    AND heb_tarif_chmbr_pers_sup.subtype = 'PERSON_SUP'
                    AND heb_tarif_chmbr_pers_sup.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_chmbr_sans_dej
                     ON hebergement.heb_pk = heb_tarif_chmbr_sans_dej.heb_pk
                    AND heb_tarif_chmbr_sans_dej.type = 'OTHER'
                    AND heb_tarif_chmbr_sans_dej.subtype = 'WITHOUT_BREAKFAST'
                    AND heb_tarif_chmbr_sans_dej.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_chmbr_table_hote_1p
                     ON hebergement.heb_pk = heb_tarif_chmbr_table_hote_1p.heb_pk
                    AND heb_tarif_chmbr_table_hote_1p.type = 'OTHER'
                    AND heb_tarif_chmbr_table_hote_1p.subtype = 'TABLE_HOTES'
                    AND heb_tarif_chmbr_table_hote_1p.valid = True
        LEFT OUTER JOIN tarifs_view AS heb_tarif_charge
                     ON hebergement.heb_pk = heb_tarif_charge.heb_pk
                    AND heb_tarif_charge.type = 'CHARGES'
                    AND heb_tarif_charge.valid = True
        LEFT JOIN link_hebergement_metadata AS heb_tenis
               ON heb_tenis.heb_fk = hebergement.heb_pk AND heb_tenis.metadata_fk = 1
        LEFT JOIN link_hebergement_metadata AS heb_nautisme
               ON heb_nautisme.heb_fk = hebergement.heb_pk AND heb_nautisme.metadata_fk = 2
        LEFT JOIN link_hebergement_metadata AS heb_sky
               ON heb_sky.heb_fk = hebergement.heb_pk AND heb_sky.metadata_fk = 3
        LEFT JOIN link_hebergement_metadata AS heb_rando
               ON heb_rando.heb_fk = hebergement.heb_pk AND heb_rando.metadata_fk = 4
        LEFT JOIN link_hebergement_metadata AS heb_piscine
               ON heb_piscine.heb_fk = hebergement.heb_pk AND heb_piscine.metadata_fk = 5
        LEFT JOIN link_hebergement_metadata AS heb_peche
               ON heb_peche.heb_fk = hebergement.heb_pk AND heb_peche.metadata_fk = 6
        LEFT JOIN link_hebergement_metadata AS heb_equitation
               ON heb_equitation.heb_fk = hebergement.heb_pk AND heb_equitation.metadata_fk = 7
        LEFT JOIN link_hebergement_metadata AS heb_velo
               ON heb_velo.heb_fk = hebergement.heb_pk AND heb_velo.metadata_fk = 8
        LEFT JOIN link_hebergement_metadata AS heb_vtt
               ON heb_vtt.heb_fk = hebergement.heb_pk AND heb_vtt.metadata_fk = 9
        LEFT JOIN link_hebergement_metadata AS heb_ravel
               ON heb_ravel.heb_fk = hebergement.heb_pk AND heb_ravel.metadata_fk = 10
        LEFT JOIN link_hebergement_metadata AS heb_animal
               ON heb_animal.heb_fk = hebergement.heb_pk AND heb_animal.metadata_fk = 11
        LEFT JOIN link_hebergement_metadata AS heb_fumeur
               ON heb_fumeur.heb_fk = hebergement.heb_pk AND heb_fumeur.metadata_fk = 12
        LEFT JOIN link_hebergement_metadata AS heb_confort_tv
               ON heb_confort_tv.heb_fk = hebergement.heb_pk AND heb_confort_tv.metadata_fk = 13
        LEFT JOIN link_hebergement_metadata AS heb_confort_feu_ouvert
               ON heb_confort_feu_ouvert.heb_fk = hebergement.heb_pk AND heb_confort_feu_ouvert.metadata_fk = 14
        LEFT JOIN link_hebergement_metadata AS heb_confort_lave_vaiselle
               ON heb_confort_lave_vaiselle.heb_fk = hebergement.heb_pk AND heb_confort_lave_vaiselle.metadata_fk = 15
        LEFT JOIN link_hebergement_metadata AS heb_confort_micro_onde
               ON heb_confort_micro_onde.heb_fk = hebergement.heb_pk AND heb_confort_micro_onde.metadata_fk = 16
        LEFT JOIN link_hebergement_metadata AS heb_confort_lave_linge
               ON heb_confort_lave_linge.heb_fk = hebergement.heb_pk AND heb_confort_lave_linge.metadata_fk = 17
        LEFT JOIN link_hebergement_metadata AS heb_confort_seche_linge
               ON heb_confort_seche_linge.heb_fk = hebergement.heb_pk AND heb_confort_seche_linge.metadata_fk = 18
        LEFT JOIN link_hebergement_metadata AS heb_confort_internet
               ON heb_confort_internet.heb_fk = hebergement.heb_pk AND heb_confort_internet.metadata_fk = 19
        LEFT JOIN link_hebergement_metadata AS heb_confort_terrasse
               ON heb_confort_terrasse.heb_fk = hebergement.heb_pk AND heb_confort_terrasse.metadata_fk = 20
        LEFT JOIN link_hebergement_metadata AS heb_confort_jardin
               ON heb_confort_jardin.heb_fk = hebergement.heb_pk AND heb_confort_jardin.metadata_fk = 21
        LEFT JOIN link_hebergement_metadata AS heb_confort_sauna
               ON heb_confort_sauna.heb_fk = hebergement.heb_pk AND heb_confort_sauna.metadata_fk = 22
        LEFT JOIN link_hebergement_metadata AS heb_confort_jacuzzi
               ON heb_confort_jacuzzi.heb_fk = hebergement.heb_pk AND heb_confort_jacuzzi.metadata_fk = 23
        LEFT JOIN link_hebergement_metadata AS heb_seminaire_vert
               ON heb_seminaire_vert.heb_fk = hebergement.heb_pk AND heb_seminaire_vert.metadata_fk = 24
        LEFT JOIN link_hebergement_metadata AS heb_gid_bebe_tendresse
               ON heb_gid_bebe_tendresse.heb_fk = hebergement.heb_pk AND heb_gid_bebe_tendresse.metadata_fk = 25
        LEFT JOIN link_hebergement_metadata AS heb_gid_access_tous
               ON heb_gid_access_tous.heb_fk = hebergement.heb_pk AND heb_gid_access_tous.metadata_fk = 26
        LEFT JOIN link_hebergement_metadata AS heb_gid_antiallergique
               ON heb_gid_antiallergique.heb_fk = hebergement.heb_pk AND heb_gid_antiallergique.metadata_fk = 27
        LEFT JOIN link_hebergement_metadata AS heb_gid_beau_jardin
               ON heb_gid_beau_jardin.heb_fk = hebergement.heb_pk AND heb_gid_beau_jardin.metadata_fk = 28
        LEFT JOIN link_hebergement_metadata AS heb_gid_eco_gite
               ON heb_gid_eco_gite.heb_fk = hebergement.heb_pk AND heb_gid_eco_gite.metadata_fk = 29
        LEFT JOIN link_hebergement_metadata AS heb_gid_activite_nature
               ON heb_gid_activite_nature.heb_fk = hebergement.heb_pk AND heb_gid_activite_nature.metadata_fk = 30
        LEFT JOIN link_hebergement_metadata AS heb_gid_panda
               ON heb_gid_panda.heb_fk = hebergement.heb_pk AND heb_gid_panda.metadata_fk = 31
        LEFT JOIN link_hebergement_metadata AS heb_gid_theme_equestre
               ON heb_gid_theme_equestre.heb_fk = hebergement.heb_pk AND heb_gid_theme_equestre.metadata_fk = 32
        LEFT JOIN link_hebergement_metadata AS heb_gid_peche
               ON heb_gid_peche.heb_fk = hebergement.heb_pk AND heb_gid_peche.metadata_fk = 33
        LEFT JOIN link_hebergement_metadata AS heb_gid_patrimoine
               ON heb_gid_patrimoine.heb_fk = hebergement.heb_pk AND heb_gid_patrimoine.metadata_fk = 34
        LEFT JOIN link_hebergement_metadata AS heb_confort_congelateur
               ON heb_confort_congelateur.heb_fk = hebergement.heb_pk AND heb_confort_congelateur.metadata_fk = 35
        LEFT JOIN link_hebergement_metadata AS heb_commerce
               ON heb_commerce.heb_fk = hebergement.heb_pk AND heb_commerce.metadata_fk = 36
        LEFT JOIN link_hebergement_metadata AS heb_restaurant
               ON heb_restaurant.heb_fk = hebergement.heb_pk AND heb_restaurant.metadata_fk = 37
        LEFT JOIN link_hebergement_metadata AS heb_gare
               ON heb_gare.heb_fk = hebergement.heb_pk AND heb_gare.metadata_fk = 38
        LEFT JOIN link_hebergement_metadata AS heb_confort_projecteur
               ON heb_confort_projecteur.heb_fk = hebergement.heb_pk AND heb_confort_projecteur.metadata_fk = 39
        LEFT JOIN link_hebergement_metadata AS heb_confort_flipchart
               ON heb_confort_flipchart.heb_fk = hebergement.heb_pk AND heb_confort_flipchart.metadata_fk = 40
        LEFT JOIN link_hebergement_metadata AS heb_confort_ecran
               ON heb_confort_ecran.heb_fk = hebergement.heb_pk AND heb_confort_ecran.metadata_fk = 41
        LEFT JOIN link_hebergement_metadata AS heb_tabhot_gourmand
               ON heb_tabhot_gourmand.heb_fk = hebergement.heb_pk AND heb_tabhot_gourmand.metadata_fk = 42
        LEFT JOIN link_hebergement_metadata AS heb_tabhot_repas_familial
               ON heb_tabhot_repas_familial.heb_fk = hebergement.heb_pk AND heb_tabhot_repas_familial.metadata_fk = 43
        LEFT JOIN link_hebergement_metadata AS heb_tabhot_gastronomique
               ON heb_tabhot_gastronomique.heb_fk = hebergement.heb_pk AND heb_tabhot_gastronomique.metadata_fk = 44
        LEFT JOIN link_hebergement_metadata AS heb_bienvenu_velo
               ON heb_bienvenu_velo.heb_fk = hebergement.heb_pk AND heb_bienvenu_velo.metadata_fk = 47
        LEFT JOIN link_hebergement_metadata AS heb_wallonie_qualite
               ON heb_wallonie_qualite.heb_fk = hebergement.heb_pk AND heb_wallonie_qualite.metadata_fk = 63
        LEFT JOIN commune
               ON hebergement.heb_com_fk = commune.com_pk
        LEFT JOIN provinces
               ON commune.com_prov_fk = provinces.prov_pk
    ''')
