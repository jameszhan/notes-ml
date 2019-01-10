# -*- coding: utf-8 -*-
import sympy as sp

method_type = type(sp.symbols)

types, modules, functions = [], [], []

for m in dir(sp):
    if hasattr(sp, m):
        attr = getattr(sp, m)
        attr_type = type(attr)
        if method_type != attr_type:
            type_str = str(attr_type)
            if type_str.startswith("<type 'str'"):
                print('sympy[{0}] = {1}.\n'.format(m, attr))
            elif type_str.startswith("<class 'sympy.core.numbers"):
                print('sympy[{0}] = {1}, val: {2}.\n'.format(m, attr, attr.evalf()))
            elif type_str.startswith("<type 'type'>"):
                types.append(m)
            elif type_str.startswith("<type 'module'>"):
                modules.append(m)
            elif type_str.startswith("<class 'sympy.core.function"):
                functions.append(m)
            else:
                print('sympy[{0}], type: {1}\n'.format(m, type(attr)))


print('types: {0}'.format(types))
print('modules: {0}'.format(modules))
print('functions: {0}'.format(functions))

