# -*- coding: utf-8 -*-
from sqlalchemy import PickleType

def makeDictionary():
    return {}


def compareDictionary(x, y):
    return x == y

PickleDict = PickleType(comparator=compareDictionary)
