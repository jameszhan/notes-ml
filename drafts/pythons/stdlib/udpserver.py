# -*- coding: utf-8 -*-

import socket

host = '127.0.0.1'
port = 8086

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((host, port))

while True:
    data, addr = udp.recv(256)
    print('%s Client connected, said: %s' %(data, addr))
