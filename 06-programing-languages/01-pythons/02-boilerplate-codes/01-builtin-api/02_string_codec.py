# -*- coding: utf-8 -*-

# 写点中文注释
with open(__file__, "rb") as bf:
    bytes = bf.read()
    print("Decode By UTF-8\n{}\n".format(bytes.decode("UTF-8")))
    print("Decode By ISO8859-1\n{}\n".format(bytes.decode("ISO8859-1")))
    try:
        print("Decode By GB18030\n{}\n".format(bytes.decode("GB18030")))
    except UnicodeDecodeError as e:
        print(e)