# -*- coding: utf-8 -*-

a = []
b = a
c = []
print id(a)
print id(b)
print id(c)

a.append(1)
print id(a)
print id(b)
print id(c)
