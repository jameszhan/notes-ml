# -*- coding: utf-8 -*-
import sympy as sp

assert 1 / 2 == 1.0 / 2
assert 1.0 / 2 == sp.Rational(1, 2)

assert sp.oo > sp.Rational(2) ** 50

print('constants: \n\
    π = {0},\n\
    e = {1},\n\
    ∞ = {2},\n\
    EulerGamma = {3},\n\
    GoldenRatio = {4},\n\
    i = {5},\n\
    nan = {6}'.format(
        sp.pi.evalf(), 
        sp.E.evalf(), 
        sp.oo.evalf(), 
        sp.EulerGamma.evalf(), 
        sp.GoldenRatio.evalf(), 
        sp.I.evalf(), 
        sp.nan.evalf()))

