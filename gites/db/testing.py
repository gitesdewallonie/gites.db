# -*- coding: utf-8 -*-
import glob
import os
import shutil
from tempfile import mkstemp
from zope.configuration import xmlconfig
from z3c.sqlalchemy import createSAWrapper
from plone.testing import Layer
from plone.testing import zca

DB_CACHE_DIR = os.path.join(os.getcwd(), '.testdb')


class RDBLayer(Layer):
    defaultBases = (zca.ZCML_DIRECTIVES, )
    logging = False

    @property
    def dbPrefix(self):
        raise NotImplementedError

    def setUp(self):
        self.tmpDBFile = self.getDBFile()
        self.setupDatabase()
        self.storeDBState()
        self.setupData()

    def getDBFile(self):
        if not os.path.exists(DB_CACHE_DIR):
            os.mkdir(DB_CACHE_DIR)
        tmpFile = None
        for file in glob.glob("%s/%s*stored.db" % (DB_CACHE_DIR, self.dbPrefix)):
            tmpFile = self.restoreDBState(file)
        if tmpFile is None:
            tmpFile = mkstemp(dir=DB_CACHE_DIR, suffix='.db',
                              prefix=self.dbPrefix)[1]
        return tmpFile

    def hasStoredDB(self):
        return len(glob.glob("%s/%s*stored.db" % (DB_CACHE_DIR, self.dbPrefix))) > 0

    def storeDBState(self):
        if self.hasStoredDB():
            return
        filepath, filename = os.path.split(self.tmpDBFile)
        filename = filename.replace('.db', 'stored.db')
        shutil.copyfile(self.tmpDBFile, os.path.join(filepath, filename))

    def restoreDBState(self, dbFile):
        filepath, filename = os.path.split(dbFile)
        filename = filename.replace('stored.db', '.db')
        newFilePath = os.path.join(filepath, filename)
        shutil.copyfile(dbFile, newFilePath)
        return newFilePath

    def setupData(self):
        """
        Hook to allow subclasses to setup initial layer data.
        """
        pass

    def testTearDown(self):
        import transaction
        transaction.abort()

    def tearDown(self):
        if os.path.exists(self.tmpDBFile):
            os.unlink(self.tmpDBFile)

    def setupDatabase(self):
        configurationContext = self['configurationContext']
        xmlconfig.file('testing.zcml', self.package, context=configurationContext)
        configurationContext.execute_actions()
        wr = createSAWrapper('sqlite:///%s' % self.tmpDBFile,
                            forZope=True,
                            echo=self.logging,
                            engine_options={'convert_unicode': True},
                            name=self.dbName,
                            model=self.model)
        self['%s_wrapper' % self.dbPrefix] = wr

import gites.db


class PGRdb(RDBLayer):
    dbPrefix = 'pg'
    dbName = 'gites_wallons'
    model = 'GitesMappings'
    package = gites.db
    logging = True

PGRDB = PGRdb(name='PGRDB')
