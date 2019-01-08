#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseClass(object):
    myvar = 1
    mybasevar = 1


class AttributeLookup(BaseClass):
    def foo_func(self):
        pass

    def foo_func(self, x):
        pass

    myvar = []


attr = AttributeLookup()
attr.myvar2 = 1

print AttributeLookup.__dict__
print attr.__dict__

print AttributeLookup.__mro__
