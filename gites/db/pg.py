# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from affinitic.db.pg import PGDB
from zope.component import getUtility
from affinitic.pwmanager.interfaces import IPasswordManager


class GitesDB(PGDB):
    db = 'gites_wallons'
    verbose = True

    @property
    def url(self):
        pwManager = getUtility(IPasswordManager, 'pg')
        return 'postgres://%s@localhost/gites_wallons' % pwManager.getLoginPassWithSeparator(':')
