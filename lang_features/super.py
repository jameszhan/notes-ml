#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Base(object):
    def __init__(self):
        print('Base')
        super(Base, self).__init__()


class Base1(Base):
    def __init__(self):
        print('base1')
        super(Base1, self).__init__()


class Base2(object):
    def __init__(self):
        print('base2')
        super(Base2, self).__init__()


class Top(Base1, Base2):
    def __init__(self):
        print('top')
        super(Top, self).__init__()


t = Top()
print(Top.__mro__)
