# -*- coding: utf-8 -*-

# 写点中文注释！！！
with open(__file__, "r") as f:
    for line in f:
        print 'line: {0}.'.format(line)

        print line.encode("utf-8").decode("utf-8")
        print line.encode("gbk")

