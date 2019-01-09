# -*- coding: utf-8 -*-

print(issubclass.__doc__)

class Person(object):
    def __init__(self):
        pass

class SuperHero(Person):
    pass

print(issubclass(SuperHero, Person))
print(issubclass(Person, SuperHero))

print(SuperHero.__mro__)

