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


def show_closest(tree, point, c):
    dist, node, _, visited_nodes = tree.closest(point)
    ax.text(point[0] - 0.35, point[1] - 0.25, "({0}, {1})".format(*point), color='g', alpha=0.8)
    ax.scatter(*point, c=c, marker='*', s=30, alpha=0.7)
    print("draw circle with radius {0}".format(dist))
    i = 10
    for d, _ in visited_nodes:
        alpha = 0.1 * i
        ax.add_patch(Circle(point, d, color=c, fill=False, alpha=alpha))
        i -= 2


class TestKDTree2d(unittest.TestCase):
    def setUp(self):
        points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
        self.tree = KDTree(points)

    def test_traversal(self):
        logger.info("PreOrder:")
        self.tree.traversal(lambda n: logger.info(n), "preorder")
        logger.info("InOrder:")
        self.tree.traversal(lambda n: logger.info(n), "inorder")
        logger.info("PostOrder:")
        self.tree.traversal(lambda n: logger.info(n), "postorder")

    def test_closest(self):
        dist, node, count, nodes = self.tree.closest((2.3, 3.3))
        logger.info("dist = {0}, node = {1}, visit_count = {2}".format(dist, node, count))
        logger.info("visited nodes = {0}".format(nodes))

        dist, node, count, nodes = self.tree.closest((2, 4.5))
        logger.info("dist = {0}, node = {1}, visit_count = {2}".format(dist, node, count))
        logger.info("visited nodes = {0}".format(nodes))

        dist, node, count, nodes = self.tree.closest((7.5, 5))
        logger.info("dist = {0}, node = {1}, visit_count = {2}".format(dist, node, count))
        logger.info("visited nodes = {0}".format(nodes))

    def test_visualization(self):
        self.tree.traversal(draw_point, 'preorder')
        show_closest(self.tree, (2.3, 3.3), 'r')
        show_closest(self.tree, (2.0, 4.5), 'g')
        show_closest(self.tree, (7.5, 5.0), 'b')
        plt.show()


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

    unittest.main()
