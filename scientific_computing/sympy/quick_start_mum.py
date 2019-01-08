# -*- coding: utf-8 -*-
from __future__ import division
import sympy as sp

assert 1 / 2 == 1.0 / 2
assert 1.0 / 2 == sp.Rational(1, 2)

assert sp.oo > sp.Rational(2) ** 50

print 'constants: \nπ = {0},\ne = {1},\n∞ = {2},\nEulerGamma = {3},\nGoldenRatio = {4},\ni = {5},\nnan = {6}'.format(
    sp.pi.evalf(), sp.E.evalf(), sp.oo.evalf(), sp.EulerGamma.evalf(), sp.GoldenRatio.evalf(), sp.I.evalf(), sp.nan.evalf())

