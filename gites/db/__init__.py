import os
from zope.component import getUtility
from affinitic.db.interfaces import IDatabase
from affinitic.pwmanager.interfaces import IPasswordManager
from z3c.sqlalchemy import createSAWrapper, getSAWrapper

from Products.Archetypes import listTypes
from Products.Archetypes.atapi import process_types
from Products.CMFCore import utils as cmfutils

from config import PROJECTNAME, DEFAULT_ADD_CONTENT_PERMISSION


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
    if os.environ.get('ZOPETESTCASE') is None:
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

    # imports packages and types for registration

    import gites.db.content.folder
    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)
    cmfutils.ContentInit(
        PROJECTNAME + ' Content',
        content_types=content_types,
        permission=DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors=constructors,
        fti=ftis,
        ).initialize(context)
