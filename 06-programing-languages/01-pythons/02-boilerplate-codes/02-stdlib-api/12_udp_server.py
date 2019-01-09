# -*- coding: utf-8 -*-
# nc -u 127.0.0.1 9999

import socket

addr = ('0.0.0.0', 9999)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)
print('starting up on {} port {}'.format(*addr))

while True:
    print('\nWaiting to receive message')
    data, address = sock.recvfrom(256)
    print('received {} bytes from {}'.format(len(data), address))
    print(data)
