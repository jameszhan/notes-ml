# -*- coding: utf-8 -*-

import unittest
from sortedcollections import SortedList


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


if __name__ == '__main__':
    unittest.main()
