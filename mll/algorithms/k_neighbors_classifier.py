# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
from collections import Counter

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_path)

from structure.kd_tree import KDTree

VALID_ALGORITHMS = ['kd_tree', 'brute']


def default_get_distince(x1, x2):
    return np.linalg.norm(np.subtract(x1, x2), ord=2)


class BruteSearch(object):
    def __init__(self, data_list, labels=None, metric=default_get_distince):
        self.metric = metric
        self.data_list = data_list
        self.labels = labels

    def predict(self, point, k=1):
        distances = []
        for v in self.data_list:
            distances.append(self.metric(v, point))
        sorted_indexes = np.argsort(distances)
        class_list = [self.labels[sorted_indexes[i]] for i in range(k)]
        counter = Counter(class_list)
        return counter.most_common(1)[0][0]


class KNeighborsClassifier(object):

    def __init__(self, algorithm='kd_tree', n_neighbors=10):
        self.n_neighbors = n_neighbors
        self.algorithm = algorithm
        self.handler = None

    def fit(self, training_set, labels):
        if self.algorithm == 'kd_tree':
            self.handler = KDTree(training_set, labels)
        else:
            self.handler = BruteSearch(training_set, labels)

    def predict(self, points):
        return [self.handler.predict(point) for point in points]
