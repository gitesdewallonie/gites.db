# -*- coding: utf-8 -*-
import os
import transaction
from zope.configuration import xmlconfig
import gocept.testdb
from sqlalchemy.orm import clear_mappers
from z3c.sqlalchemy import createSAWrapper
from z3c.sqlalchemy import getSAWrapper
from plone.testing import Layer
from plone.testing import zca

CURRENT_DIR = os.path.dirname(__file__)


def createHeb(session):
    from gites.db.content import (Hebergement, TypeHebergement, Proprio,
                                  LinkHebergementEpis, Commune,
                                  HebergementApp)
    typeHebGite = TypeHebergement(type_heb_nom='gites')
    proprio = Proprio(pro_nom1=u'Foo',
                      pro_etat=True)
    epis3 = LinkHebergementEpis(heb_nombre_epis=3)
    yvoir = Commune(com_nom=u'Yvoir')
    heb_app = HebergementApp(heb_app_sort_order=1)
    heb = Hebergement(heb_nom='Home sweet home',
                      type=typeHebGite,
                      proprio=proprio,
                      epis=[epis3],
                      commune=yvoir,
                      app=heb_app,
                      heb_site_public='1')
    session.add(heb)
    session.flush()


class RDBLayer(Layer):
    defaultBases = (zca.ZCML_DIRECTIVES, )
    logging = False

    @property
    def dbPrefix(self):
        raise NotImplementedError

    def setUp(self):
        self.setupDatabase()
        self.setupData()

    def setupData(self):
        """
        Hook to allow subclasses to setup initial layer data.
        """
        createHeb(self.wrapper.session)
        transaction.commit()

    def tearDown(self):
        clear_mappers()
        self.invalidate()
        self.db.drop_all()

    def invalidate(self):
        """
        Invalidates the connections to the database
        """
        self.wrapper.session.close()
        self.engine.dispose()
        del self.engine

    def testTearDown(self):
        transaction.abort()

    def setupDatabase(self):
        configurationContext = self['configurationContext']
        xmlconfig.file('testing.zcml', self.package, context=configurationContext)
        configurationContext.execute_actions()
        schema_file = os.path.join(CURRENT_DIR, 'tests', 'gites_wallons.sql')
        self.db = gocept.testdb.PostgreSQL(encoding='UTF8',
                                           db_template='gites_wallons_testing',
                                           schema_path=schema_file)
        self.db.create()
        wr = createSAWrapper(self.db.dsn,
                             forZope=self.forZope,
                             echo=self.logging,
                             engine_options={'convert_unicode': True},
                             name=self.dbName,
                             model=self.model)
        self['%s_wrapper' % self.dbPrefix] = self.wrapper = wr
        self.engine = self.wrapper.engine
        wrapper = getSAWrapper('gites_wallons')
        wrapper.metadata.create_all()

import gites.db


class PGRdb(RDBLayer):
    dbPrefix = 'pg'
    dbName = 'gites_wallons'
    model = 'GitesMappings'
    package = gites.db
    logging = True
    forZope = True


class PGRdbNoZope(PGRdb):
    forZope = False


PGRDB = PGRdb(name='PGRDB')
PGRDBNOZOPE = PGRdb(name='PGRDBNOZOPE')