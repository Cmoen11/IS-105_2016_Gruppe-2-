'''
This module will give orders based on server and client.
'''

import threading

from uke15_oppgaver.ServerHandler.server import Server
from uke15_oppgaver.core.state import State


def queue_server(state) :
    s = Server(state)
    s.start_server()
    print 'server started'


state = State()

server = threading.Thread(target=queue_server, args=(state,))

server.start()
#art.start()
