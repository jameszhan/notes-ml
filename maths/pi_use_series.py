# -*- coding: utf-8 -*-

import numpy as np

n = 100000
pi = np.sum(4.0 / np.r_[1:n:4, -3:-n:-4])

print pi

