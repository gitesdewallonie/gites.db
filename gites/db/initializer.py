# -*- coding: utf-8 -*-
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import DeferredReflection
from z3c.sqlalchemy import Model
from z3c.sqlalchemy.interfaces import IModelProvider
from zope.interface import implements
from gites.db import DeclarativeBase
from gites.db.content import (BlockingHistory,
                              Charge,
                              Commune,
                              Hebergement,
                              HebergementBlockingHistory,
                              HebergementMaj,
                              InfoTouristique,
                              LinkHebergementEpis,
                              LinkHebergementMetadata,
                              LogItem,
                              MaisonTourisme,
                              MapBlacklist,
                              MapProvider,
                              Metadata,
                              MetadataType,
                              Proprio,
                              ProprioMaj,
                              Province,
                              ReservationProprio,
                              TableHote,
                              TypeHebergement,
                              TypeTableHoteOfHebergement,
                              TypeTableHoteOfHebergementMaj,
                              Civilite)


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
        metadata.create_all()
        DeferredReflection.prepare(metadata.bind)

        model = Model()
        model.add('reservation_proprio',
                  table=ReservationProprio.__table__,
                  mapper_class=ReservationProprio)
        model.add('commune', table=Commune.__table__,
                  mapper_class=Commune)
        model.add('proprio', table=Proprio.__table__,
                  mapper_class=Proprio)
        model.add('proprioMaj', table=ProprioMaj.__table__,
                  mapper_class=ProprioMaj)
        model.add('province', table=Province.__table__,
                  mapper_class=Province)
        model.add('charge', table=Charge.__table__,
                  mapper_class=Charge)
        model.add('hebergement', table=Hebergement.__table__,
                  mapper_class=Hebergement)
        model.add('hebergementMaj', table=HebergementMaj.__table__,
                  mapper_class=HebergementMaj)
        model.add('maison_tourisme', table=MaisonTourisme.__table__,
                  mapper_class=MaisonTourisme)
        model.add('type_heb', TypeHebergement.__table__,
                  mapper_class=TypeHebergement)
        model.add('info_touristique', table=InfoTouristique.__table__,
                  mapper_class=InfoTouristique)
        model.add('table_hote', table=TableHote.__table__,
                  mapper_class=TableHote)
        model.add('heb_tab_hote', table=TypeTableHoteOfHebergement.__table__,
                  mapper_class=TypeTableHoteOfHebergement)
        model.add('heb_tab_hote_maj', table=TypeTableHoteOfHebergementMaj.__table__,
                  mapper_class=TypeTableHoteOfHebergementMaj)
        model.add('log_item', table=LogItem.__table__,
                  mapper_class=LogItem)
        model.add('map_provider',
                  table=MapProvider.__table__,
                  mapper_class=MapProvider)
        model.add('map_blacklist',
                  table=MapBlacklist.__table__,
                  mapper_class=MapBlacklist)
        model.add('link_hebergement_metadata',
                  table=LinkHebergementMetadata.__table__,
                  mapper_class=LinkHebergementMetadata)
        model.add('metadata_type',
                  table=MetadataType.__table__,
                  mapper_class=MetadataType)
        model.add('metadata',
                  table=Metadata.__table__,
                  mapper_class=Metadata)
        metadata.create_all()
        return model


def setupRDB(engine):
    metadata = MetaData(engine)
    model = GitesModel()
    model.getModel(metadata)
