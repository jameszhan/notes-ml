# -*-coding:utf-8 -*-

import scipy.io
import numpy as np
from gradientDescent_reg import gradientDescent_reg
from computeCost_reg import computeCost_reg
from predictOneVsAll import predictOneVsAll

if __name__ == '__main__':

    # Part1:load data
    """
    data中为0-9的数字图片像素值，共有5000行x400列。
    每个图片都是20x20的小矩阵，将矩阵变成data中的一
    行向量。每个数字都有500个数据集。
    """
    print 'Loading data...\n'
    # data类型为dictionary
    data = scipy.io.loadmat('ex3data1.mat') # 假设文件名为1.mat
    # 即可知道Mat文件中存在数据名，假设存在'x', 'y'两列数据
    print '数据列有：',data.keys()
    # 所有像素点X
    X = data['X']
    # 数字的标签y
    y = data['y']

    print X, y

    # Part2:Gradient Descent
    y[0:500,:] = 0  # 将10标签替换成0标签
    m,n = X.shape
    num_labels = 10
    lambd = 0.1
    # computeCost_reg(theta,X,y,lambd)
    all_theta,J_history = gradientDescent_reg(X,y,num_labels,lambd)
    # print J_history


    # Part3:Predict
    pred = predictOneVsAll(all_theta,X)
    accuracy = np.mean(pred == y)
    print 'Train accuracy is :%f\n' % accuracy

