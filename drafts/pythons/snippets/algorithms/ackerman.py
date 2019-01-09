# -*- coding: utf-8 -*-


def ackerman(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackerman(m - 1, 1)
    else:
        return ackerman(m - 1, ackerman(m, n - 1))


print('ackerman(1, 1) = {0}'.format(ackerman(1, 1)))
print('ackerman(1, 2) = {0}'.format(ackerman(1, 2)))
print('ackerman(1, 3) = {0}'.format(ackerman(1, 3)))
print('ackerman(1, 4) = {0}'.format(ackerman(1, 4)))
print('ackerman(2, 1) = {0}'.format(ackerman(2, 1)))
print('ackerman(2, 2) = {0}'.format(ackerman(2, 2)))
print('ackerman(2, 3) = {0}'.format(ackerman(2, 3)))
print('ackerman(2, 4) = {0}'.format(ackerman(2, 4)))
print('ackerman(3, 1) = {0}'.format(ackerman(3, 1)))
print('ackerman(3, 2) = {0}'.format(ackerman(3, 2)))
print('ackerman(3, 3) = {0}'.format(ackerman(3, 3)))
print('ackerman(3, 4) = {0}'.format(ackerman(3, 4)))