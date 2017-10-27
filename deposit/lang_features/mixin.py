#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'james'


class Chocolate(object):
    def __init__(self):
        super(Chocolate, self).__init__()
        print 'inited'

    def color(self):
        return 'black'

    def taste(self):
        return 'sweet'

    
class Peanuts(object):
    def __init__(self):
        super(Peanuts, self).__init__()
        print 'inited'

    def color(self):
        return 'light yellow'

    def feel(self):
        return 'crispy'


class Mixed(Peanuts, Chocolate):
    def __init__(self):
        super(Mixed, self).__init__()
    pass

if __name__ == '__main__':
    m = Mixed()
    print m.color()
    print m.taste()
    print m.feel()


class C7(object):
    def test(self):
        print('test in C7')


class C4(C7):
    def test(self):
        print('test in C4')


class C5(C7):
    def test(self):
        print('test in C5')


class C6(C7):
    def test(self):
        print('test in C6')


class C2(C4, C5):
    def test(self):
        print('test in C2')


class C3(C4, C6):
    pass


class C1(C2, C3):
    pass


class C0(C2, C3):
    def test(self):
        print('test in C0')
        super(C3,self).test()


if __name__ == '__main__':
    c1 = C1()
    c1.test()
    c0 = C0()
    c0.test()
