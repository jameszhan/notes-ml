# -*- coding: utf-8 -*-
import os
import sys
import logging
import unittest
import numpy as np
import matplotlib.pyplot as plt

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_path)

from linear_gd2 import linear_gd


logger = logging.getLogger("unittestLogger")


class TestLinearGD(unittest.TestCase):

    def test_gd(self):
        X = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        Y = [0.199, 0.389, 0.580, 0.783, 0.980, 1.177, 1.380, 1.575, 1.771]

        theta = linear_gd(X, Y, 0.05, 1e-6)
        logger.info("theta = {}".format(theta))

        b, a = theta

        logger.info('y = {0} * x + {1}'.format(a, b))

        x = np.array(X)
        plt.plot(x, Y, 'o', label='Original data', markersize=5)
        plt.plot(x, a * x + b, 'r', label='Fitted line')
        plt.show()


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')
    unittest.main()
