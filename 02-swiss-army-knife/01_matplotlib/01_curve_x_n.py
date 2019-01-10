# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 100)

plt.plot(x, x)
plt.plot(x, x ** 0.9)
plt.plot(x, x ** 0.7)
plt.plot(x, x ** 0.5)


plt.grid(True)
plt.show()