
'''
this will hold the controlls for the client
'''
import threading
from Tkinter import *

from uke15_oppgaver.core.New_Art import Art

from uke15_oppgaver.ClientHandler import client as s
from uke15_oppgaver.core.state import State


def queue_river_GUI(state, id) :
    'start the whole art system'
    root = Tk()
    Art(root, state, id)
    root.mainloop()

def send_update(command):
    'this is used to send update to the server, example man in boat.. '
    s.client(command)


def get_state(id, state):
    '''
    this will update the state with servers version of state.
    '''
    state.tape.set_man(s.client('(%s) get man' % id))
    state.tape.set_boat(s.client('(%s) get boat' % id))
    state.tape.set_chicken(s.client('(%s) get chicken' % id))
    state.tape.set_fox(s.client('(%s) get fox' % id))
    state.tape.set_corn(s.client('(%s) get corn' % id))

    print state.tape.man
    print state.tape.boat
    print state.tape.chicken
    print state.tape.fox
    print state.tape.corn

    return state

def move_item(item, pos, id):
    request = id+' move '+item+' '+pos
    print request
    print s.client(request)

def create_lobby():
    pass

def join_lobby():
    pass

def get_id():
    request = 'XX ID REQUEST'
    return s.client(request)

def start() :
    print '||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
    print 'Please type "create lobby" in order to create a new lobby,' \
          '\nor "join lobby" to join a lobby.'
    print '||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
    raw_input("please enter your command: ")

    id = get_id()

    print id
    state = get_state(id, State())

    art = threading.Thread(target=queue_river_GUI, args=(state,id))

    #print state.tape.chicken
    art.start()

start()