# -*- coding: utf-8 -*-
import numpy as np
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


def default_get_distince(x1, x2):
    return np.linalg.norm(np.subtract(x1, x2), ord=2)


class KDTree(object):
    def __init__(self, data_list, labels=None, metric=default_get_distince):
        self.metric = metric
        self._build(data_list, labels)

    def kclosest(self, point, k=1):
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
                current_dist = self.metric(node.point, point)
                logger.debug("append candidate {0} with distance {1}".format(node, current_dist))
                candidates.add((current_dist, node))

                nodes_visited += travel(further_node)
                return nodes_visited

        if k == 1:
            closest_dist, closest_node, visit_count, visited_nodes = self.closest(point)
            return [(closest_dist, closest_node)], visit_count, visited_nodes
        else:
            visit_count = travel(self.root)
            logger.info("expected {0}, touched {1}, candidates: {2}".format(k, visit_count, len(candidates)))
            return candidates[0:k], visit_count, candidates

    def closest(self, point):
        candidates = []

        def travel(node, init_dist):
            logger.debug("enter visit {0}, dist: {1}".format(node, init_dist))
            if node is None:
                return np.inf, node, 0

            closest_dist, closest_node, nodes_visited = init_dist, node, 1

            axis = node.axis
            if point[axis] < node.point[axis]:
                nearer_node = node.left_child
                further_node = node.right_child
            else:
                nearer_node = node.right_child
                further_node = node.left_child

            tmp_dist, tmp_node, touched = travel(nearer_node, init_dist)            # 查找临近子树的最近节点
            nodes_visited += touched

            if tmp_dist < closest_dist:
                closest_dist, closest_node = tmp_dist, tmp_node

            axis_dist = np.abs(node.point[axis] - point[axis])  # 第axis维上目标点与分割超平面的距离
            logger.debug("axis: {0}, distance: {1}, point: {2}".format(axis, axis_dist, node))
            if closest_dist < axis_dist:                        # 不相交则可以直接返回，不用继续判断
                logger.debug("exit visit exclusive node {0}".format(node))
            else:
                current_dist = self.metric(node.point, point)
                if current_dist < closest_dist:
                    closest_dist, closest_node = current_dist, node

                logger.debug("metric {0}".format(node))
                candidates.append((current_dist, node))

                tmp_dist, tmp_node, touched = travel(further_node, closest_dist)    # 查找远点子树的最近节点
                nodes_visited += touched

                if tmp_dist < closest_dist:
                    closest_dist, closest_node = tmp_dist, tmp_node
                logger.debug("exit visit inclusive node {0}".format(node))

            return closest_dist, closest_node, nodes_visited

        dist, target, count = travel(self.root, np.inf)
        logger.info("expected {0}, touched {1}, candidates: {2}".format(1, count, len(candidates)))
        return dist, target, count, candidates

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
            if len(items) <= 0:
                return None
            axis, m = depth % n, len(items)
            sorted_data_list = sorted(items, key=lambda data: data[axis])
            mid = m // 2
            point = sorted_data_list[mid]
            node = KDNode(axis, point[:-1], point[-1], build(sorted_data_list[:mid], depth + 1),
                          build(sorted_data_list[mid + 1:], depth + 1))
            if node.left_child:
                node.left_child.parent = node
            if node.right_child:
                node.right_child.parent = node
            return node

        self.root = build(_data_list, depth=0)
