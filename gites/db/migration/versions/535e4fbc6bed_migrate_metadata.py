# -*- coding: utf-8 -*-

"""Migrate metadata

Revision ID: 535e4fbc6bed
Revises: None
Create Date: 2013-02-13 16:51:40.867726

"""

# revision identifiers, used by Alembic.
revision = '535e4fbc6bed'
down_revision = None

from alembic import op
from sqlalchemy import select, MetaData
from gites.db.tables import getHebergementTable, getMetadata, \
                            getLinkHebergementMetadata


metadatas = [
    {'id':'heb_tenis',
     'titre_fr':'Tennis',
     'titre_nl':'Tennis',
     'titre_en':'Tennis',
     'titre_it':'Tennis',
     'titre_de':'Tennis',
     'filterable': True},
    {'id':'heb_nautisme',
     'titre_fr':'Sports nautiques',
     'titre_nl':'Watersporten',
     'titre_en':'Water sports',
     'titre_it':'Sport nautici',
     'titre_de':'Wassersport',
     'filterable': True},
    {'id':'heb_sky',
     'titre_fr':'Ski',
     'titre_nl':'Ski',
     'titre_en':'Ski',
     'titre_it':'Sci',
     'titre_de':'Ski',
     'filterable': True},
    {'id':'heb_rando',
     'titre_fr':'Randonnée',
     'titre_nl':'Tocht',
     'titre_en':'Walk',
     'titre_it':'Gita',
     'titre_de':'Wandern',
     'filterable': True},
    {'id':'heb_piscine',
     'titre_fr':'Piscine',
     'titre_nl':'Zwembad',
     'titre_en':'Swimming pool',
     'titre_it':'Piscina',
     'titre_de':'Swimmingpool',
     'filterable': True},
    {'id':'heb_peche',
     'titre_fr':'Pêche',
     'titre_nl':'Hengelen',
     'titre_en':'Fishing',
     'titre_it':'Pesca',
     'titre_de':'Angeln',
     'filterable': True},
    {'id':'heb_equitation',
     'titre_fr':'Equitation',
     'titre_nl':'Paardrijden',
     'titre_en':'Horse-riding',
     'titre_it':'Equitazione',
     'titre_de':'Reitsport',
     'filterable': True},
    {'id':'heb_velo',
     'titre_fr':'Vélo',
     'titre_nl':'Fiets',
     'titre_en':'Bicycle',
     'titre_it':'Bicicletta',
     'titre_de':'Fahrrad',
     'filterable': True},
    {'id':'heb_vtt',
     'titre_fr':'VTT',
     'titre_nl':'Mountainbike',
     'titre_en':'MTB',
     'titre_it':'Moutain bike',
     'titre_de':'Moutainbike',
     'filterable': True},
    {'id':'heb_ravel',
     'titre_fr':'Ravel',
     'titre_nl':'Ravel',
     'titre_en':'Ravel',
     'titre_it':'Ravel',
     'titre_de':'Ravel',
     'filterable': True},
    {'id':'heb_animal',
     'titre_fr':'Animaux de compagnie autorisés',
     'titre_nl':'Gezelschapsdieren toegelaten',
     'titre_en':'Pets allowed',
     'titre_it':'Animali di compagnia autorizzati',
     'titre_de':'Haustiere zugelassen',
     'filterable': True},
    {'id':'heb_fumeur',
     'titre_fr':'Hébergement fumeur',
     'titre_nl':'Rokers-logeeradres',
     'titre_en':'Smoking accommodation',
     'titre_it':'Abitazione fumatori',
     'titre_de':'Unterkunft für Raucher',
     'filterable': True},
    {'id':'heb_confort_tv',
     'titre_fr':'Télévision',
     'titre_nl':'Televisie',
     'titre_en':'Television',
     'titre_it':'Televisione',
     'titre_de':'Fernseher',
     'filterable': True},
    {'id':'heb_confort_feu_ouvert',
     'titre_fr':'Feu ouvert',
     'titre_nl':'Open haard',
     'titre_en':'Open fire',
     'titre_it':'Caminetto',
     'titre_de':'Offener Kamin',
     'filterable': True},
    {'id':'heb_confort_lave_vaiselle',
     'titre_fr':'Lave-vaisselle',
     'titre_nl':'Vaatwas',
     'titre_en':'Dish-washer',
     'titre_it':'Lavastoviglie',
     'titre_de':'Geschirrspüler',
     'filterable': True},
    {'id':'heb_confort_micro_onde',
     'titre_fr':'Micro-onde',
     'titre_nl':'Microgolf',
     'titre_en':'Microwave',
     'titre_it':'Microonde',
     'titre_de':'Mikrowelle',
     'filterable': True},
    {'id':'heb_confort_lave_linge',
     'titre_fr':'Lave-linge',
     'titre_nl':'Wasmachine',
     'titre_en':'Washing-machine',
     'titre_it':'Lavatrice',
     'titre_de':'Waschmaschine',
     'filterable': True},
    {'id':'heb_confort_seche_linge',
     'titre_fr':'Sèche-linge',
     'titre_nl':'Droogkast',
     'titre_en':'Dryer',
     'titre_it':'Asciugabiancheria',
     'titre_de':'Wäschetrockner',
     'filterable': True},
    {'id':'heb_confort_internet',
     'titre_fr':'Internet',
     'titre_nl':'Internet',
     'titre_en':'Internet',
     'titre_it':'Internet',
     'titre_de':'Internet',
     'filterable': True},
    {'id':'heb_confort_terrasse',
     'titre_fr':'Terrasse',
     'titre_nl':'Terras',
     'titre_en':'Terrace',
     'titre_it':'Terrazza',
     'titre_de':'Terrasse',
     'filterable': True},
    {'id':'heb_confort_jardin',
     'titre_fr':'Jardin',
     'titre_nl':'Tuin',
     'titre_en':'Garden',
     'titre_it':'Giardino',
     'titre_de':'Garten',
     'filterable': True},
    {'id':'heb_confort_sauna',
     'titre_fr':'Sauna',
     'titre_nl':'Sauna',
     'titre_en':'Sauna',
     'titre_it':'Sauna',
     'titre_de':'Sauna',
     'filterable': True},
    {'id':'heb_confort_jacuzzi',
     'titre_fr':'Jacuzzi',
     'titre_nl':'Jacuzzi',
     'titre_en':'Jacuzzi',
     'titre_it':'Jacuzzi',
     'titre_de':'Jacuzzi',
     'filterable': True},
    {'id':'heb_seminaire_vert',
     'titre_fr':'Séminaire',
     'titre_nl':'Seminarie',
     'titre_en':'Seminar',
     'titre_it':'Seminario',
     'titre_de':'Seminar',
     'filterable': True},
    {'id':'heb_gid_bebe_tendresse',
     'titre_fr':'Gîte Bébé Tendresse',
     'titre_nl':'Gîte Baby-lief',
     'titre_en':'Cuddly Baby Gite',
     'titre_it':'Alloggio Dolce Bebè',
     'titre_de':'Ferienhaus Fürs Baby',
     'filterable': True},
    {'id':'heb_gid_access_tous',
     'titre_fr':'Gîte accessible à tous',
     'titre_nl':'Gîte toegankelijk voor elk van ons',
     'titre_en':'Gite accessible to all',
     'titre_it':'Alloggio Accessibile a Tutti',
     'titre_de':'Ferienhaus Zugänglich für alle',
     'filterable': True},
    {'id':'heb_gid_antiallergique',
     'titre_fr':'Gîte antiallergique',
     'titre_nl':'Antiallergische gîte',
     'titre_en':'Anti-allergic Gite',
     'titre_it':'Alloggio Antiallergico',
     'titre_de':'Ferienhaus Allergiefrei',
     'filterable': True},
    {'id':'heb_gid_beau_jardin',
     'titre_fr':'Gîte au jardin',
     'titre_nl':'Tuin-gîte',
     'titre_en':'Garden Gite',
     'titre_it':'Alloggio in Giardino',
     'titre_de':'Ferienhaus im Garten',
     'filterable': True},
    {'id':'heb_gid_activite_nature',
     'titre_fr':'Gîte Activités Découverte Nature',
     'titre_nl':'Gîte Natuurontdekkingsactiviteiten',
     'titre_en':'Gite of Nature Discovery Activities',
     'titre_it':'Alloggio Attività Scoperta della Natura',
     'titre_de':'Ferienhaus Aktiv Natur entdecken',
     'filterable': True},
    {'id':'heb_gid_panda',
     'titre_fr':'Gîte Panda',
     'titre_nl':'Gîte Panda',
     'titre_en':'Panda Gite',
     'titre_it':'Alloggio Panda',
     'titre_de':'Ferienhaus Panda',
     'filterable': True},
    {'id':'heb_gid_theme_equestre',
     'titre_fr':'Gîte équestre',
     'titre_nl':'Gîte Paardrijden',
     'titre_en':'Equestrian Gite',
     'titre_it':'Alloggio Equitazione',
     'titre_de':'Ferienhaus Reiten',
     'filterable': True},
    {'id':'heb_gid_peche',
     'titre_fr':'Gîte Pêche',
     'titre_nl':'Gîte Hengelen',
     'titre_en':'Fishing Gite',
     'titre_it':'Alloggio Pesca',
     'titre_de':'Ferienhaus Angeln',
     'filterable': True},
    {'id':'heb_gid_patrimoine',
     'titre_fr':'Gîte Patrimoine',
     'titre_nl':'Gîte Erfgoed',
     'titre_en':'Heritage Gite',
     'titre_it':'Alloggio Patrimonio Storico',
     'titre_de':'Ferienhaus Kulturerbe',
     'filterable': True},
    {'id':'heb_gid_eco_gite',
     'titre_fr':'Eco-Gîte',
     'titre_nl':'Eco-Gîte',
     'titre_en':'Eco-Gîte Stay',
     'titre_it':'Eco-Gîte',
     'titre_de':'Öko-Unterkunft',
     'filterable': True},
    {'id':'heb_confort_congelateur',
     'titre_fr':'Congélateur',
     'titre_nl':'Diepvries',
     'titre_en':'Freezer',
     'titre_it':'Congelatore',
     'titre_de':'Gefrierschrank',
     'filterable': False},
    {'id':'heb_taxe_sejour',
     'titre_fr':'Taxe de séjour',
     'titre_nl':'Verblijfstaks',
     'titre_en':'Sojourn tax',
     'titre_it':'Tassa di soggiorno',
     'titre_de':'Kurtaxe',
     'filterable': False},
    {'id':'heb_commerce',
     'titre_fr':'Commerce',
     'titre_nl':'Handelszaak',
     'titre_en':'Shops',
     'titre_it':'Negozio',
     'titre_de':'Geschäft',
     'filterable': False},
    {'id':'heb_restaurant',
     'titre_fr':'Restaurant',
     'titre_nl':'Restaurant',
     'titre_en':'Restaurant',
     'titre_it':'Ristorante',
     'titre_de':'Restaurant',
     'filterable': False},
    {'id':'heb_gare',
     'titre_fr':'Gare',
     'titre_nl':'Station',
     'titre_en':'Station',
     'titre_it':'Stazione',
     'titre_de':'Bahnhof',
     'filterable': False},
    {'id':'heb_confort_projecteur',
     'titre_fr':'Projecteur',
     'titre_nl':'Projector',
     'titre_en':'Projector',
     'titre_it':'Proiettore',
     'titre_de':'Projektor',
     'filterable': False},
    {'id':'heb_confort_flipchart',
     'titre_fr':'Flipchart',
     'titre_nl':'Flipchart',
     'titre_en':'Flipchart',
     'titre_it':'Flipchart',
     'titre_de':'Flipchart',
     'filterable': False},
    {'id':'heb_confort_ecran',
     'titre_fr':'Ecran',
     'titre_nl':'Scherm',
     'titre_en':'Screen',
     'titre_it':'Schermo',
     'titre_de':'Bildschirm',
     'filterable': False}
  ]


