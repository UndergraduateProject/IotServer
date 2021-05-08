import socket
import sys


def action():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ("140.117.71.98", 8889)
    sock.connect(server_address)
    try:
        # Send data
        message = "water"
        b = message.encode("utf-8")
        sock.sendall(b)

        # Look for the response
        amount_received = 0
        amount_expected = len(b)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)

    finally:
        sock.close()
