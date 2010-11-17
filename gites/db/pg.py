# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from affinitic.db.pg import PGDB


class GitesDB(PGDB):
    db = 'gites_wallons'
