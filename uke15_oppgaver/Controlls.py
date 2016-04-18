
'''
this will hold the controlls for the client
'''
import client as s
import threading
from New_Art import Art
from Tkinter import *
from state import State


def queue_river_GUI(state) :
    'start the whole art system'
    root = Tk()
    Art(root, state)
    root.mainloop()

def send_update(command):
    'this is used to send update to the server, example man in boat.. '
    s.client(command)

def get_state(state):
    '''
    this will update the state with servers version of state.
    '''
    state.tape.set_man(s.client('get man'))
    state.tape.set_boat(s.client('get boat'))
    state.tape.set_chicken(s.client('get chicken'))
    state.tape.set_fox(s.client('get fox'))
    state.tape.set_corn(s.client('get corn'))

    print state.tape.man
    print state.tape.boat
    print state.tape.chicken
    print state.tape.fox
    print state.tape.corn

    return state

def move_item(item, pos):
    request = 'move '+item+' '+pos
    print request
    print s.client(request)


state = get_state(State())
#move_item('chicken', 'boat')
#state = get_state(state)

art = threading.Thread(target=queue_river_GUI, args=(state,))

print state.tape.chicken
art.start()