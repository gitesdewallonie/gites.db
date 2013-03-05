# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy.util._collections import immutabledict
from sqlalchemy import PickleType
from sqlalchemy.dialects.sqlite.pysqlite import SQLiteDialect_pysqlite as SQLiteDialect
from sqlalchemy.ext.declarative import DeferredReflection


def makeDictionary():
    return {}


def compareDictionary(x, y):
    return x == y


PickleDict = PickleType(comparator=compareDictionary)


def get_fk_with_schema(table):
    """ Returns a list with the foreign keys that depend on a schema """
    fk_list = []
    for col in [c for c in table.columns if c.foreign_keys]:
        fk_list.extend(
            [f for f in col.foreign_keys if len(f._colspec.split('.')) > 2])
    return fk_list


def declaratives_mappers(metadata):
    # http://stackoverflow.com/questions/8956928/how-to-iterate-through-every-class-declaration-descended-from-a-particular-base/8957113#8957113
    #
    from z3c.sqlalchemy.mapper import MappedClassBase
    import gc
    all_refs = gc.get_referrers(MappedClassBase)
    results = []
    for obj in all_refs:
        # __mro__ attributes are tuples
        # and if a tuple is found here, the given class is one of its members
        if (isinstance(obj, tuple) and
            # check if the found tuple is the __mro__ attribute of a class
            getattr(obj[0], "__mro__", None) is obj):
            results.append(obj[0])
    for klass in results:
        if hasattr(klass, '__table__') and \
           klass.__table__ in metadata.tables.values():
            yield klass


def initialize_declarative_mappers(declarativebase, metadata):
    # Avoid troubles with sqlite and the schemas
    tables = dict(declarativebase.metadata.tables)
    # Extends the metadata from the model
    new_tables = dict(metadata.tables)
    for table_key, table in tables.items():
        table.metadata = metadata
        new_tables[table_key] = table
    metadata.tables = immutabledict(new_tables)
    for mapper in declaratives_mappers(metadata):
        # Ensure that a primary mapper is defined
        if not isinstance(metadata.bind.dialect, SQLiteDialect) and \
           issubclass(mapper, DeferredReflection):
            mapper.prepare(metadata.bind)
        elif not hasattr(mapper, '__mapper__') or \
            mapper.__mapper__ is not mapper.__mapper__.class_manager.mapper:
            mapper.__mapper__ = sqlalchemy.orm.mapper(mapper,
                                                        mapper.__table__)
