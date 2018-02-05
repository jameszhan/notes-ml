# -*- coding: utf-8 -*-

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 0, 1

x = np.arange(-5, 5, 0.1)
y = stats.norm.pdf(x, mu, sigma)

plt.title('Normal: $\mu$={0}, $\sigma^2$={1}'.format(mu, sigma))
plt.plot(x, y, 'k--')
plt.xlabel('x')
plt.ylabel('probability density')

plt.text(-1, 0.025, "$f(x) = \\frac{1}{\sigma\sqrt{2\pi}}e^{-\\frac{(x-\mu)^2}{2\sigma^2}}$")


X = mu + sigma * np.random.randn(10000)
# the histogram of the data
n, bins, patches = plt.hist(X, 50, normed=1, facecolor='y', alpha=0.75)

print('n = {0}, \nbins = {1}, \npatches = {2}'.format(n, bins, patches))

plt.grid(True)
plt.show()
