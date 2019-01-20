# -*- coding: utf-8 -*-
import socket

addr = ('0.0.0.0', 9999)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(addr)
    sock.listen(1)
    conn, addr = sock.accept()
    with conn:
        print('connected by', addr)
        while True:
            data = conn.recv(8192)
            if not data:
                break
            conn.sendall(data)