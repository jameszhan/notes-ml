# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.distance import pdist

v1 = np.array([1.0, 2.0, 3.0])
v2 = np.array([9.0, 8.0, 7.0])


def euclidean(vec1, vec2):
    s = 0
    for i in range(len(vec1)):
        s += (vec1[i] - vec2[i]) ** 2
    return np.sqrt(s)


def euclidean2(vec1, vec2):
    return np.sqrt(np.sum(np.square(vec1 - vec2)))


def euclidean3(vec1, vec2):
    diff = vec1 - vec2
    return np.sqrt(np.dot(diff, diff.T))


def euclidean4(vec1, vec2):
    return np.linalg.norm(vec1 - vec2, ord=2)


print("euclidean = {0}".format(euclidean(v1, v2)))
print("euclidean2 = {0}".format(euclidean2(v1, v2)))
print("euclidean3 = {0}".format(euclidean3(v1, v2)))
print("euclidean4 = {0}".format(euclidean4(v1, v2)))


# 曼哈顿距离 (Manhattan Distance)：
# 又称城市街区距离，顾名思义，就像穿行在曼哈顿的街区一样，只能走直线然后拐弯在接着走直线，而不是两点之间直线最短
# \sum_{k=1}^n |x_{1k} - x_{2k}|
def manhattan(vec1, vec2):
    return np.sum(np.abs(vec1 - vec2))


def manhattan2(vec1, vec2):
    return np.linalg.norm(vec1 - vec2, ord=1)


print("manhattan = {0}".format(manhattan(v1, v2)))
print("manhattan2 = {0}".format(manhattan2(v1, v2)))


# 切比雪夫距离 (Chebyshev Distance)：
# 一张国际象棋的棋盘可以说明这个距离。大家都知道国际象棋中的后非常自由，可以用任意方法走任意多格，
# 切比雪夫距离就相当于问后从棋盘上一个位置到另一个位置最少需要走多少步（假设一步只能走一格，但这
# 一格可以是朝任何方向，直线斜线均可，用图像处理的概念说就是8邻域内的任何一个位置都可以一步走到）。
# 举个例子，从（1,1）位置走到（4,5）位置，后可以先斜向走到（2,2），然后（3,3），再然后（4,4），
# 最后直走一步到（4,5），也就是一共需要走4步，因此这两点的切比雪夫距离就是4。
# max |x_{1i} - x_{2i}|
def chebyshev(vec1, vec2):
    distance = 0
    for i in range(len(vec1)):
        m = abs(vec1[i] - vec2[i])
        if m > distance:
            distance = m
    return distance


def chebyshev2(vec1, vec2):
    return np.linalg.norm(vec1 - vec2, ord=np.inf)


print("chebyshev = {0}".format(chebyshev(v1, v2)))
print("chebyshev2 = {0}".format(chebyshev2(v1, v2)))


# 以上三种距离本质都是闵可夫斯基（Minkowski）距离的特定形式，切比雪夫距离中n取了无穷大，曼哈顿距离中n=1，而欧氏距离中n=2.
# D = \left( \sum_{i=1}^n \left|x_i - y_i\right|^p \right)^{1/p}
# \lim_{p \to \inf} D = max |x_{1i} - x_{2i}|
def minkowski(vec1, vec2, c=2.0):
    return np.sum(np.abs(vec1 - vec2) ** c) ** (1.0 / c)


print("minkowski(1) = {0}".format(minkowski(v1, v2, 1)))
print("minkowski(2) = {0}".format(minkowski(v1, v2, 2)))
print("minkowski(3) = {0}".format(minkowski(v1, v2, 3)))
print("minkowski(100) = {0}".format(minkowski(v1, v2, 100.0)))


# cos(\theta) = \frac{\sum_{k=1}^n x_{1k}x_{2k}}{\sqrt{\sum_{k=1}^n x_{1k}^2} \sqrt{\sum_{k=1}^n x_{2k}^2}}
# cos(\theta) = \frac{AB}{|A||B|}
def cosine(vec1, vec2):
    a = np.dot(vec1, vec2)
    b1 = np.sqrt(np.dot(vec1, vec1.T))
    b2 = np.sqrt(np.dot(vec2, vec2.T))
    return a / (b1 * b2)


def cosine2(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


# print(np.hstack([v1, v2]))
# print(np.vstack([v1, v2]))
# print(np.c_[v1, v2])
# print(np.r_[v1, v2])


def cosine3(vec1, vec2):
    x = np.vstack([vec1, vec2])
    # x = np.array([vec1, vec2])
    return (1 - pdist(x, 'cosine'))[0]


print("cosine = {0}".format(cosine(v1, v2)))
print("cosine2 = {0}".format(cosine2(v1, v2)))
print("cosine3 = {0}".format(cosine3(v1, v2)))


# 杰卡德相似系数
# J(A, B) = \frac{|A \bigcap B|}{|A \bigcup B|}
# J_{\delta}(A,B) = 1 − J(A,B)= \frac{|A \bigcup B|−|A \bigcap B|}{|A \bigcup B|}

def jaccard(vec1, vec2):
    up = np.bitwise_and((vec1 != vec2), np.bitwise_or(vec1 != 0, vec2 != 0)).sum()
    down = np.bitwise_or(vec1 != 0, vec2 != 0).sum()
    return up / down


def jaccard2(vec1, vec2):
    x = np.vstack([vec1, vec2])
    return pdist(x, 'jaccard')[0]


print("jaccard = {0}".format(jaccard(v1, v2)))
print("jaccard2 = {0}".format(jaccard2(v1, v2)))

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [5, 6, 2, 3, 13, 4, 1, 2, 4, 8]
# z = [2, 3, 3, 3, 5, 7, 9, 11, 9, 10]
#
# ax.scatter(*v1, c='r', marker='o')
# ax.scatter(*v2, c='b', marker='o')
#
#
# ax.set_xlabel('X Axis')
# ax.set_ylabel('Y Axis')
# ax.set_zlabel('Z Axis')
#
# plt.show()