def upgrade():
    connection = op.get_bind()
    adHocMetadata = MetaData()
    adHocMetadata.bind = connection.engine

    hebergementTable = getHebergementTable(adHocMetadata)
    metadataTable = getMetadata(adHocMetadata)
    linkHebergementMetadataTable = getLinkHebergementMetadata(adHocMetadata)

    print "... Create new tables"
    metadataTable.create(checkfirst=True)
    linkHebergementMetadataTable.create(checkfirst=True)

    print "... Create all metadata records"
    op.bulk_insert(metadataTable,
                     [{'met_id': m['id'],
                       'met_titre_fr': m['titre_fr'],
                       'met_titre_nl': m['titre_nl'],
                       'met_titre_en': m['titre_en'],
                       'met_titre_it': m['titre_it'],
                       'met_titre_de': m['titre_de'],
                       'met_filterable': m['filterable']
                       } for m in metadatas])

    print "... Migrate existing metadata data"
    query = select([hebergementTable.c.heb_pk],
                   order_by=hebergementTable.c.heb_pk)
    result = connection.execute(query).fetchall()
    hebsPks = [r.heb_pk for r in result]

    index = 0
    for pk in hebsPks:
        index += 1
        if (index % 100) == 0:
            print "... Handling heb %s / %s" % (index, len(hebsPks))
        for metadata in metadatas:
            if metadata['id'] == 'heb_seminaire_vert':
                # the one and only boolean field !  don't want to write
                # beautiful code just for this one
                op.execute(u"""
                    INSERT INTO link_hebergement_metadata (heb_fk, metadata_fk, link_met_value)
                           SELECT pk, met_pk, value FROM
                                  (SELECT %s AS pk) s1,
                                  (SELECT met_pk AS met_pk FROM metadata WHERE met_id = '%s') s2,
                                  (SELECT CASE WHEN (%s = true) THEN true ELSE false END AS value FROM hebergement WHERE heb_pk = %s) s3
                    """ % (pk, metadata['id'], metadata['id'], pk))
            else:
                op.execute(u"""
                    INSERT INTO link_hebergement_metadata (heb_fk, metadata_fk, link_met_value)
                           SELECT pk, met_pk, value FROM
                                  (SELECT %s AS pk) s1,
                                  (SELECT met_pk AS met_pk FROM metadata WHERE met_id = '%s') s2,
                                  (SELECT CASE WHEN (%s = 'oui') THEN true ELSE false END AS value FROM hebergement WHERE heb_pk = %s) s3
                    """ % (pk, metadata['id'], metadata['id'], pk))


def downgrade():
    print "... Impossible to downgrade, too hard ;-)"
