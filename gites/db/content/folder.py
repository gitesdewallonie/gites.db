# -*- coding: utf-8 -*-
"""
arsia.gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id$
"""
from App.class_init import InitializeClass
from AccessControl import ClassSecurityInfo
from zope.component.factory import Factory
from Products.Archetypes.ExtensibleMetadata import ExtensibleMetadata
from Products.ATContentTypes.content.folder import ATFolder
from collective.rope.folder import _my_import
from collective.rope.baseatfolder import BaseFolderMixin


def manage_addGitesRDBFolder(dispatcher, id, itemClass, sessionName='',
                             title='', REQUEST=None):
    """
    Adds a new Folder object with id *id*.
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


class GitesRDBFolder(BaseFolderMixin, ExtensibleMetadata, ATFolder):
    portal_type = meta_type = 'Gites Rope Folder'
    security = ClassSecurityInfo()
    session_name = 'pg'
    schema = BaseFolderMixin.schema + ExtensibleMetadata.schema + ATFolder.schema
    type = []

InitializeClass(GitesRDBFolder)


def _GitesRDBFolderFactory(id, itemClass, sessionName='pg', title=''):
    ob = GitesRDBFolder(id)
    ob.title = str(title)
    ob.item_class = _my_import(itemClass)
    ob.session_name = sessionName
    return ob

GitesRDBFolderFactory = Factory(_GitesRDBFolderFactory)
