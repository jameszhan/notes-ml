# -*- coding: utf-8 -*-
import numpy as np
from collections import Counter


def dot_distance(vec1, vec2):
    return np.linalg.norm(np.subtract(vec1, vec2), ord=2)


class KNeighborsClass(object):
    def __init__(self, n_neighbors=10):
        self.n_neighbors = n_neighbors
        self.training_set = []
        self.labels = []

    def fit(self, training_set, labels):
        self.training_set = training_set
        self.labels = labels

    def predict(self, test_row):
        distances = []
        for v in self.training_set:
            distances.append(dot_distance(v, test_row))
        sorted_indexes = np.argsort(distances)
        class_list = [self.labels[sorted_indexes[i]] for i in range(self.n_neighbors)]
        counter = Counter(class_list)
        return counter.most_common(1)[0][0]


if __name__ == '__main__':
    sigma1, sigma2, count = 6, 0.5, 500
    x1 = np.random.normal(50, sigma1, count)
    y1 = np.random.normal(5, sigma2, count)

    x2 = np.random.normal(30, sigma1, count)
    y2 = np.random.normal(4, sigma2, count)

    x3 = np.random.normal(45, sigma1, count)
    y3 = np.random.normal(2.5, sigma2, count)

    labels = [1] * count + [2] * count + [3] * count

    knn = KNeighborsClass()
    training_set = np.c_[np.r_[x1, x2, x3], np.r_[y1, y2, y3]]

    knn.fit(training_set, labels)

    def do_test(test_set, label):
        tp = 0.0
        for row in test_set:
            result = knn.predict(row)
            # print("{0} => {1}".format(row, result))
            if result == label:
                tp += 1
        return tp / len(test_set)

    _x1 = np.random.normal(50, sigma1, 100)
    _y1 = np.random.normal(5, sigma2, 100)
    test_set = np.c_[_x1, _y1]
    print("test {0} and tp is {1}".format(1, do_test(test_set, 1)))

    _x2 = np.random.normal(30, sigma1, 100)
    _y2 = np.random.normal(4, sigma2, 100)
    test_set = np.c_[_x2, _y2]
    print("test {0} and tp is {1}".format(3, do_test(test_set, 2)))

    _x3 = np.random.normal(45, sigma1, 100)
    _y3 = np.random.normal(2.5, sigma2, 100)
    test_set = np.c_[_x3, _y3]
    print("test {0} and tp is {1}".format(3, do_test(test_set, 3)))


