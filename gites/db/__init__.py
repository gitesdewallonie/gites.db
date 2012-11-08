from zope.component import getUtility
from affinitic.db.interfaces import IDatabase
from affinitic.pwmanager.interfaces import IPasswordManager
from z3c.sqlalchemy import createSAWrapper, getSAWrapper

def session():
    try:
        wrapper = getSAWrapper('gites_wallons')
    except ValueError:
        db = getUtility(IDatabase, 'postgres')
        return db.session
    else:
        return wrapper.session

from gites.db.content import *

def initialize(context):
    pwManager = getUtility(IPasswordManager, 'pg')
    connString = 'postgres://%s@localhost/gites_wallons' % \
                        pwManager.getLoginPassWithSeparator(':')
    createSAWrapper(connString,
                        forZope=True,
                        engine_options = {'convert_unicode': True,
                                          'encoding': 'utf-8'},
                        encoding='utf-8',
                        name='gites_wallons',
                        model='GitesMappings')
