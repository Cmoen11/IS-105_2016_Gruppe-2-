import tape as t

class State :
    def __init__(self):
        self.tape = t.Database()                     # create new tape for the boat project

    def check_state(self):
        # if everything is left, as it would in the start of the game.
        if 'left' in (self.tape.man, self.tape.chicken, self.tape.fox, self.tape.corn, self.tape.boat):
            pass

    def check_lose_comboes(self):
        '''
        This will check if the current state will lead to the player to lose
        :return:
        '''
        pass
    