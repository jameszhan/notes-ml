# -*- coding: utf8 -*-
__author__ = 'james'

"""
'__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', 
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__'
"""


class Base(object):
    def __getattr__(self, name):
        print("__getattr__", self, name)
        return name + " from getattr" 
    
    def __getattribute__(self, *args):
        print "{0}.__getattribute__({1})".format( self, *args)
        return super(Base, self).__getattribute__(*args)
    
    def __get__(self, instance, owner):
        print "{0}.__get__({1}, {2})".format(self, instance, owner)
        return self


class Other(object):  
    b = Base()


if __name__ == '__main__':
    print("dir(base) => ", dir(Base))    
    print("Base.__hash__ => ", Base.__hash__)
    print('\n\n')
    b = Base()
    print("dir(b) => ", dir(b))
    print("b.__hash__ => ", b.__hash__)
    
    print("\n\n")
    print("------------------------")
    print(b.x)

    o = Other()  
    print o.b
    print(o.b.a)

