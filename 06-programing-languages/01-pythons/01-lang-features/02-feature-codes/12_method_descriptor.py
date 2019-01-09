# -*- coding: utf-8 -*-

# staticmethod and classmethod are build-in descriptor
class Class1(object):
    def __del__(self):
        print('del Class1')
        
    def do_something(x):
        print(x)

    do_something = staticmethod(do_something)

    def do_smth(self):
        print(self, 'do it')

    do_smth = classmethod(do_smth)

class Class2(object):
    def __del__(self):
        print('del Class2')
        
    @staticmethod
    def do_something(x):
        print(x)

    @classmethod
    def do_smth(self):
        print(self, 'do it')

obj1 = Class1()

obj1.do_something(10)
Class1.do_something(10)

obj1.do_smth()
Class1.do_smth()

obj2 = Class2()

obj2.do_something(10)
Class2.do_something(10)

obj2.do_smth()
Class2.do_smth()

