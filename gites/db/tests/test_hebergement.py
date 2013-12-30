# -*- coding: utf-8 -*-
import unittest2
from gites.db.testing import PGRDB
from gites.db import session
from gites.db.content import Hebergement, Proprio


class HebergementMapperTest(unittest2.TestCase):
    layer = PGRDB

    def test_simple_get(self):
        PK = 99
        heb = Hebergement(heb_pk=PK)
        sess = session()
        sess.add(heb)
        sess.flush()
        self.assertEqual(heb.heb_pk, Hebergement.first(heb_pk=PK).heb_pk)

    def test_proprio_link(self):
        PK = 98
        heb = Hebergement(heb_pk=PK, heb_pro_fk=PK)
        pro = Proprio(pro_pk=PK)
        sess = session()
        sess.add(heb)
        sess.add(pro)
        sess.flush()
        self.assertEqual(heb.proprio.pro_pk, Proprio.first(pro_pk=PK).pro_pk)
        heb = sess.query(Hebergement).first()
        heb.proprio
