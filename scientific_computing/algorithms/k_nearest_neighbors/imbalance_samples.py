# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 15
fig_size[1] = 10

x1 = np.random.normal(50, 6, 50)
y1 = np.random.normal(5, 0.5, 50)
# plt.scatter(x1, y1, c='b', marker='s', s=50, alpha=0.8)

x2 = np.random.normal(30, 6, 500)
y2 = np.random.normal(4, 0.5, 500)
# plt.scatter(x2, y2, c='r', marker='^', s=50, alpha=0.8)

x3 = np.random.normal(45, 6, 5000)
y3 = np.random.normal(2.5, 0.5, 5000)
# plt.scatter(x3, y3, c='g', s=50, alpha=0.8)

plt.axis((10, 70, 1, 7))

x_val = np.concatenate((x1, x2, x3))
y_val = np.concatenate((y1, y2, y3))

x_diff = max(x_val) - min(x_val)
y_diff = max(y_val) - min(y_val)

print(x_diff)
print(y_diff)

x_normalized = x_val / x_diff
y_normalized = y_val / y_diff
xy_normalized = list(zip(x_normalized, y_normalized))


clf = neighbors.KNeighborsClassifier(10)
labels = [1] * 50 + [2] * 500 + [3] * 5000

clf.fit(xy_normalized, labels)

nearests = clf.kneighbors([(50 / x_diff, 5 / y_diff), (30 / x_diff, 3 / y_diff)], 5, False)

print(nearests)

xx,yy = np.meshgrid(np.arange(1, 70.1, 0.1), np.arange(1, 7.01, 0.01))
xx_normalized = xx / x_diff
yy_normalized = yy / y_diff
coords = np.c_[xx_normalized.ravel(), yy_normalized.ravel()]

Z = clf.predict(coords)
Z = Z.reshape(xx.shape)

light_rgb = ListedColormap([ '#AAAAFF', '#FFAAAA', '#AAFFAA'])
plt.pcolormesh(xx, yy, Z, cmap=light_rgb)


plt.scatter(x1, y1, c='b', marker='s', s=30, alpha=0.7)
plt.scatter(x2, y2, c='r', marker='^', s=30, alpha=0.7)
plt.scatter(x3, y3, c='g', s=30, alpha=0.7)

plt.scatter([50, 30, 45], [5, 4, 2.5], c='m', marker='*', s=100, alpha=1.0)


plt.show()

