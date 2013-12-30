# -*- coding: utf-8 -*-
import os
from zope.configuration import xmlconfig
import gocept.testdb
from z3c.sqlalchemy import createSAWrapper
from z3c.sqlalchemy import getSAWrapper
from plone.testing import Layer
from plone.testing import zca

CURRENT_DIR = os.path.dirname(__file__)


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
        pass

    def testTearDown(self):
        import transaction
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
        self['%s_wrapper' % self.dbPrefix] = wr
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
