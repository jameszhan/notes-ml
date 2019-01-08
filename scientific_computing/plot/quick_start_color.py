# -*- coding: utf-8 -*-
import sys
import logging
import numpy as np
import matplotlib.pyplot as plt


logger = logging.getLogger("examples")
logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

fig = plt.figure()

x = np.random.normal(0, 1, 300)
y = np.random.normal(0, 1, 300)
size = np.random.randint(1, 50, 300)
color = np.random.randint(1, 200, 300)

dir_cm = dir(plt.cm)

logger.info("cm({0}) is {1}".format(len(dir_cm), dir_cm))
logger.info("cmaps = {0}".format(plt.cm.cmap_d.keys()))


# plt.set_cmap(plt.cm.hsv)
plt.set_cmap(plt.cm.brg)
plt.scatter(x, y, size, color)
plt.colorbar()
plt.show()
