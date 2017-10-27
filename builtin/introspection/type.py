# -*- coding: utf-8 -*-

import types

print "----------PRINT TYPES---------"
print types.__doc__
print dir(types)

print "----------TYPE BOOLEAN---------"
print type(True)

print "----------TYPE NUMBER---------"
print type(68)

print "----------TYPE STRING---------"
print type("This is a string")

print "----------TYPE ARRAY---------"
print type([])

print "----------TYPE TUPLE---------"
print type(())

print "----------TYPE DICTIONARY---------"
print type({})

print "----------TYPE FUNCTION---------"
print type(dir)

class Person:
    """Person class DOC"""
    def __init__(self):
        pass

obj = Person()
print "----------DIR OBJECT(" + Person.__doc__ + ")---------"
print type(obj)