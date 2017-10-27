# -*- coding: utf-8 -*-

import numpy as np

X = [1, 2, 3, 4, 5]
print 'mean = {0}'.format(np.mean(X))                       # 平均值
print 'variance = {0}'.format(np.var(X))                    # 方差
print 'standard deviation = {0}'.format(np.std(X))          # 标准差
print 'covariance = {0}'.format(np.cov(X))                  # 协方差


a = np.array([1, 1, 2, 3, 5, 8, 13, 21])
print 'gradient({0}) = {1}'.format(a, np.gradient(a))
print 'gradient({0}, 2) = {1}'.format(a, np.gradient(a, 2))
print 'gradient({0}, 5) = {1}'.format(a, np.gradient(a, 5))


b = np.array([[1, 2, 6], [3, 4, 5]])
print 'gradient({0}) = {1}'.format(b, np.gradient(b))


