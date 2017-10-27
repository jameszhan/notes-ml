# -*- coding:utf-8 -*-

import numpy as np
from computeCost_reg import computeCost_reg
from sigmoid import sigmoid

def gradientDescent_reg(X,y,num_labels,lambd):
    m,n = X.shape
    X = np.concatenate((np.ones((m, 1)), X), axis=1)
    # 如果需要提高准确度可以增加迭代次数，但是同样的会增加时间耗时
    iterations = 500
    alpha = 0.03
    # all_theta10x401，为10个类别的最终权值
    all_theta = np.zeros((num_labels, n+1))
    J_history = np.zeros((iterations,1))
    for i in range(num_labels):
        theta = np.zeros((n+1,1))
        for j in range(iterations):
            h = sigmoid(np.dot(X,theta))
            theta = theta - alpha/m*np.dot(X.T,(h-boolToDigit(y==i)))
            J_history[j,:] = computeCost_reg(theta,X,boolToDigit(y==i),lambd)
        print 'training digit %d position...\n'%i
        all_theta[i,:] = theta.T
    return all_theta,J_history

def boolToDigit(array):
    m,n = array.shape
    digit = np.zeros((m,n))
    for i in range(m):
        if array[i,:] == True:
            digit[i,:] = 1
        else:
            digit[i,:] = 0
    return digit

