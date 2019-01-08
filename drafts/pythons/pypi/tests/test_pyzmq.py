# -*- coding: utf-8 -*-

import unittest
import zmq
import time
import threading


def send_message():
    context = zmq.Context()

    print("Connecting to zmq-req-resp server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:9876")

    for request in range(0, 10):
        print("Sending request: {0} ".format(request))
        socket.send_string("request {0}".format(request))

        message = socket.recv()
        print("Received response {0} [{1}]".format(request, message))

    socket.send_string("exit")


def recv_message():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:9876")

    while True:
        message = socket.recv_string()
        print("Received request: {0}".format(message))

        time.sleep(1)

        socket.send_string("response")

        if message == 'exit':
            break


###
# conda install -n python3 pyzmq
###
class TestPyZeroMQ(unittest.TestCase):

    def test_client(self):
        t1 = threading.Thread(target=send_message, args=())
        t1.start()

    def test_server(self):
        t2 = threading.Thread(target=recv_message, args=())
        t2.start()


if __name__ == '__main__':
    unittest.main()
