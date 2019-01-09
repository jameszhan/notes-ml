#!/usr/bin/env python

class TestClass(object):
    def __init__(self):
        super(TestClass, self).__init__()
        print('TestClass intialized')

    def member_method(self, x):
        print('member_method invoked with', x)

def func(x):
    print("Hello", x)

ATestClass = TestClass
obj = ATestClass()
obj.member_method(100)

func2 = func
func2('James')
