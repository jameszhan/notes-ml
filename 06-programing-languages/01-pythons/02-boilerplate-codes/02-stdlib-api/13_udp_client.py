# -*- coding: utf-8 -*-
import socket

server_ddr = ('127.0.0.1', 9999)
cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        data = input("Send message: ")
        if data:
            cs.sendto(bytes(data + "\n", "utf8"), server_ddr)
        else:
            break
finally:
    cs.close()
