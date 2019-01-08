# -*- coding: utf-8 -*-

print(divmod(111, 11))
print(pow(2, 10))
# 2^8 % 10
print(pow(2, 8, 10))

a = 1, 2
b = 3, 4
c = a + b
print(a)
print(b)
print(c)

d = (1, 2, 3, 4)
print(d)
print('c==d is ', c == d)
print('c is d is ', c is d)
print('d is c is ', d is c)
print('id(c) = ', id(c))
print('id(d) = ', id(d))

x = 1
y = 2
print('x = ', x)
print('y = ', y)
(y, x) = (x, y)
print('x = ', x)
print('y = ', y)

s = [4, 1, 8, 0, 3, 9, 7, 2]
print(s)
ts = [(s[i], i) for i in range(len(s))]
print(ts)
print(min(ts))
print(max(ts))
