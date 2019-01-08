#!/usr/bin/env python


class mydescriptor(object):
    def __call__(cls):
        print('new me')

    #i'm going to be bound!!!
    def __get__(self, new_self, Type = None):
        #let us bind it!!!
        print('__get__')
        return self.__call__

    #oh no.... i'm being override..
    def __set__(self, new_self, value):
        print('__set__')
        #nonono i won't
        #raise AttributeError


class host(object):
    data = mydescriptor()

    def __init__(self):
        self.data = mydescriptor()
        self.data1 = mydescriptor()


h = host()
print(h.__dict__)
h.data()
h.data1()

print('----------')


#functions are natural descriptors, cuz they have __get__
#to bind values in order
def foo_func(x, y):
    return x + 2 * y

#50
foo_func(10, 20)
#41
bar_func = foo_func.__get__(1)
bar_func(20)

