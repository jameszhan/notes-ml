#!/usr/bin/env python

class host(object):
    def __init__(self, x):
        #self is a argument!!!
        self.x = x

    def member_method1(cls):
        #see "self" is a candy...
        print cls.x

#constructed and bind our methods!!!
#call __init__ BTW
h = host(10)
#cls or self disappeared, because it has been bound
h.member_method1()
#unbound method can also be called
host.member_method1(h)

