# -*- coding: utf-8 -*-
import sympy as sp

x = sp.symbols('x')

assert 1 == sp.limit(sp.exp(x), x, 0)

assert 1 == sp.limit(sp.sin(x) / x, x, 0)

assert sp.oo == sp.limit(1.0 / x, x, 0)

assert sp.E.evalf() == sp.limit((1 + 1.0 / x) ** x, x, sp.oo)
