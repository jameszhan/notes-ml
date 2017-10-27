# -*- coding: utf-8 -*-

with open(__file__, 'r') as f:
    for line in f.readlines():
        print line.strip()


with open(__file__, 'r') as f:
    for line in f:
        print line.strip()