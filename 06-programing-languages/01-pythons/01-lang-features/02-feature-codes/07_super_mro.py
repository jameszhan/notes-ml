# -*- coding: utf-8 -*-

class Base(object):
    def __init__(self):
        super(Base, self).__init__()
        print('base.__init__')

class Base1(Base):
    def __init__(self):
        super(Base1, self).__init__()
        print('base1.__init__')

class Base2(object):
    def __init__(self):
        super(Base2, self).__init__()
        print('base2.__init__')

class Top(Base1, Base2):
    def __init__(self):
        super(Top, self).__init__()
        print('top.__init__')
        

t = Top()
print(Top.__mro__)
