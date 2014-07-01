# encoding: utf-8
"""
gites.db

Created by schminitz
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from gites.db import testing
from gites.db.content import Tarifs
from gites.db.testing import GitesWallonsDBTestCase


class TarifsMapperTest(GitesWallonsDBTestCase):
    layer = testing.PGRDB
    gites_wallons_sql_file = ('tarifs')

    def test_get_hebergement_tarifs(self):
        tarifs = Tarifs.get_hebergement_tarifs(81)
        self.assertEqual(len(tarifs), 1)
        self.assertEqual(tarifs[0].min, 50)
