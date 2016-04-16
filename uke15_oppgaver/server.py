import socket
import sys


class Server :
    def __init__(self, state):
        self.state = state

    def start_server(self):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = ('localhost', 10000)
        print >>sys.stderr, 'starting up on %s port %s' % server_address
        sock.bind(server_address)

        # Listen for incoming connections
        sock.listen(1)

        while True:
            # Wait for a connection
            print >>sys.stderr, 'waiting for a connection'
            connection, client_address = sock.accept()

            try:
                print >>sys.stderr, 'connection from', client_address

                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(60)
                    print data
                    respons = str(self.decode(data))                              # decode the response

                    if data:
                        print >>sys.stderr, 'sending data back to the client'   # send it back to the client.
                        connection.sendall(respons)

                    else:
                        print >>sys.stderr, 'no more data from', client_address
                        break

            finally:
                # Clean up the connection
                connection.close()

    def decode(self, msg):
        if 'get' in msg:
            if 'man' in msg :
                return self.state.tape.man
            elif 'boat' in msg:
                return self.state.tape.boat
            elif 'corn' in msg:
                return self.state.tape.corn
            elif 'fox' in msg:
                return self.state.tape.fox
            elif 'chicken' in msg:
                return self.state.tape.chicken

        elif 'move' in msg:
            move = self.state.tape
            if 'man' in msg:
                if 'left' in msg:
                    move.set_man('left')
                    return 'ok, moved'
                elif 'boat' in msg:
                    move.set_man('boat')
                    return 'ok, moved'
                elif 'right' in msg:
                    move.set_man('right')
                    return 'ok, moved'

            elif 'corn' in msg:
                if 'left' in msg:
                    move.set_corn('left')
                    return 'ok, moved'
                elif 'right' in msg:
                    move.set_corn('right')
                    return 'ok, moved'
                elif 'boat' in msg:
                    move.set_corn('boat')
                    return 'ok, moved'

            elif 'chicken' in msg:
                if 'left' in msg:
                    move.set_chicken('left')
                    return 'ok, moved'
                elif 'right' in msg:
                    move.set_chicken('right')
                    return 'ok, moved'
                elif 'boat' in msg:
                    move.set_chicken('boat')
                    return 'ok, moved'

            elif 'fox' in msg :
                if 'left' in msg :
                    move.set_fox('left')
                    return 'ok, moved'
                elif 'right' in msg:
                    move.set_fox('right')
                    return 'ok, moved'
                elif 'boat' in msg:
                    move.set_fox('boat')
                    return 'ok, moved'

            elif 'boat' in msg :
                if 'left' in msg:
                    move.set_boat('left')
                    return 'ok, moved'
                elif 'right' in msg:
                    move.set_boat('right')
                    return 'ok, moved'
        else :
            return 'lol'
