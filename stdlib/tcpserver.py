# -*- coding: utf-8 -*-

import socket

host = '127.0.0.1'
port = 8086

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

while True:
    cs, ca = s.accept()
    print('Client connected %s %s' %(cs, ca))
    cs.sendall('Hello World!'.encode('utf-8'))
    cs.close()
