# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 1

X = mu + sigma * np.random.randn(10000)
# the histogram of the data

plt.subplot(511)
n, bins, patches = plt.hist(X, 50, normed=0, facecolor='yellowgreen', alpha=0.75)
print 'n = {0}, \nbins = {1}, \npatches = {2}'.format(n, bins, patches)

X2 = np.random.normal(mu, sigma, 10000)
plt.subplot(512)
n, bins, patches = plt.hist(X2, 50, normed=0, facecolor='pink', alpha=0.75)
print 'n = {0}, \nbins = {1}, \npatches = {2}'.format(n, bins, patches)

X3 = np.random.rand(10000)
plt.subplot(513)
n, bins, patches = plt.hist(X3, 50, normed=0, facecolor='b', alpha=0.75)
print 'n = {0}, \nbins = {1}, \npatches = {2}'.format(n, bins, patches)

X4 = np.random.uniform(mu, sigma, 10000)
plt.subplot(514)
n, bins, patches = plt.hist(X4, 50, normed=0, facecolor='b', alpha=0.75)
print 'n = {0}, \nbins = {1}, \npatches = {2}'.format(n, bins, patches)

X5 = np.random.random_sample(10000)  # np.random.randint(0, 10, size=10000)
plt.subplot(515)
n, bins, patches = plt.hist(X5, 50, normed=0, facecolor='b', alpha=0.75)
print 'n = {0}, \nbins = {1}, \npatches = {2}'.format(n, bins, patches)


plt.grid(True)
plt.show()