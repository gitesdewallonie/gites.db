# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from z3c.sqlalchemy import Model
from z3c.sqlalchemy.interfaces import IModelProvider
from zope.interface import implements
from sqlalchemy.orm import mapper, relation, clear_mappers
from sqlalchemy import MetaData, and_
from gites.db.tables import (getHebergementTable,
                             getHebergementMajTable,
                             getTypeHebergementTable,
                             getMaisonTourisme,
                             getCommune,
                             getProprio,
                             getProprioMaj,
                             getCivilite,
                             getProvinces,
                             getInfoTouristique,
                             getTableHote,
                             getTypeTableHoteOfHebergement,
                             getTypeTableHoteOfHebergementMaj,
                             getLinkHebergementEpisTable,
                             getInfoPratique,
                             getTypeInfoPratique,
                             getTypeInfoTouristique,
                             getCharge,
                             getReservationProprio,
                             getHebBlockedHistory,
                             getBlockingHistory,
                             getLogTable,
                             getPackage,
                             getPackageDetail,
                             getLinkPackageHebergement,
                             getMetadata,
                             getLinkHebergementMetadata,
                             getMapBlacklist)
from gites.db.content import (Civilite,
                              Province,
                              TableHote,
                              Charge,
                              MaisonTourisme,
                              Hebergement,
                              HebergementMaj,
                              Commune,
                              TypeHebergement,
                              InfoTouristique,
                              TypeTableHoteOfHebergement,
                              TypeTableHoteOfHebergementMaj,
                              LinkHebergementEpis,
                              Proprio,
                              ProprioMaj,
                              ReservationProprio,
                              HebergementBlockingHistory,
                              BlockingHistory,
                              LogItem,
                              PackageDetail,
                              LinkPackageHebergement,
                              Metadata,
                              LinkHebergementMetadata,
                              MapBlacklist)

from gites.core.content.package import Package


