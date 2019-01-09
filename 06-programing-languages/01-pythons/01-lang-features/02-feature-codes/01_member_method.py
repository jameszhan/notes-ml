# -*- coding: utf-8 -*-

class MyClass(object):
    def __init__(self, x):
        self.x = x

    def member_method1(self):
        print(self.x)

obj = MyClass(10)

obj.member_method1()

MyClass.member_method1(obj)

