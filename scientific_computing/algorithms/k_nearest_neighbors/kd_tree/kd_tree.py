# -*- coding: utf-8 -*-
import numpy as np
import heapq
import logging
from sortedcollections import SortedListWithKey

logger = logging.getLogger("KDTree")


class KDNode(object):
    def __init__(self, axis, point, label=None, left_child=None, right_child=None, parent=None):
        self.axis = axis
        self.point = point
        self.label = label
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def is_leaf(self):
        return self.left_child is None and self.right_child is None

    def __str__(self):
        return "{0}:{1}".format(self.point, self.axis)

    def __repr__(self):
        return self.__str__()


def metric(x1, x2):
    return np.linalg.norm(np.subtract(x1, x2), ord=2)


def _kd_tree(_data_list, depth):
    if len(_data_list) <= 0:
        return None
    m, n = np.shape(_data_list)
    axis = depth % (n - 1)  # exclude label
    # _data_list.sort(key=lambda data: data[axis])
    sorted_data_list = sorted(_data_list, key=lambda data: data[axis])
    mid = m // 2
    point = sorted_data_list[mid]
    node = KDNode(axis, point[:-1], point[-1], _kd_tree(sorted_data_list[:mid], depth + 1), _kd_tree(sorted_data_list[mid + 1:], depth + 1))
    if node.left_child:
        node.left_child.parent = node
    if node.right_child:
        node.right_child.parent = node
    return node


def kd_tree(data_list, labels, depth=0):
    assert len(data_list) == len(labels)
    return _kd_tree(np.c_[data_list, labels], depth)


def preorder_traversal(root, handle):
    if root:
        handle(root)
    else:
        return
    preorder_traversal(root.left_child, handle)
    preorder_traversal(root.right_child, handle)


def midorder_traversal(root, handle):
    if root is None:
        return
    midorder_traversal(root.left_child, handle)
    handle(root)
    midorder_traversal(root.right_child, handle)


def _handle_node(heap, k, distance, node):
    largest_item = heapq.nlargest(1, heap)
    largest_distance = np.inf
    if largest_item:
        largest_distance, _ = largest_item[0]
    if len(heap) < k or distance < largest_distance:
        logger.debug("% heappush {0} to {1}.".format((distance, node), heap))
        heapq.heappush(heap, (distance, node))
    else:
        logger.debug("ignore node {0}".format(node.point))


def closest(root, point, k=1):
    candidates = SortedListWithKey(key=lambda v: v[0])

    def current_max():
        candidates_len = len(candidates)
        if candidates_len >= k:
            return candidates[k - 1][0]
        elif candidates_len > 0:
            return candidates[-1][0]
        else:
            return np.inf

    def travel(node):
        logger.debug("visit {0}".format(node))
        if node is None:
            return 0

        nodes_visited = 1

        axis = node.axis
        if point[axis] < node.point[axis]:
            nearer_node = node.left_child
            further_node = node.right_child
        else:
            nearer_node = node.right_child
            further_node = node.left_child

        nodes_visited += travel(nearer_node)

        max_dist = current_max()
        axis_dist = np.abs(node.point[axis] - point[axis])
        logger.debug("axis: {0}, distance: {1}, point: {2}".format(axis, axis_dist, node))
        if max_dist < axis_dist and len(candidates) >= k:
            return nodes_visited
        else:
            current_dist = metric(node.point, point)
            logger.debug("append candidate {0} with distance {1}".format(node, current_dist))
            candidates.add((current_dist, node))

            nodes_visited += travel(further_node)
            return nodes_visited

    visit_count = travel(root)
    logger.info("expected {0}, touched {1}, candidates: {2}".format(k, visit_count, len(candidates)))
    return candidates[0:k], visit_count, candidates


if __name__ == '__main__':
    import sys
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

    points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2), (6, 3), (7, 0), (8, 5)]
    tree = kd_tree(points, [1] * len(points))

    print("Pre Order:")
    preorder_traversal(tree, lambda x: print(x))
    print("Mid Order:")
    midorder_traversal(tree, lambda x: print(x))

    point = (2.1, 3.1)

    figure = plt.figure(figsize=(10, 10))

    ax = figure.add_subplot(111, aspect=True)
    # ax.grid(True)
    figure.subplots_adjust(left=0.05, bottom=0.05, right=0.99, top=0.99, wspace=None, hspace=None)

    colors = ['r', 'b', 'g', 'y', 'm', 'c', 'k']

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

    preorder_traversal(tree, draw_point)
    ax.scatter(*point, c='b', marker='*', s=30, alpha=0.7)


    def show_closest(k):
        closest_points, _, _ = closest(tree, point, k=k)
        max_dist = closest_points[-1][0]
        print("draw circle with radius {0}".format(max_dist))
        for d, node in closest_points:
            print("point = {0}, distance = {1}".format(node, d))
            ax.add_patch(Circle(point, d, color='m', fill=False, alpha=0.5))


    show_closest(1)

    plt.show()


