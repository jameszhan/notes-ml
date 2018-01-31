# -*- coding: utf-8 -*-
import os
import sys
import logging
import unittest
import numpy as np

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_path)

from kd_tree import KDTree

logger = logging.getLogger("unittestLogger")


class TestKDTree1d(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        points = np.random.randint(0, 50, 10)
        self.tree = KDTree(np.transpose([points]))

    def test_traversal(self):
        logger.info("PreOrder:")
        self.tree.traversal(lambda n: logger.info(n), "preorder")
        logger.info("InOrder:")
        self.tree.traversal(lambda n: logger.info(n), "inorder")
        logger.info("PostOrder:")
        self.tree.traversal(lambda n: logger.info(n), "postorder")

    def test_closest(self):
        dist, node, count, candidates = self.tree.closest([15])
        logger.info("dist = {0}, node = {1}, visit_count = {2}".format(dist, node, count))
        logger.info("visited nodes = {0}".format(candidates))


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

    unittest.main()
