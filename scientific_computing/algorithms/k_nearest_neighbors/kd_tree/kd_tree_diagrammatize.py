# -*- coding: utf-8 -*-
import numpy as np
import logging
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import kd_tree as kd

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]

tree = kd.kd_tree(points, [1] * len(points))

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
    ax.scatter(*n.point, c=color, marker=marker, s=100, alpha=0.8)
    plt.text(n.point[0] - 0.2, n.point[1] - 0.2, "({0}, {1})".format(*n.point), color='g', alpha=0.8)

    _x = np.linspace(0, 10, 10)
    _y = np.linspace(0, 10, 10)

    pn = n.parent
    if n.axis == 0:
        if pn:
            if n.point[1] < pn.point[1]:
                _y = np.linspace(0, pn.point[1], 10)
            else:
                _y = np.linspace(pn.point[1], 10, 10)
        plt.plot([n.point[0]] * 10, _y, c=color, label='Splitter', alpha=0.5)
    else:
        if pn:
            if n.point[0] < pn.point[0]:
                _x = np.linspace(0, pn.point[0], 10)
            else:
                _x = np.linspace(pn.point[0], 10, 10)
        plt.plot(_x, [n.point[1]] * 10, c=color, label='Splitter', alpha=0.5)


def show_closest(point, k, c):
    closest_points = kd.closest(tree, point, k=k)
    max_dist = closest_points[-1][0]
    plt.text(point[0] - 0.3, point[1] - 0.2, "({0}, {1})".format(*point), color='g', alpha=0.8)
    ax.scatter(*point, c=c, marker='*', s=30, alpha=0.7)
    print("draw circle with radius {0}".format(max_dist))
    for d, node in closest_points:
        print("point = {0}, distance = {1}".format(node, d))
        ax.add_patch(Circle(point, d, color=c, fill=False, alpha=0.5))


kd.preorder_traversal(tree, draw_point)
# show_closest((2.3, 3.3), 1, 'm')
# show_closest((2, 4.5), 1, 'y')
show_closest((7.5, 5), 1, 'y')


plt.show()
