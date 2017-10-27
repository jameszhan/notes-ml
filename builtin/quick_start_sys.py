# -*- coding: utf-8 -*-
import sys

print 'dir(sys) = {0}'.format(dir(sys))

method_type = type(sys.exit)


for m in dir(sys):
    if hasattr(sys, m):
        attr = getattr(sys, m)
        if type(attr) != method_type:
            print 'sys[{0}] = {1}\n'.format(m, attr)
        else:
            if m.startswith('get') or m.startswith('is'):
                try:
                    print 'sys.{0}() = {1}\n'.format(m, apply(attr))
                except TypeError, e:
                    print 'ignore sys.{0}()\n'.format(m)
            else:
                print 'ignore sys.{0}()\n'.format(m)

