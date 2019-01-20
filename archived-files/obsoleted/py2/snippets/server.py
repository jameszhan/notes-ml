import select
import socket
import os
import re

SERVER_NAME = 'localhost'
SERVER_PORT = 8888
HTTP_REGEX = 'GET\s+([^\s]+)\s+HTTP'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((SERVER_NAME, SERVER_PORT))
    s.listen(16)
    inputs = [s]
    while (True):
        rs, ws, es = select.select(inputs, [], [])
        for r in rs:
            if r is s:
                c, addr = s.accept()
                print('Got connection from', addr)
                inputs.append(c)
            else:
                try:
                    data = r.recv(1024)
                    msg = str(data)
                    print('msg=', msg)
                    pa = re.compile('.')
                    print('hello---', pa.match(msg).groups)
                    filename = pa.match(msg).groups[0]
                    if (filename == '/'):
                        filename = 'index.html'
                    pathname = os.getcwd() + filename

                    f = open(pathname, 'rb')
                    r.send(f.read())
                    f.close()

                    disconnected = not data
                except(socket.error):
                    disconnected = True
                if disconnected:
                    inputs.remove(r)
                else:
                    print(data)

except(socket.error):
    print('socket error:%s')
