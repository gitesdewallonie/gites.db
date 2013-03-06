# -*- coding: utf-8 -*-
import unittest2
import sqlalchemy
from z3c.sqlalchemy import getSAWrapper
from gites.db.testing import PGRDB
from gites.db import session
from gites.db.content import Province


class HebergementMapperTest(unittest2.TestCase):
    layer = PGRDB

    def test_simple_get(self):
        prov = Province(prov_pk=1)
        sess = session()
        sess.add(prov)
        sess.flush()

    def test_get_sa_wrapper(self):
        wrapper = getSAWrapper('gites_wallons')
        self.assertTrue(wrapper.getMapper('provinces') == Province)

    def test_get_wrong_sa_wrapper(self):
        wrapper = getSAWrapper('gites_wallons')
        with self.assertRaises(KeyError):
            wrapper.getMapper('provincesXXX')
        with self.assertRaises(KeyError):
            wrapper.getMapper('provinces')
