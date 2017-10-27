#!/usr/bin/env python


class testclass(object):
    def __init__(self):
        self.x = 10
        
    def method(self):
        pass
    x = 10
    y = []


t = testclass()
print t.__dict__
print testclass.__dict__
