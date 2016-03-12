import tape as t
import art


class State:
    def __init__(self):
        self.tape = t.Database()                          # create new tape for the boat project
        self.art = art.Art()                              # create an art object, to show us some graphics

    def check_state(self):                                # if everything is left, as it would in the start of the game.

        if self.check_lose_comboes():                     # check if the player has hit any death traps.
            print("player is dead")                       # print art to the player NB: not created art for yet.
            return None                                   # break the check

        if 'left' in (self.tape.man, self.tape.chicken, self.tape.fox, self.tape.corn, self.tape.boat):
            print(self.art.art_a['a_with_items_person'])  # print the art for the position.

    def check_lose_comboes(self):
        '''
        This will check if the current state will lead to the player to lose
        :return: True if the player is 'dead' | False if the user is not 'dead'
        '''

        # for ever condition where the man has left A wrong.
        # where either chicken and corn is left alone, or fox and chicken is left alone.
        if 'left' in (self.tape.boat, self.tape.chicken, self.tape.corn) and \
            'boat' in (self.tape.man, self.tape.fox) or \
                'left' in (self.tape.boat, self.tape.chicken, self.tape.fox) and \
                'boat' in (self.tape.man, self.tape.corn):
            return True
        pass


def test():
    state = State()
    state.check_state()

test()