# -*- coding: utf-8 -*-

import logging
import unittest
import itertools

logger = logging.getLogger("unittestLogger")

class TestPythonTrick(unittest.TestCase):

    def test_product(self):
        arrays = itertools.product(['a', 'b', 'c'], [1, 2], ['x', 'y'])
        strings = [''.join(map(lambda x: str(x), array)) for array in arrays]
        expects = ['a1x', 'a1y', 'a2x', 'a2y', 'b1x', 'b1y', 'b2x', 'b2y', 'c1x', 'c1y', 'c2x', 'c2y']
        self.assertEqual(expects, strings)

    def test_groupby(self):
        groups = itertools.groupby(sorted(["cat", "dog", "chick", "duck", "cow"]), key=lambda x: x[0])
        expects = {
            'c': ['cat', 'chick', 'cow'],
            'd': ['dog', 'duck']
        }
        for g, members in groups:
            self.assertEqual(expects[g], list(members))
            
if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    unittest.main()


