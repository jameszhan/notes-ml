# -*- coding: utf-8 -*-
import time
import csv
import numpy as np
from sklearn import neighbors


def load_data(file):
    with open(file,'r') as csvfile:
        lines = csv.reader(csvfile)
        train_label, train_data = [], []
        test_label, test_data = [], []
        for i, line in enumerate(lines):
            if i == 0:
                # print("title: {0}".format(line))
                pass
            elif i < 39000:
                train_data.append(line[1:-1])
                train_label.append(line[0])
            else:
                test_data.append(line[1:-1])
                test_label.append(line[0])
        return np.array(train_data, np.int), np.array(train_label, np.int), np.array(test_data, np.int), np.array(test_label, np.int)


def fit(train_data, train_label):
    knn = neighbors.KNeighborsClassifier(n_neighbors=10)
    knn.fit(train_data, train_label)
    return knn


if __name__ == '__main__':
    start_time = time.time()
    train_data, train_label, test_data, test_label = load_data("/Users/james/Downloads/train.csv")
    load_time = time.time()
    print("Load Data cost {0}s".format(load_time - start_time))

    knn = fit(train_data, train_label)
    fit_time = time.time()
    print("Fit cost {0}s".format(fit_time - load_time))

    prediction = knn.predict(test_data)
    predict_time = time.time()
    print("Predict cost {0}s".format(predict_time - fit_time))
    print("test_data count is {0} and prediction is {1} and test_label is {2}".format(len(test_data), len(prediction), len(test_label)))

    tp = 0
    for i, label in enumerate(prediction):
        if label != test_label[i]:
            print("prediction is {0}, actual is {1}".format(label, test_label[i]))
        else:
            tp += 1

    print("tp count is {0}".format(tp * 1.0 / len(prediction)))
