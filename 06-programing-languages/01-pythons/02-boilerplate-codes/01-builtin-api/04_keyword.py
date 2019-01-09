# -*- coding: utf-8 -*-
import keyword

print('dir(keyword) = {0}'.format(dir(keyword)))

method_type = type(keyword.iskeyword)

for m in dir(keyword):
    if hasattr(keyword, m):
        attr = getattr(keyword, m)
        if type(attr) != method_type:
            print('keyword[{0}] = {1}'.format(m, attr))
        else:
            if m.startswith('get') or m.startswith('is'):
                try:
                    # print('keyword.{0}() = {1}\n'.format(m, apply(attr)))     # python3 not support apply
                    print('keyword.{0}() = {1}'.format(m, attr()))
                except TypeError:
                    print('ignore keyword.{0}()'.format(m))
            else:
                print('ignore keyword.{0}()'.format(m))

