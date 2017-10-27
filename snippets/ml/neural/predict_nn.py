# -*- coding:utf-8 -*-

import numpy as np
from sigmoid import sigmoid

def predict_nn(Theta1,Theta2,X):
    m,n = X.shape
    pred = np.zeros((m,1))

    a1 = np.concatenate((np.ones((m,1)),X),axis=1)
    z2 = np.dot(a1,Theta1.T)
    a2 = np.concatenate((np.ones((m,1)),sigmoid(z2)),axis=1)
    z3 = np.dot(a2,Theta2.T)
    a3 = sigmoid(z3)

    for i in range(a3.shape[0]):
        # 获取每行的最大值的列索引，因为该weights数据集是从mat文件导入的并不是训练出来的，
        # 而matlab下标是从1开始的python是从0开始的故要加1来确保一致性
        pred[i,:] = np.where(a3[i,:] == np.max(a3[i,:]))[0][0]+1
    return pred
