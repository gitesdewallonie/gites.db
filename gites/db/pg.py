# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from affinitic.db import utils
from affinitic.db.pg import PGDB
from affinitic.pwmanager.interfaces import IPasswordManager
from gites.db import DeclarativeBase
from zope.component import getUtility


class GitesDB(PGDB):
    db = 'gites_wallons'
    verbose = False

    @property
    def url(self):
        pwManager = getUtility(IPasswordManager, 'pg')
        return 'postgres://%s@localhost/gites_wallons' % pwManager.getLoginPassWithSeparator(':')


def set_mappers(metadata, event=None):
    utils.initialize_declarative_mappers(DeclarativeBase, metadata)
    utils.initialize_defered_mappers(metadata)
