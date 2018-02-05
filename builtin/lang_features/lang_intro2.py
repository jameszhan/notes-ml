#!/usr/bin/env python

class testclass(object):
    def __init__(self):
        super(testclass, self).__init__()
        print 'construct'

    def member_method(self):
        print 'member method'

def func(x):
    print x

#now we do the magic....
#class definations are instance!!!
atestclass = testclass
t = atestclass()
t.member_method()

#functions are functors...
f = func;
f('hello mars')
