# -*- coding: utf-8 -*-
import numpy as np

M = np.mat('0 1 2; 1 0 3; 4 -3 8')

print 'M = {0}, \nM.I = {1}'.format(M, M.I)             # 矩阵的逆
print 'M.I.inv() = {0}'.format(np.linalg.inv(M.I))      # 矩阵的逆

print 'M.I * A = {0}\n\n\n'.format(M.I * M)

# solve Ax = b
A = np.array([1, 2, 3, 3, 1, 2, 2, 3, 1]).reshape((3, 3))
b = np.array([10, 13, 13])
x = np.linalg.solve(A, b)                               # 求解线性方程组
print 'A = {0}\n x = {1}, A * x = {2}'.format(A, x, np.dot(A, x))


# least square estimate
X = np.array([1, 2, 3, 4, 5, 6, 7, 8])
Y = np.array([2, 3, 4, 5, 6, 7, 8, 9])
X_T = np.vstack([X, np.ones(len(X))]).T

print np.linalg.lstsq(X_T, Y)


print 'Eigenvalues(A): {0}, Eigenvectors(A): {1}'.format(np.linalg.eigvals(A), np.linalg.eig(A))

M2 = np.mat('3 -2; 1 0')
w, v = np.linalg.eig(M2)
print 'Eigenvalues({0}): {1}, Eigenvectors: {2}'.format(M2, w, v)
for i in range(len(w)):
    v_i = v[:, i]
    print '{0}: {1} vs. {2}'.format(v_i, np.dot(M2, v_i), w[i] * v_i)


# determinat
M3 = np.mat('1 0 0; 0 2 0; 0 0 3')
det = np.linalg.det(M3)
print 'det({0}) = {1}'.format(M3, det)

