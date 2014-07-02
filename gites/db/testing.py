# -*- coding: utf-8 -*-
import gocept.testdb
import os
import transaction
from zope.configuration import xmlconfig
from zope.component import provideUtility
from sqlalchemy import create_engine
from sqlalchemy.orm import clear_mappers
from z3c.sqlalchemy import createSAWrapper
from z3c.sqlalchemy import getSAWrapper
from plone.testing import Layer
from plone.testing import zca
from affinitic.db.interfaces import IDatabase
from affinitic.db.utils import (initialize_declarative_mappers,
                                initialize_defered_mappers)
from affinitic.testing import DatabaseTestCase
from gites.db import DeclarativeBase
from gites.db.pg import GitesDB

CURRENT_DIR = os.path.dirname(__file__)


def createHeb(session):
    from gites.db.content import (Hebergement, Proprio,
                                  LinkHebergementEpis, Commune,
                                  HebergementApp)
    proprio = Proprio(pro_nom1=u'Foo',
                      pro_etat=True)
    epis3 = LinkHebergementEpis(heb_nombre_epis=3)
    yvoir = Commune(com_nom=u'Yvoir')
    heb_app = HebergementApp(heb_app_sort_order=1)
    heb = Hebergement(heb_nom='Home sweet home',
                      heb_typeheb_fk=1,
                      proprio=proprio,
                      epis=[epis3],
                      commune=yvoir,
                      app=heb_app,
                      heb_site_public='1')
    session.add(heb)
    session.flush()


class GitesTestDB(GitesDB):

    @property
    def url(self):
        return self.dsn


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


class PGScriptRDB(RDBLayer):
    dbPrefix = 'pg'
    dbName = 'gites_wallons'
    package = gites.db

    def setupData(self):
        pass

    def testTearDown(self):
        pass

    def invalidate(self):
        """
        Invalidates the connections to the database
        """
        db_name = self.session.bind.url.database
        self.session.close()
        new_session = self.pg.session
        query = new_session.execute(
            "SELECT procpid FROM pg_stat_activity where datname = '{0}'"
            "order by backend_start asc".format(db_name))
        connections = [l[0] for l in query.fetchall()]
        for conn in connections:
            statement = 'SELECT pg_terminate_backend({0})'.format(conn)
            try:
                new_session.execute(statement).fetchall()
            except:
                pass
        self.conn.invalidate()
        self.engine.dispose()
        del self.engine

    def setupDatabase(self):
        configurationContext = self['configurationContext']
        xmlconfig.file('testing.zcml', self.package,
                       context=configurationContext)
        configurationContext.execute_actions()
        schema_file = os.path.join(CURRENT_DIR, 'tests', 'gites_wallons.sql')
        self.db = gocept.testdb.PostgreSQL(encoding='UTF8',
                                           db_template='gites_wallons_testing',
                                           schema_path=schema_file)
        self.db.create()
        self.engine = create_engine(self.db.dsn)
        self.conn = self.engine.connect()
        self.pg = GitesTestDB()
        self.pg.dsn = self.db.dsn
        self.session = self.pg.session
        initialize_declarative_mappers(DeclarativeBase, self.pg.metadata)
        initialize_defered_mappers(self.pg.metadata)
        provideUtility(self.pg, IDatabase, 'postgres')


class PGRdbNoZope(PGRdb):
    forZope = False


class GitesWallonsDBTestCase(DatabaseTestCase):
    databases = ('gites_wallons', )

    @property
    def gites_wallons_session(self):
        return getSAWrapper('gites_wallons').session


PGRDB = PGRdb(name='PGRDB')
PGRDBNOZOPE = PGRdb(name='PGRDBNOZOPE')
