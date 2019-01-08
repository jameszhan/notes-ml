# -*- coding: utf-8 -*-

import gzip

with gzip.open('time-1.7.tar.gz', 'rb') as f:
    print(f.read())
