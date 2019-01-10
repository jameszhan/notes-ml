# -*- coding: utf-8 -*-
import sympy as sp


p = sp.symbols('p')

print("log'(p) = {0}".format(sp.diff(sp.log(p)).simplify()))
print("(p*log(p))' = {0}".format(sp.diff(p * sp.log(p)).simplify()))
print("((1-p)*log(1-p))' = {0}".format(sp.diff((1-p) * sp.log(1 - p)).simplify()))


H = -(p * sp.log(p) + (1 - p) * sp.log(1 - p))

print("H'(p) = {0}".format(sp.diff(H, p).simplify()))

