import tape as t
import art


class State:
    def __init__(self):
        self.tape = t.Database()                     # create new tape for the boat project
        self.art = art.Art()                         # create an art object, to show us some graphics

    def check_state(self):                           # if everything is left, as it would in the start of the game.

        if self.check_lose_combo():                  # if the player left chicken and corn alone or fox and chicken
            print("player is dead")                  # print art to the player NB: not created art for it yet.
            return None                              # break the state check

        self.man_in_boat()                           # if man is inside the boat options is delivered
        self.man_on_left()                           # if the man is at left, give options
        self.man_on_right()                          # if the man is at right, give options.

    def check_lose_combo(self):
        '''
        This will check if the current state will lead to the player to lose
        :return: True if the player is 'dead' | False if the user is not 'dead'
        '''

        # where either chicken and corn is left alone, or fox and chicken is left alone.
        if (self.tape.chicken in self.tape.fox) and (self.tape.man not in self.tape.chicken) or \
                (self.tape.chicken in self.tape.corn) and (self.tape.man not in self.tape.chicken):

            return True                                 # return True if the player has lost the game
        return False                                    # return False if the player has not lost the game.

    def man_in_boat(self):
        if self.tape.man in 'boat':
            if 'boat' in 'left':        # man can go out of boat to left side (a) or can travel to right side (b)
                pass
            if 'boat' in 'right':       # man can go out of boat to the right side (b) or can travel to the left side.
                pass

    def man_on_left(self):
        if self.tape.man in 'left':

            # check if the statement is at the beginning of the game.
            if 'left' in (self.tape.man, self.tape.chicken, self.tape.fox, self.tape.corn, self.tape.boat):
                print(self.art.art_a['a_with_items_person'])  # print the art for the position.

            # start to sort of items on the selected position
            pass

    def man_on_right(self):
        if self.tape.man in 'right' :
            pass


def test():
    state = State()
    state.check_state()

test()