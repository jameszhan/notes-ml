# -*- coding: utf-8 -*-

import heapq

a = []

heapq.heappush(a, 3)
heapq.heappush(a, 2)
heapq.heappush(a, 4)
heapq.heappush(a, 7)
heapq.heappush(a, 5)
heapq.heappush(a, 1)
heapq.heappush(a, 8)
heapq.heappush(a, 6)

print("heap = {0}".format(a))
for i in range(10):
    print("top {0} = {1}".format(i, heapq.nsmallest(i, a)))

for i in range(len(a)):
    print("{0}: {1}".format(i, heapq.heappop(a)))


class Node(object):
    def __lt__(self, other):
        if other is None:
            return -1
        elif other == self:
            return 0
        else:
            return 1

    # def __eq__(self, other):
    #     return self == other


b = []
heapq.heappush(b, (3, Node()))
print("heap = {0}".format(b))
heapq.heappush(b, (1, Node()))
print("heap = {0}".format(b))
heapq.heappush(b, (2, Node()))
print("heap = {0}".format(b))
heapq.heappush(b, (3, Node()))
heapq.heappush(b, (1, Node()))

print("heap = {0}".format(b))

for i in range(len(b)):
    print("{0}: {1}".format(i, heapq.heappop(b)))
