import socket
import sys

def client(command) :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)

    s.connect(server_address)

    try:
        # Send data
        message = command
        s.sendall(command)

        # Look for the response
        amount_received = 0
        amount_expected = len(command )

        while amount_received < amount_expected:
            data = s.recv(60)
            amount_received += len(data)
            #print >>sys.stderr, 'received "%s"' % data
            return data

    finally:
        #print >>sys.stderr, 'closing socket'
        s.close()