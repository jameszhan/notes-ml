# -*- coding: utf-8 -*-
import sympy as sp

x = sp.symbols('x')


assert sp.pi == sp.integrate(sp.sqrt(1 - x**2), (x, -1, 1)) * 2
assert 1 == sp.integrate(sp.sin(x), (x, 0, sp.pi / 2))
assert 1 == sp.integrate(sp.cos(x), (x, 0, sp.pi / 2))
assert 1 == sp.integrate(sp.exp(x), (x, -sp.oo, 0))
assert sp.oo == sp.integrate(1.0 / x, (x, 0, 1))


