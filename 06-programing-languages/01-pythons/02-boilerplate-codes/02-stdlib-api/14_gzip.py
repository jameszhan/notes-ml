# -*- coding: utf-8 -*-
import gzip
import shutil
import os.path

s = b"Hello World!"
t = gzip.compress(s)
print("{} => {}".format(len(s), len(t)))
assert(s == gzip.decompress(t))

ss = s * 100
tt = gzip.compress(ss)
print("{} => {}".format(len(ss), len(tt)))
assert(ss == gzip.decompress(tt))

tmp_file = "/tmp/{}.tar.gz".format(os.path.basename(__file__))

with open(__file__, 'rb') as fin:
    with gzip.open(tmp_file, 'wb') as gout:
        shutil.copyfileobj(fin, gout)

with gzip.open(tmp_file, 'rb') as f:
    print(f.read().decode('UTF-8'))