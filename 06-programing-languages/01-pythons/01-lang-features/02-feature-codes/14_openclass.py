# -*- coding: utf8 -*-
__author__ = 'james'

class Base(object):
    def hello(self, name):
        return "hello %s" % name

    def world(self):
        return "James's world"
        

if __name__ == '__main__': 
    b = Base()
    print(b.hello('James'))
    
    def hw(self):
        return "hello world!"
        
    Base.hw = hw    
    print(b.hw())
    
    def hw1():
        return 'hw1'
    
    b.hw1 = hw1
    print(b.hw1())
    
    b2 = Base()
    print(b2.hw())
    #print(b2.hw1()) // Not Found!

    class int(int):
        def square(self):
            return self * self
    
    print(int(3).square())