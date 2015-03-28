__author__ = 'susperius'

__author__ = 'susperius'

import gevent
import gevent.monkey
import gevent.socket
from gevent import socket

#gevent.monkey.patch_all()


class TcpClient():
    def __init__(self, node_listener, node_port):
        self._node_listener = node_listener
        self._node_port = node_port

    def send_to_node(self, data):
        answer = ""
        sock = gevent.socket.create_connection((self._node_listener, self._node_port))
        sock.send(data)
        fp = sock.makefile()
        while True:
            line = fp.readline()
            if line:
                answer += line
                fp.flush()
            else:
                break
        sock.close()
        return answer