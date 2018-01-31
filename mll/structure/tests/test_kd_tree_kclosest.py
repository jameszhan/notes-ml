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
figure = plt.figure(figsize=(10, 10))
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
    ax.text(point[0] - 0.35, point[1] - 0.25, "({0}, {1})".format(*point), color='g', alpha=0.8)
    ax.scatter(*point, c=c, marker='*', s=30, alpha=0.7)
    i = 10
    for d, _ in visited_nodes:
        alpha = 0.1 * i
        if alpha <= 0:
            alpha = 0.1
        ax.add_patch(Circle(point, d, color=c, fill=False, alpha=alpha))
        i -= 2


class TestKDTree2d(unittest.TestCase):

    # def test_visualization(self):
    #     points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
    #     tree = KDTree(points)
    #
    #     tree.traversal(draw_point, 'preorder')
    #     show_closest(tree, (2.3, 3.3), 3, 'r')
    #     # show_closest(self.tree, (2.0, 4.5), 3, 'g')
    #     # show_closest(self.tree, (7.5, 5.0), 3, 'b')
    #     plt.show()

    def test_random(self):
        count, sigma1, sigma2 = 50, 0.6, 0.5

        np.random.seed(0)
        x1 = np.random.normal(5, sigma1, count)
        y1 = np.random.normal(5, sigma2, count)

        x2 = np.random.normal(3, sigma1, count)
        y2 = np.random.normal(4, sigma2, count)

        x3 = np.random.normal(4.5, sigma1, count)
        y3 = np.random.normal(2.5, sigma2, count)

        point = [np.random.normal(5, 0.6), np.random.normal(5, 0.5)]

        ax.scatter(x1, y1, c='b', marker='s', s=10, alpha=0.7)
        ax.scatter(x2, y2, c='r', marker='^', s=10, alpha=0.7)
        ax.scatter(x3, y3, c='g', s=10, alpha=0.7)

        ax.scatter(*point, c='m', marker='*', s=100, alpha=1.0)

        points = np.c_[np.r_[x1, x2, x3], np.r_[y1, y2, y3]]

        tree = KDTree(points)
        show_closest(tree, point, 2, 'm')
        plt.show()


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

    unittest.main()
