# -*- coding: utf-8 -*-

a = []
b = a
c = []
print("id(a) = ", id(a))
print("id(b) = ", id(b))
print("id(c) = ", id(c))

a.append(1)
b.append(2)
c.append(3)

print("id(a) = ", id(a))
print("id(b) = ", id(b))
print("id(c) = ", id(c))
