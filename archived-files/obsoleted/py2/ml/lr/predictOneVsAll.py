# -*-coding:utf-8 -*-

import numpy as np
from sigmoid import sigmoid

def predictOneVsAll(all_theta,X):
    # X:5000x400
    m = X.shape[0]

    # num_labels:10,all_theta:10x401
    num_labels = all_theta.shape[0]

    p = np.zeros((m,1))

    X = np.concatenate((np.ones((m,1)),X),axis=1)

    predict = sigmoid(np.dot(X,all_theta.T))

    position = np.zeros((m,1))

    for i in range(predict.shape[0]):
        # 获取每行的最大值的列索引
        position[i,:] = np.where(predict[i,:] == np.max(predict[i,:]))[0][0]

    return position