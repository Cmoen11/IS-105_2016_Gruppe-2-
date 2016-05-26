'''
server lobby
'''

from uke15_oppgaver.core import state

class lobby :

    def __init__(self):
        self.MAX_MEMBERS = 3        # how many members that is allowed to enter the game.
        self.members = []          # the members that is inside of the lobby.
        self.state = state()        # state object, to store our state.

    def addClient(self, client):
        self.members.append(client)