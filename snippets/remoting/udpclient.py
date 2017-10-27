import socket

host = '127.0.0.1'
port = 8086

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = input("Send message: ")
    if data:
        cs.sendto(bytes(data + "\n", "utf8"), ('127.0.0.1', 8000))
    else:
        break

cs.close()
