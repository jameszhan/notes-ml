# -*- coding: utf-8 -*-

a = 3
b = 5

print 'abs({0} - {1}) == abs({1}, {0}) => {2}'.format(a, b, abs(a - b) == abs(b - a))

print 'bin({0}) => {1}, bin(1023) => {2}'.format(b, bin(b), bin(1023))
print 'oct({0}) => {1}, oct(1023) => {2}'.format(b, oct(b), oct(1023))
print 'hex({0}) => {1}, hex(1023) => {2}'.format(b, hex(b), hex(1023))

print 'complex(3) => {0}, complex("2+3j") == complex(2, 3) => {1}'.format(complex(3), complex("2+3j") == complex(2, 3))

x, y = complex(3), complex(0, 4)
print '{0} + {1} = {2}'.format(x, y, x + y)

print 'divmod(11, 3) => {0}'.format(divmod(11, 3))

print 'pow(2, 5) = {0} vs. 2 ** 5 = {1}'.format(pow(2, 5), 2 ** 5)
print 'pow(2, 5, 3) = {0}, pow(2, 5, 11) = {1}'.format(pow(2, 5, 3), pow(2, 5, 11))

print 'bool(3) = {0}, bool(0) = {1}, bool("a") = {2}'.format(bool(3), bool(0), bool('a'))

print 'int(10) = {0}, int("10", 16) = {1}'.format(int(10), int('10', 16))
print 'long(10) = {0}, long("10", 16) = {1}'.format(long(10), long('10', 16))
print 'float(10) = {0}, float("10") = {1}'.format(float(10), float('10'))