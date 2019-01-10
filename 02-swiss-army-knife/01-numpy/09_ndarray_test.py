# -*- coding: utf-8 -*-

import logging
import unittest
import numpy as np

logger = logging.getLogger("unittestLogger")


class TestNumpyArray(unittest.TestCase):

    def test_slice(self):
        a = np.arange(0, 64)
        a.shape = (4, 4, 4)
        logger.info("Array is {0}".format(a))

        self.assertEqual(63, a.item(63))
        self.assertEqual(63, a[3, 3, 3])
        self.assertEqual(22, a[1, 1, 2])

        a0_4_2 = [[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
                  [[32, 33, 34, 35], [36, 37, 38, 39], [40, 41, 42, 43], [44, 45, 46, 47]]]
        self.assertTrue(np.all(a0_4_2 == a[0:4:2]))
        a0_4_2_0_4_2 = [[[0, 1, 2, 3], [8, 9, 10, 11]], [[32, 33, 34, 35], [40, 41, 42, 43]]]
        self.assertTrue(np.array_equal(a0_4_2_0_4_2, a[0:4:2, 0:4:2]), "actual is {0}".format(a[0:4:2, 0:4:2]))
        self.assertTrue(np.array_equal([[[0, 2], [8, 10]], [[32, 34], [40, 42]]], a[0:4:2, 0:4:2, 0:4:2]),
                        "actual is {0}".format(a[0:4:2, 0:4:2, 0:4:2]))

    def test_index(self):
        a = np.arange(0, 100, 10)
        self.assertTrue(np.array_equal([10, 30, 50], a[[1, 3, 5]]))


if __name__ == '__main__':
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    unittest.main()
