import tape as t
import art as art

class State :
    def __init__(self):
        self.tape = t.Database()                            # create new tape for the boat project
        self.art = art.Art()

    def check_state(self):
        # if everything is left, as it would in the start of the game.
        if 'left' in (self.tape.man, self.tape.chicken, self.tape.fox, self.tape.corn, self.tape.boat):
            print(art.Art.art_a['a_with_items_person'])     # print the art for the position.

    def check_lose_comboes(self):
        '''
        This will check if the current state will lead to the player to lose
        :return:
        '''
        pass
