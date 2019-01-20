# -*- coding: utf-8 -*-
# +------------+
# | BaseServer |
# +------------+
#       |
#       v
# +-----------+        +------------------+
# | TCPServer |------->| UnixStreamServer |
# +-----------+        +------------------+
#       |
#       v
# +-----------+        +--------------------+
# | UDPServer |------->| UnixDatagramServer |
# +-----------+        +--------------------+

import http.server
import socketserver

addr = ("0.0.0.0", 9999)
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(addr, handler)

print("serving at port", addr[1])
httpd.serve_forever()
