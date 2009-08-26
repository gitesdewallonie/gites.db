from zope.component import getUtility
from affinitic.pwmanager.interfaces import IPasswordManager
from z3c.sqlalchemy import createSAWrapper


def initialize(context):
    pwManager = getUtility(IPasswordManager, 'pg')
    connString = 'postgres://%s@localhost/gites_wallons' % \
                        pwManager.getLoginPassWithSeparator(':')
    wr = createSAWrapper(connString,
                        forZope=True,
                        engine_options = {'convert_unicode': True,
                                          'encoding': 'utf-8'},
                        encoding='utf-8',
                        name='gites_wallons',
                        model='GitesMappings')
