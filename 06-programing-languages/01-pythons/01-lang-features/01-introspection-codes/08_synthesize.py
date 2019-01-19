# -*- coding: utf-8 -*-

class partial:

    def __new__(*args):
        if not args:
            raise TypeError("descriptor '__new__' of partial needs an argument")
        if len(args) < 2:
            raise TypeError("type 'partial' takes at least one argument")
        cls, func, *funcargs = args
        if not callable(func):
            raise TypeError("the first argument must be callable")
        args = tuple(funcargs)

        self = super(partial, cls).__new__(cls)

        self.func = func
        self.funcargs = funcargs
        return self
    
    def __call__(*args):
        if not args:
            raise TypeError("descriptor '__call__' of partial needs an argument")
        self, *args = args
        return self.func(*self.funcargs, *args)

def add(a, b):
    return a + b

plus3 = partial(add, 3)

print(plus3(5))