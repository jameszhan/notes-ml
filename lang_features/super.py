#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Base(object):
    def __init__(self):
        print('base.__init__')
        super(Base, self).__init__()


class Base1(Base):
    def __init__(self):
        print('base1.__init__')
        super(Base1, self).__init__()


class Base2(object):
    def __init__(self):
        print('base2.__init__')
        super(Base2, self).__init__()


class Top(Base1, Base2):
    def __init__(self):
        print('top.__init__')
        super(Top, self).__init__()


t = Top()
print(Top.__mro__)
