# -*- coding: utf-8 -*-

with open(__file__, 'r', encoding='ISO8859-1') as f:
    print("Read {} with encoding {}.".format(__file__, f.encoding))
    for line in f.readlines():
        print(line, end='')