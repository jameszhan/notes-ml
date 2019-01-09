# -*- coding: utf-8 -*-


def log(func):
    def wrapper(*args, **kv):
        print('enter: {0}, locals: {1}'.format(func.__name__, locals()))
        func(*args, **kv)
        print('exit: {0}, locals: {1}'.format(func.__name__, locals()))

    wrapper.__name__ = func.__name__
    #    wrapper.__globals__ = func.__globals__
    return wrapper

@log
def test(x, y=1, *a, **b):
    pass


test(1)
test(1, 2)
test(1, 2, 3)
test(1, 2, 3, 4)
test(1, 2, 3, 4, 5)
test(x=1, y=2)
test(1, a=2)
test(1, 2, 3, a=4)
test(1, 2, 3, u=2)
