import http.server
import socketserver

PORT = 8086

handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), handler)

print("serving at port", PORT)
httpd.serve_forever()
