# -*- coding: utf-8 -*-

import unittest
from sortedcollections import *


###
# conda install -n python3 sortedcollections
###
class TestSortedList(unittest.TestCase):

    def test_sorted_list(self):
        sl = SortedList()
        self.assertEqual(0, len(sl))
        sl.update([3, 1, 2])
        print("sorted_list = {0}".format(sl))
        self.assertEqual([1, 2, 3], sl)
        sl.add(6)
        sl.add(5)
        self.assertEqual([1, 2, 3, 5, 6], sl)

    def test_sorted_list_with_key(self):
        slwk = SortedListWithKey(key=lambda v: v[1])
        self.assertEqual(0, len(slwk))
        slwk.update([(3, 2), (1, 3), (2, 1)])
        print("sorted_list = {0}".format(slwk))


if __name__ == '__main__':
    unittest.main()
