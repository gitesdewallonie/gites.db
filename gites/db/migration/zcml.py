# -*- coding: utf-8 -*-
"""
arsia.db.migration

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id$
"""
from zope.configuration import xmlconfig
import gites.db as package


def parseZCML(package=package):
    context = xmlconfig._getContext()
    xmlconfig.include(context, 'configure.zcml', package)
    context.execute_actions()
