# -*- coding: utf-8 -*-
import sympy as sp

x = sp.symbols('x')

print "sin'(x) = {0}".format(sp.diff(sp.sin(x), x))
print "sin'(x^2) = {0}".format(sp.diff(sp.sin(x ** 2), x))
print "log'(x) = {0}".format(sp.diff(sp.log(x), x))

sigmod = (1 / (1 + sp.E ** -x))

print "sigmod'(x) = {0}".format(sp.diff(sigmod, x))

theta0, theta1, theta2 = sp.symbols('theta0 theta1 theta2')
x1, x2, y = sp.symbols('x1 x2 y')

sse = (theta0 + theta1 * x1 + theta2 * x2 - y) ** 2 / 2

print 'partial(θ0) = {0}'.format(sp.diff(sse, theta0))
print 'partial(θ1) = {0}'.format(sp.diff(sse, theta1))
print 'partial(θ2) = {0}'.format(sp.diff(sse, theta2))

