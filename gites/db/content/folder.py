# -*- coding: utf-8 -*-
"""
arsia.gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id$
"""
from collective.rope.folder import _my_import
from collective.rope.baseatfolder import BaseFolderMixin
from Products.Archetypes.ExtensibleMetadata import ExtensibleMetadata
from AccessControl import ClassSecurityInfo
from App.class_init import InitializeClass
from zope.component.factory import Factory
from Products.ATContentTypes.content.folder import ATFolderSchema

_marker = object()


def manage_addGitesRDBFolder(dispatcher,
                             id,
                             itemClass,
                             sessionName='',
                             title='',
                             REQUEST=None):
    """Adds a new Folder object with id *id*.
    """
    id = str(id)
    ob = GitesRDBFolder(id)
    ob.title = str(title)
    ob.item_class = _my_import(itemClass)
    ob.session_name = str(sessionName)
    dispatcher._setObject(id, ob)
    ob = dispatcher._getOb(id)
    if REQUEST is not None:
        return dispatcher.manage_main(dispatcher, REQUEST, update_menu=1)

GitesRDBFolderSchema = ATFolderSchema.copy()


class GitesRDBFolder(BaseFolderMixin, ExtensibleMetadata):
    meta_type = 'Gites Rope Folder'
    security = ClassSecurityInfo()
    schema = GitesRDBFolderSchema
    type = []

InitializeClass(GitesRDBFolder)


def _GitesRDBFolderFactory(id, itemClass, sessionName='', title=''):
    ob = GitesRDBFolder(id)
    ob.title = str(title)
    ob.item_class = _my_import(itemClass)
    ob.session_name = sessionName
    return ob

GitesRDBFolderFactory = Factory(_GitesRDBFolderFactory)
