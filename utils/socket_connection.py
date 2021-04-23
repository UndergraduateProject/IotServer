import socket
import sys

class SocketMsg:
    def __init__(self, message):
        self.message = message
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('172.20.10.2', 8888)
    def send_to_iot(self):
        self.socket.connect(self.server_address)
        try:
            # Send data
            b = self.message.encode('utf-8')
            print('sending "%s"' % self.message)
            self.socket.sendall(b)

            # Look for the response
            amount_received = 0
            amount_expected = len(b)
            
            while amount_received < amount_expected:
                data = self.socket.recv(16)
                amount_received += len(data)
                print('received "%s"' % data)

        finally:
            print('closing socket')
            self.socket.close()