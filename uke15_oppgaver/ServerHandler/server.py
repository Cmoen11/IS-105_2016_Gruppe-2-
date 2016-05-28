# some code from https://pymotw.com/2/socket/tcp.html
import socket
import sys
from functools import partial
import state_protocol

class Server :
    def __init__(self, state):
        self.state = state
        self.tape = self.state.tape
        self.next_id = 1
        self.client_id = None
        self.current_id = 1                              # The one that are allowed to move.
        self.clients = [

        ]

        self.client_data = {
            'ID REQUEST':           self.new_id,
        }

        self.lobby = {


        }

        self.getters = {
            'get man':              self.tape.get_man,
            'get boat':             self.tape.get_boat,
            'get corn':             self.tape.get_corn,
            'get fox':              self.tape.get_fox,
            'get chicken':          self.tape.get_chicken
        }
        self.editState = {
            'move man left':        self.tape.set_man,
            'move man right':       self.tape.set_man,
            'move man boat':        self.tape.set_man,
            'move boat left':       self.tape.set_boat,
            'move boat right':      self.tape.set_boat,
            'move corn left':       self.tape.set_corn,
            'move corn boat':       self.tape.set_corn,
            'move corn right':      self.tape.set_corn,
            'move chicken left':    self.tape.set_chicken,
            'move chicken right':   self.tape.set_chicken,
            'move chicken boat':    self.tape.set_chicken,
            'move fox left':        self.tape.set_fox,
            'move fox right':       self.tape.set_fox,
            'move fox boat':        self.tape.set_fox,

        }

    def new_id(self):
        self.clients.append(
            self.next_id
        )
        self.next_id = self.next_id + 1

    def next_person(self):
        try:
            self.current_id = self.clients[self.next_id]
            self.next_id = self.next_id + 1
        except IndexError :
            self.next_id = 0
            self.current_id = self.clients[self.next_id]
            self.next_id = self.next_id + 1

    def isAllowed(self, id):
        if str(self.client_id) == str(self.current_id):
            return str(True);
        return str(False)

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
            #print >>sys.stderr, 'waiting for a connection'
            connection, client_address = sock.accept()

            try:
                #print >>sys.stderr, 'connection from', client_address

                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(1000)
                    if data :
                        array = data.split()                    # split data..
                        self.client_id = array[0]               # get ID out and store it under client ID
                        array.remove(self.client_id)            # remove ID from the data.
                        data = " ".join(array)


                    if len(data) > 1 and state_protocol.state_protocol(self.tape, data):       # if there is any data to look for
                        if state_protocol.state_protocol(self.tape, data):
                            if self.client_data.has_key(data):
                                self.client_data[data]()
                                respons = str(int(self.next_id - 1))

                            elif self.lobby.has_key(data):
                                pass

                            elif self.editState.has_key(data):
                                array = data.split()
                                self.editState[data](array[2])
                                self.next_person()
                                print 'next_person allowed: ' + str(self.current_id)

                            elif self.getters.has_key(data):
                                respons = str(self.getters[data]())                      # get position

                            elif data == 'is allowed':
                                respons = self.isAllowed(self.client_id)
                                #print str(self.client_id) + respons
                        else:
                            print data
                            respons = str(False)

                    if data:
                        #print >>sys.stderr, 'sending data back to the client'   # send it back to the client.
                        connection.sendall(respons)

                    else:
                        #print >>sys.stderr, 'no more data from', client_address
                        break

            finally:
                # Clean up the connection
                connection.close()