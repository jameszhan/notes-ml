# -*- coding: utf-8 -*-

import collections

a = [3, 6, 3, 6, 3, 2, 2, 5, 5, 5, 5, 5, 1, 1, 3, 2, 3, 5, 2]

counter = collections.Counter(a)
assert len(counter.items()) == 5
assert counter.most_common(1) == [(5, 6)]
assert counter.most_common(2) == [(5, 6), (3, 5)]

