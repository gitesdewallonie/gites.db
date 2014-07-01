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
        self.assertEqual(tarifs[0].pk, 2)

    def test_get_tarifs_to_confirm(self):
        tarifs = Tarifs.get_tarifs_to_confirm()
        self.assertEqual(len(tarifs), 4)
        self.assertEqual(tarifs[0].heb_pk, 81)
        self.assertEqual(tarifs[1].heb_pk, 82)
        self.assertEqual(tarifs[2].heb_pk, 83)
        self.assertEqual(tarifs[3].heb_pk, 84)

    def test_get_hebergement_tarifs_to_confirm(self):
        tarif = Tarifs.get_hebergement_tarif_to_confirm(heb_pk=83,
                                                        type='LOW_SEASON',
                                                        subtype='WEEK')
        self.assertNotEqual(tarif, None)
        self.assertEqual(tarif.pk, 6)

    def test_get_hebergement_tarif_to_confirm_with_value(self):
        tarif = Tarifs.get_hebergement_tarif_to_confirm_with_value(
            heb_pk=84,
            type='LOW_SEASON',
            subtype='WEEKEND',
            min='550',
            max='650',
            cmt=None)
        self.assertNotEqual(tarif, None)
        self.assertEqual(tarif.pk, 7)

        tarif = Tarifs.get_hebergement_tarif_to_confirm_with_value(
            heb_pk=84,
            type='LOW_SEASON',
            subtype='WEEKEND',
            min='551',
            max='651',
            cmt=None)
        self.assertEqual(tarif, None)

    def test_exists_tarifs(self):
        tarif_not_valid = Tarifs.exists_tarifs(heb_pk=84,
                                               type='LOW_SEASON',
                                               subtype='WEEKEND',
                                               min='550',
                                               max='650',
                                               cmt=None)
        self.assertEqual(tarif_not_valid, False)

        tarif_wrong_value = Tarifs.exists_tarifs(heb_pk=84,
                                                 type='LOW_SEASON',
                                                 subtype='WEEKEND',
                                                 min='251',
                                                 max='260',
                                                 cmt=None)
        self.assertEqual(tarif_wrong_value, False)

        tarif = Tarifs.exists_tarifs(heb_pk=84,
                                     type='LOW_SEASON',
                                     subtype='WEEKEND',
                                     min='250',
                                     max='260',
                                     cmt=None)
        self.assertEqual(tarif, True)

    def test_get_hebergement_tarifs_charges(self):
        """
        Get only one CHARGES even there is several active.
        Get the highest pk
        """
        tarifs = Tarifs.get_hebergement_tarifs(85)
        self.assertEqual(len(tarifs), 1)
        self.assertEqual(tarifs[0].pk, 10)
