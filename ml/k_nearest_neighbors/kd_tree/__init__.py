# -*- coding: utf-8 -*-
import numpy as np


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

    def __lt__(self, other):
        if other is None:
            return -1
        elif other == self:
            return 0
        else:
            return 1

    def __str__(self):
        return "{0}:{1}".format(self.point, self.axis)

    def __repr__(self):
        return self.__str__()


def _preorder_traversal(node, visit):
    if node is None:
        return
    visit(node)
    _preorder_traversal(node.left_child, visit)
    _preorder_traversal(node.right_child, visit)


def _inorder_traversal(node, visit):
    if node is None:
        return
    _inorder_traversal(node.left_child, visit)
    visit(node)
    _inorder_traversal(node.right_child, visit)


def _postorder_traversal(node, visit):
    if node is None:
        return
    _postorder_traversal(node.left_child, visit)
    _postorder_traversal(node.right_child, visit)
    visit(node)


class KDTree(object):
    def __init__(self, data_list, labels=None):
        self._build(data_list, labels)

    def traversal(self, visit, kind='preorder'):
        if kind == 'inorder':
            _inorder_traversal(self.root, visit)
        elif kind == 'postorder':
            _postorder_traversal(self.root, visit)
        else:
            _preorder_traversal(self.root, visit)

    def _build(self, data_list, labels):
        if data_list is None or len(data_list) <= 0:
            self.root = None
            return

        if labels is None:
            labels = np.zeros(len(data_list))
        else:
            assert len(data_list) == len(labels)

        _data_list = np.c_[data_list, labels]

        _, n = np.shape(data_list)  # exclude label column

        def build(items, depth):
            axis, m = depth % n, len(items)
            sorted_data_list = sorted(items, key=lambda data: data[axis])
            mid = m // 2
            point = sorted_data_list[mid]
            node = KDNode(axis, point[:-1], point[-1], build(sorted_data_list[:mid], depth + 1), build(sorted_data_list[mid + 1:], depth + 1))
            if node.left_child:
                node.left_child.parent = node
            if node.right_child:
                node.right_child.parent = node
            return node

        self.root = build(_data_list, depth=0)
