import os
from zope.component import getUtility
from affinitic.pwmanager.interfaces import IPasswordManager
from z3c.sqlalchemy import createSAWrapper


def initialize(context):
    pwManager = getUtility(IPasswordManager, 'pg')
    dbHostname = os.environ.get('PG_HOSTNAME', 'localhost')
    connString = 'postgres://%s@%s/gites_wallons' % \
                        (pwManager.getLoginPassWithSeparator(':'),
                         dbHostname)
    wr = createSAWrapper(connString,
                        forZope=True,
                        engine_options = {'convert_unicode': True,
                                          'encoding': 'utf-8'},
                        encoding='utf-8',
                        name='gites_wallons',
                        model='GitesMappings')