class GitesModel(object):
    """
    A model providers provides information about the tables to be used
    and the mapper classes.
    """
    implements(IModelProvider)

    def getModel(self, metadata=None):
        """
            The model is described as an ordered dictionary.  The entries are
            (tablename, some_dict) where 'some_dict' is a dictionary containing a
            key 'table' referencing a Table() instance and an optional key
            'relationships' referencing a sequence of related table names. An
            optional mapper class can be specified through the 'class' key
            (otherwise a default mapper class will be autogenerated).
        """
        clear_mappers()

        CiviliteTable = getCivilite(metadata)
        CiviliteTable.create(checkfirst=True)

        MaisonTourismeTable = getMaisonTourisme(metadata)
        MaisonTourismeTable.create(checkfirst=True)

        ProvincesTable = getProvinces(metadata)
        ProvincesTable.create(checkfirst=True)

        CommuneTable = getCommune(metadata)
        CommuneTable.create(checkfirst=True)

        ProprioTable = getProprio(metadata)
        ProprioTable.create(checkfirst=True)

        ProprioMajTable = getProprioMaj(metadata)
        ProprioMajTable.create(checkfirst=True)

        TypeHebergementTable = getTypeHebergementTable(metadata)
        TypeHebergementTable.create(checkfirst=True)

        ChargeTable = getCharge(metadata)
        ChargeTable.create(checkfirst=True)

        HebergementTable = getHebergementTable(metadata)
        HebergementTable.create(checkfirst=True)

        HebergementMajTable = getHebergementMajTable(metadata)
        HebergementMajTable.create(checkfirst=True)

        InfoTouristiqueTable = getInfoTouristique(metadata)
        InfoTouristiqueTable.create(checkfirst=True)

        InfoPratiqueTable = getInfoPratique(metadata)
        InfoPratiqueTable.create(checkfirst=True)

        TypeInfoPratiqueTable = getTypeInfoPratique(metadata)
        TypeInfoPratiqueTable.create(checkfirst=True)

        TypeInfoTouristiqueTable = getTypeInfoTouristique(metadata)
        TypeInfoTouristiqueTable.create(checkfirst=True)

        TableHoteTable = getTableHote(metadata)
        TableHoteTable.create(checkfirst=True)

        TypeTableHoteOfHebergementTable = getTypeTableHoteOfHebergement(metadata)
        TypeTableHoteOfHebergementTable.create(checkfirst=True)

        TypeTableHoteOfHebergementMajTable = getTypeTableHoteOfHebergementMaj(metadata)
        TypeTableHoteOfHebergementMajTable.create(checkfirst=True)

        LinkHebergementEpisTable = getLinkHebergementEpisTable(metadata)
        LinkHebergementEpisTable.create(checkfirst=True)

        ReservationProprioTable = getReservationProprio(metadata)
        ReservationProprioTable.create(checkfirst=True)

        MapBlacklistTable = getMapBlacklist(metadata)
        MapBlacklistTable.create(checkfirst=True)

        mapper(ReservationProprio, ReservationProprioTable)

        mapper(LinkHebergementEpis, LinkHebergementEpisTable)

        mapper(InfoTouristique, InfoTouristiqueTable)

        mapper(Province, ProvincesTable,
               properties={'relatedHebergement': relation(Hebergement, lazy=True,
                                                          secondary=CommuneTable,
                                                          primaryjoin=ProvincesTable.c.prov_pk == CommuneTable.c.com_prov_fk,
                                                          secondaryjoin=CommuneTable.c.com_pk == HebergementTable.c.heb_com_fk)})

        mapper(Commune, CommuneTable,
               properties={'relatedHebergement': relation(Hebergement, lazy=True,
                            primaryjoin=CommuneTable.c.com_pk == HebergementTable.c.heb_com_fk),
                           'province': relation(Province, lazy=True,
                                                primaryjoin=ProvincesTable.c.prov_pk == CommuneTable.c.com_prov_fk)})
        mapper(Civilite, CiviliteTable)

        mapper(Proprio, ProprioTable,
               properties={'civilite': relation(Civilite),
                           'commune': relation(Commune)})

        mapper(ProprioMaj, ProprioMajTable,
               properties={'civilite': relation(Civilite),
                           'commune': relation(Commune)})

        mapper(HebergementMaj, HebergementMajTable)

        mapper(TableHote, TableHoteTable)

        mapper(TypeTableHoteOfHebergement, TypeTableHoteOfHebergementTable, primary_key=[TypeTableHoteOfHebergementTable.c.hebhot_heb_fk, TypeTableHoteOfHebergementTable.c.hebhot_tabho_fk])

        mapper(TypeTableHoteOfHebergementMaj, TypeTableHoteOfHebergementMajTable, primary_key=[TypeTableHoteOfHebergementMajTable.c.hebhot_maj_heb_fk, TypeTableHoteOfHebergementMajTable.c.hebhot_maj_tabho_fk])

        mapper(Charge, ChargeTable)

        mapper(Hebergement, HebergementTable,
               properties={'type': relation(TypeHebergement, lazy=True),
                           'proprio': relation(Proprio, lazy=True,
                                               backref='hebergements'),
                           'reservations': relation(ReservationProprio, lazy=True,
                                                    backref='hebergement'),
                           'charge': relation(Charge, lazy=True),
                           'commune': relation(Commune, lazy=True),
                           'epis': relation(LinkHebergementEpis, lazy=True),
                           'province': relation(Province,
                                                secondary=CommuneTable,
                                                foreign_keys=[CommuneTable.c.com_pk, CommuneTable.c.com_prov_fk],
                                                primaryjoin=HebergementTable.c.heb_com_fk == CommuneTable.c.com_pk,
                                                secondaryjoin=CommuneTable.c.com_prov_fk == ProvincesTable.c.prov_pk,
                                                lazy=True),
                           'maisonTourisme': relation(MaisonTourisme,
                                                      secondary=CommuneTable,
                                                      foreign_keys=[CommuneTable.c.com_pk, CommuneTable.c.com_mais_fk],
                                                      primaryjoin=CommuneTable.c.com_pk == HebergementTable.c.heb_com_fk,
                                                      secondaryjoin=MaisonTourismeTable.c.mais_pk == CommuneTable.c.com_mais_fk,
                                                      lazy=True),
                           'tableHote': relation(TableHote,
                                                 secondary=TypeTableHoteOfHebergementTable,
                                                 foreign_keys=[TypeTableHoteOfHebergementTable.c.hebhot_heb_fk, TypeTableHoteOfHebergementTable.c.hebhot_tabho_fk],
                                                 primaryjoin=HebergementTable.c.heb_pk == TypeTableHoteOfHebergementTable.c.hebhot_heb_fk,
                                                 secondaryjoin=TypeTableHoteOfHebergementTable.c.hebhot_tabho_fk == TableHoteTable.c.tabho_pk,
                                                 lazy=True),
                           })
        mapper(TypeHebergement, TypeHebergementTable)

        mapper(MaisonTourisme, MaisonTourismeTable,
               properties={'commune': relation(Commune,
                                               lazy=True),
                           'infosTouristique': relation(InfoTouristique,
                                                       secondary=CommuneTable,
                                                       primaryjoin=CommuneTable.c.com_mais_fk == MaisonTourismeTable.c.mais_pk,
                                                       secondaryjoin=CommuneTable.c.com_pk == InfoTouristiqueTable.c.infotour_commune_fk,
                                                       lazy=True)})
        hebBlockedHistory = getHebBlockedHistory(metadata)
        mapper(HebergementBlockingHistory, hebBlockedHistory,
               properties={'hebergement': relation(Hebergement, backref='hebblockinghistory')})
        blockingHistory = getBlockingHistory(metadata)
        mapper(BlockingHistory, blockingHistory,
               properties={'hebergement': relation(Hebergement, backref='blockinghistory')})

        logItemTable = getLogTable(metadata)
        mapper(LogItem, logItemTable)

        # Gestion des métadonnées

        metadataTable = getMetadata(metadata)
        metadataTable.create(checkfirst=True)

        linkHebergementMetadataTable = getLinkHebergementMetadata(metadata)
        linkHebergementMetadataTable.create(checkfirst=True)

        mapper(LinkHebergementMetadata, linkHebergementMetadataTable)
        mapper(Metadata, metadataTable)

        # Nouveau contenu package (denières minutes, sejours, etc.)

        PackageTable = getPackage(metadata)
        PackageTable.create(checkfirst=True)

        PackageDetailTable = getPackageDetail(metadata)
        PackageDetailTable.create(checkfirst=True)

        LinkPackageHebergementTable = getLinkPackageHebergement(metadata)
        LinkPackageHebergementTable.create(checkfirst=True)

        mapper(Package, PackageTable,
               properties={'key': PackageTable.c.pack_id,
                           'hebergements': relation(Hebergement,
                                                    secondary=LinkPackageHebergementTable,
                                                    lazy=True,
                                                    backref='packages'),
                           'detail_fr': relation(PackageDetail,
                                                 uselist=False,
                                                 primaryjoin=and_(PackageTable.c.pack_pk == PackageDetailTable.c.packdet_package_fk,
                                                                  PackageDetailTable.c.packdet_langue == 'fr'),
                                                 lazy=True),
                           'detail_en': relation(PackageDetail,
                                                 uselist=False,
                                                 primaryjoin=and_(PackageTable.c.pack_pk == PackageDetailTable.c.packdet_package_fk,
                                                                  PackageDetailTable.c.packdet_langue == 'en'),
                                                 lazy=True),
                           'detail_nl': relation(PackageDetail,
                                                 uselist=False,
                                                 primaryjoin=and_(PackageTable.c.pack_pk == PackageDetailTable.c.packdet_package_fk,
                                                                  PackageDetailTable.c.packdet_langue == 'nl'),
                                                 lazy=True),
                           'detail_it': relation(PackageDetail,
                                                 uselist=False,
                                                 primaryjoin=and_(PackageTable.c.pack_pk == PackageDetailTable.c.packdet_package_fk,
                                                                  PackageDetailTable.c.packdet_langue == 'it'),
                                                 lazy=True),
                           'detail_de': relation(PackageDetail,
                                                 uselist=False,
                                                 primaryjoin=and_(PackageTable.c.pack_pk == PackageDetailTable.c.packdet_package_fk,
                                                                  PackageDetailTable.c.packdet_langue == 'de'),
                                                 lazy=True)})

        mapper(PackageDetail, PackageDetailTable,
               properties={'package': relation(Package,
                                               lazy=True,
                                               uselist=False,
                                               backref='details')})

        mapper(LinkPackageHebergement, LinkPackageHebergementTable)
        mapper(MapBlacklist, MapBlacklistTable)

        model = Model()
        model.add('reservation_proprio',
                  table=ReservationProprioTable,
                  mapper_class=ReservationProprio)
        model.add('commune', table=CommuneTable,
                  mapper_class=Commune)
        model.add('proprio', table=ProprioTable,
                  mapper_class=Proprio)
        model.add('proprioMaj', table=ProprioMajTable,
                  mapper_class=ProprioMaj)
        model.add('province', table=ProvincesTable,
                  mapper_class=Province)
        model.add('charge', table=ChargeTable,
                  mapper_class=Charge)
        model.add('hebergement', table=HebergementTable,
                  mapper_class=Hebergement)
        model.add('hebergementMaj', table=HebergementMajTable,
                  mapper_class=HebergementMaj)
        model.add('maison_tourisme', table=MaisonTourismeTable,
                  mapper_class=MaisonTourisme)
        model.add('type_heb', TypeHebergementTable,
                  mapper_class=TypeHebergement)
        model.add('info_touristique', table=InfoTouristiqueTable,
                  mapper_class=InfoTouristique)
        model.add('table_hote', table=TableHoteTable,
                  mapper_class=TableHote)
        model.add('heb_tab_hote', table=TypeTableHoteOfHebergementTable,
                  mapper_class=TypeTableHoteOfHebergement)
        model.add('heb_tab_hote_maj', table=TypeTableHoteOfHebergementMajTable,
                  mapper_class=TypeTableHoteOfHebergementMaj)
        model.add('log_item', table=logItemTable,
                  mapper_class=LogItem)
        model.add('package',
                  table=PackageTable,
                  mapper_class=Package)
        model.add('package_detail',
                  table=PackageDetailTable,
                  mapper_class=PackageDetail)
        model.add('map_blacklist',
                  table=MapBlacklistTable,
                  mapper_class=MapBlacklist)
        metadata.create_all()
        return model


def setupRDB(engine):
    metadata = MetaData(engine)
    model = GitesModel()
    model.getModel(metadata)
