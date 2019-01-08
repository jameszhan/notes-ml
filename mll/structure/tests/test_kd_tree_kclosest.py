# -*- coding: utf-8 -*-
import os
import sys
import logging
import unittest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_path)

from kd_tree import KDTree

logger = logging.getLogger("unittestLogger")

colors = ['r', 'b', 'g', 'y', 'm', 'c', 'k']
figure = plt.figure(figsize=(12, 8))
ax = figure.add_subplot(111, aspect=True)
ax.grid(True)
figure.subplots_adjust(left=0.05, bottom=0.05, right=0.99, top=0.99, wspace=None, hspace=None)


def draw_point(n):
    if n.is_leaf():
        marker = 'o'
    else:
        marker = 's'
    color = colors[n.axis]
    ax.scatter(*n.point, c=color, marker=marker, s=30, alpha=0.8)
    ax.text(n.point[0] - 0.36, n.point[1] - 0.25, "({0}, {1})".format(*n.point), color='g', alpha=0.8)

    _x = np.linspace(0, 10, 10)
    _y = np.linspace(0, 10, 10)

    pn = n.parent
    if n.axis == 0:
        if pn:
            if n.point[1] < pn.point[1]:
                _y = np.linspace(0, pn.point[1], 10)
            else:
                _y = np.linspace(pn.point[1], 10, 10)
        ax.plot([n.point[0]] * 10, _y, c=color, label='Splitter', alpha=0.5)
    else:
        if pn:
            if n.point[0] < pn.point[0]:
                _x = np.linspace(0, pn.point[0], 10)
            else:
                _x = np.linspace(pn.point[0], 10, 10)
        ax.plot(_x, [n.point[1]] * 10, c=color, label='Splitter', alpha=0.5)


def show_closest(tree, point, k, c):
    nodes, count, visited_nodes = tree.kclosest(point, k)
    ax.scatter(*point, c=c, marker='*', s=10, alpha=0.7)
    logger.info("expected {0}, touched {1}, candidates: {2}".format(len(nodes), count, len(visited_nodes)))
    i = 10
    for d, _ in nodes:
        alpha = 0.1 * i
        if alpha <= 0:
            alpha = 0.1
        logger.info("draw circle with radius {0} with point {1}".format(d, point))
        ax.add_patch(Circle(point, d, color=c, fill=False, alpha=alpha))
        i -= 2


class TestKDTree2d(unittest.TestCase):

    def test_random(self):
        count, sigma1, sigma2 = 10000, 0.6, 0.5

        np.random.seed(0)
        x = np.random.normal(3, sigma1, count)
        y = np.random.normal(3, sigma2, count)

        point = [3.01, 3.01]
        for i in range(count):
            if 2.98 < x[i] < 3.03 and 2.98 < y[i] < 3.03:
                ax.scatter(x[i], y[i], c='b', marker='s', s=10, alpha=0.7)
        # ax.scatter(x, y, c='b', marker='s', s=10, alpha=0.7)
        points = np.c_[x, y]

        tree = KDTree(points)
        show_closest(tree, point, 50, 'm')
        plt.show()


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

    unittest.main()
