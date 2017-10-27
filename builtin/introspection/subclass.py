# -*- coding: utf-8 -*-

print issubclass.__doc__


class Person(object):
    def __init__(self):
        pass


class SuperHero(Person):
    def intro(self):
        """Return an introduction."""
        return "Hello, I'm SuperHero %s and I'm %s." % (self.name, self.age)


print issubclass(SuperHero, Person)

print issubclass(Person, SuperHero)

