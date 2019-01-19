# -*- coding: utf-8 -*-

import logging
import unittest
import functools

logger = logging.getLogger("unittestLogger")

def add(a, b):
    """ Calculate the square of the given number. """
    return a + b

def trace(func):
    def callit(*args, **kwargs):
        """A wrapper function."""
        logger.info('Before call {}\n'.format(func.__name__))
        ret = func(*args, **kwargs)
        logger.info('After call {} and get {}\n'.format(func.__name__, ret))
        return ret
    return callit

def trace2(func):
    @functools.wraps(func)
    def callit(*args, **kwargs):
        """A wrapper function."""
        logger.info('Before call {}\n'.format(func.__name__))
        ret = func(*args, **kwargs)
        logger.info('After call {} and get {}\n'.format(func.__name__, ret))
        return ret
    return callit

@trace
def square(x):
    """Calculate the square of the given number."""
    return x * x

@trace2
def square2(x):
    """Calculate the square of the given number."""
    return x * x

class TestFunctools(unittest.TestCase):

    def test_partial(self):
        plus3 = functools.partial(add, 3)
        plus5 = functools.partial(add, 5)

        self.assertEqual(5, plus3(2))
        self.assertEqual(8, plus5(3))

    def test_wrapper(self):
        help(square)
        logger.info("square.__name__ is {}.".format(square.__name__))
        logger.info("square.__doc__ is {}.".format(square.__doc__))

        help(square2)
        logger.info("square2.__name__ is {}.".format(square2.__name__))
        logger.info("square2.__doc__ is {}.".format(square2.__doc__))



if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    unittest.main()


