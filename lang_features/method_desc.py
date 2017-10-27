#!/usr/bin/env python

#staticmethod and classmethod are build-in descriptor

class class1(object):
    def __del__(self):
        print 'del'
        
    def do_something(x):
        print x

    do_something = staticmethod(do_something)

    def do_smth(self):
        print self, 'do it'

    do_smth = classmethod(do_smth)

instance = class1()

#these doesn't make any difference...
instance.do_smth()
class1.do_something(10)

#call unbound method ....error
#class1.do_smth(instance)
class1.do_smth()#this calls with the static method...

#call static with self like x.... error
#instance.do_something()
instance.do_something(10)#is equivalent with class1.do_something(10)

