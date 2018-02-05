# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Circle
from kd_tree import kd_tree, closest, preorder_traversal

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

figure = plt.figure(figsize=(10, 10))

ax = figure.add_subplot(111, aspect=True)
ax.grid(True)
figure.subplots_adjust(left=0.05, bottom=0.05, right=0.99, top=0.99, wspace=None, hspace=None)

count, sigma1, sigma2 = 10, 0.6, 0.5

np.random.seed(0)
x1 = np.random.normal(5, sigma1, count)
y1 = np.random.normal(5, sigma2, count)

x2 = np.random.normal(3, sigma1, count)
y2 = np.random.normal(4, sigma2, count)

x3 = np.random.normal(4.5, sigma1, count)
y3 = np.random.normal(2.5, sigma2, count)

ax.scatter(x1, y1, c='b', marker='s', s=10, alpha=0.7)
ax.scatter(x2, y2, c='r', marker='^', s=10, alpha=0.7)
ax.scatter(x3, y3, c='g', s=10, alpha=0.7)

point = [np.random.normal(5, 0.6), np.random.normal(5, 0.5)]

ax.scatter(*point, c='m', marker='*', s=100, alpha=1.0)

points = np.c_[np.r_[x1, x2, x3], np.r_[y1, y2, y3]]
tree = kd_tree(points, [1] * count + [2] * count + [3] * count)

colors = ['r', 'y', 'g', 'b', 'm', 'c', 'k']


def show_closests(k, i):
    closest_points = closest(tree, point, k=k)
    max_dist = closest_points[-1][0]
    print("draw circle with radius {0}".format(max_dist))
    for d, node in closest_points:
        print("point = {0}, distance = {1}".format(node, d))
        ax.add_patch(Circle(point, d, color=colors[i % len(colors)], fill=False))


# show_closests(1, 0)
show_closests(3, 1)
# show_closests(10, 2)
# show_closests(50, 3)
# show_closests(100, 4)
# show_closests(200, 5)
# show_closests(300, 5)

plt.show()
