"""empty message

Revision ID: 1969b7af44c6
Revises: 4fc12b740618
Create Date: 2013-03-21 14:45:26.782044

"""

# revision identifiers, used by Alembic.
revision = '1969b7af44c6'
down_revision = '4fc12b740618'


from alembic import op


def upgrade():
    print "... Creates the hebergement view"
    op.execute("""
        CREATE VIEW hebergement_view AS
        SELECT hebergement.*,
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
               CASE heb_tabhot_gastronomique.link_met_value WHEN true THEN 'oui' ELSE 'non' END AS heb_tabhot_gastronomique
        FROM hebergement
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
        """)


def downgrade():
    print "... Removes the hebergement view"
    op.execute('DROP VIEW hebergement_view')
