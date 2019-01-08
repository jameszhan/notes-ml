# -*- coding: utf-8 -*-
import os
import sys
import csv
import logging
import unittest
import time
import numpy as np

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_path)

from k_neighbors_classifier import KNeighborsClassifier

logger = logging.getLogger("unittestLogger")


def load_data(file):
    with open(file,'r') as csvfile:
        lines = csv.reader(csvfile)
        train_label, train_data = [], []
        test_label, test_data = [], []
        for i, line in enumerate(lines):
            if i == 0:
                # print("title: {0}".format(line))
                pass
            elif i < 40000:
                train_data.append(line[1:-1])
                train_label.append(line[0])
            else:
                test_data.append(line[1:-1])
                test_label.append(line[0])
        return np.array(train_data, np.int), np.array(train_label, np.int), np.array(test_data, np.int), np.array(test_label, np.int)


class TestDigitRecognizer(unittest.TestCase):
    def setUp(self):
        start_time = time.time()
        self.train_data, self.train_labels, self.test_data, self.test_labels = load_data("../../data/train.csv")
        load_time = time.time()
        logger.info("Load Data cost {0}s".format(load_time - start_time))

    def test_brute(self):
        logger.info("Use brute algorithm")
        start_time = time.time()
        knn = KNeighborsClassifier(n_neighbors=10, algorithm='brute')
        knn.fit(self.train_data, self.train_labels)
        fit_time = time.time()
        logger.info("Fit cost {0}s".format(fit_time - start_time))

        prediction = knn.predict(self.test_data)
        predict_time = time.time()
        logger.info("Predict cost {0}s".format(predict_time - fit_time))
        logger.info("test_data count is {0} and prediction is {1} and test_label is {2}".format(len(self.test_data),
                                                                                                len(prediction),
                                                                                                len(self.test_labels)))
        tp = 0
        for i, label in enumerate(prediction):
            if label != self.test_labels[i]:
                logger.info("prediction is {0}, actual is {1}".format(label, self.test_labels[i]))
            else:
                tp += 1

        logger.info("tp count is {0}".format(tp * 1.0 / len(prediction)))

    def test_kd_tree(self):
        logger.info("Use kd tree algorithm")
        start_time = time.time()
        knn = KNeighborsClassifier(n_neighbors=10, algorithm='kd_tree')
        knn.fit(self.train_data, self.train_labels)
        fit_time = time.time()
        logger.info("Fit cost {0}s".format(fit_time - start_time))

        prediction = knn.predict(self.test_data)
        predict_time = time.time()
        logger.info("Predict cost {0}s".format(predict_time - fit_time))
        logger.info("test_data count is {0} and prediction is {1} and test_label is {2}".format(len(self.test_data),
                                                                                                len(prediction),
                                                                                                len(self.test_labels)))
        tp = 0
        for i, label in enumerate(prediction):
            if label != self.test_labels[i]:
                logger.info("prediction is {0}, actual is {1}".format(label, self.test_labels[i]))
            else:
                tp += 1

        logger.info("tp is {0}".format(tp * 1.0 / len(prediction)))


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    unittest.main()
