# -*- coding: utf8 -*-
__author__ = 'james'


def hi(name):
    return "hello %s" % name


class Base(object):
    def __init__(self):
        self.x = 'x'
        self.y = 'y'
        self.z = 'z'
        
    def __getattr__(self, name):
        if name == 'hello':
            l = lambda x: x + 1
            self.__setattr__(name, l)
            return l
        elif name == 'world':
            return hi
        else: 
            raise AttributeError(name)
            pass


class Hasie(object):
    def __init__(self, _hash):
        self.hash = _hash

    def __getattr__(self, name):
        if name in self.hash:
            func = lambda: self.hash[name]
            self.__setattr__(name, func)
            return func
        else:
            raise AttributeError(name)


if __name__ == '__main__': 
    b = Base()
    print(b.x, b.y, b.z)
    print(b.hello(1))
    print(b.world('James'))    
    # print(b.a)

    hash = {'a': 1, 'b': 2}
    h = Hasie(hash)
    print(h.a())
    print(h.b())