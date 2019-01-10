# -*- coding: utf-8 -*-
import os
import sys
import logging
import unittest
import numpy as np
import matplotlib.pyplot as plt

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_path)

from gradient_descent import bgd


logger = logging.getLogger("unittestLogger")

def hypothesis(x, theta):
    return 1.0 / (1 + np.exp(-np.dot(x, theta)))

def cost(x, theta, y):
    h = hypothesis(x, theta)
    if y == 1:
        return -np.log(h)
    else:
        return -np.log(1 - h)


def predict2d(theta, x, y):
    data = [1, x, y]
    v = hypothesis(theta, data)
    print('predict ({0}, {1}) = {2}, z = {3}'.format(x, y, v, np.dot(theta, data)))
    return v

class TestLogisticGD(unittest.TestCase):

    def test_gd(self):
        m = 12
        x1 = np.linspace(0, 6, m + 1)
        x2 = np.linspace(0, 6, m + 1)
        X, Y = [], []

        for i in range(m):
            for j in range(m):
                X.append((x1[i], x2[j]))
                if x1[i] > 5 or x2[j] > 5 or x1[i] + x2[j] > 5:
                    Y.append(1)
                else:
                    Y.append(0)

        for i in range(len(X)):
            c, m = 'r', 'o'
            if Y[i] == 0:
                c, m = 'b', 'x'
            plt.scatter(X[i][0], X[i][1], c=c, marker=m)

        plt.grid(True)
        plt.show()

        theta2 = bgd(X, Y, hypothesis, cost, alpha=0.5, trace=False)
        print('theta = {0}'.format(theta2))

        self.assertGreater(predict2d(theta2, 10, 10), 0.5)
        self.assertGreater(predict2d(theta2, 10, 1), 0.5)
        self.assertGreater(predict2d(theta2, 2, 8), 0.5)
        self.assertGreater(predict2d(theta2, 5, 5), 0.5)
        self.assertGreater(predict2d(theta2, 4, 4), 0.5)
        self.assertGreater(predict2d(theta2, 3, 4), 0.5)
        self.assertGreater(predict2d(theta2, 3, 3), 0.5)
        self.assertGreater(predict2d(theta2, 2, 4), 0.5)
        self.assertGreater(predict2d(theta2, 3, 2.5), 0.5)
        self.assertGreater(predict2d(theta2, 2.5, 3), 0.5)
        self.assertLess(predict2d(theta2, 2.5, 2.5), 0.5)
        self.assertLess(predict2d(theta2, 3, 2), 0.5)
        self.assertLess(predict2d(theta2, 1, 1), 0.5)
        self.assertLess(predict2d(theta2, -3, -3), 0.5)
        self.assertLess(predict2d(theta2, -5, -5), 0.5)
        self.assertLess(predict2d(theta2, -10, -10), 0.5)

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')
    unittest.main()
