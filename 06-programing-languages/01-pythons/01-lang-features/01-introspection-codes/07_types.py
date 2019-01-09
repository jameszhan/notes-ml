# -*- coding: utf-8 -*-
import types

print("----------PRINT TYPES---------")
print(types.__doc__)
print(dir(types))

print("----------DIR BOOLEAN---------")
print(dir(True))

print("----------DIR NUMBER---------")
print(dir(68))

print("----------DIR STRING---------")
print(dir("This is a string"))

print("----------DIR ARRAY---------")
print(dir([]))

print("----------DIR TUPLE---------")
print(dir(()))

print("----------DIR DICTIONARY---------")
print(dir({}))

print("----------DIR FUNCTION---------")
print(dir(dir))

class Person:
    """Person class DOC"""
    def __init__(self):
        pass

obj = Person()
print("----------DIR OBJECT(" + Person.__doc__ + ")---------")
print(dir(obj))

class People(object):
    """People class DOC"""
    def __init__(self):
        pass

obj = People()
print("----------DIR OBJECT(" + People.__doc__ + ")---------")
print(dir(obj))

def intersection(list1, list2):
    return [x for x in list1 if x in list2]

def intersctions(*lists):
    target = []
    for i, l in enumerate(lists):
        if i == 0:
            target = l
        else:
            target = intersection(target, l)
    return target


print("----------DIR INTERSECTION---------")
print(intersctions(dir([]), dir(()), dir({}), dir(""), dir(dir), dir(True)))

