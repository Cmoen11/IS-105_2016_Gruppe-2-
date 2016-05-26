'''
    This class will tell what 'state' the program is at.
'''
class Database:
    # this class will hold the "tape".
    def __init__(self):
        '''
            set the def settings to left.
            Keep in mind, this is only the position of the current elements of the 'game'
            not actually the figures in the game.
        '''
        self.boat = self.man = self.chicken = self.fox = self.corn = "left"
        pass

    '''
        'Write' to the tape with changes..
        new_pos will be either left, boat or right.

        :return: False if the edit was invalid. | return True if the edit was valid
    '''
    def set_boat(self, new_pos):
        if new_pos in ('left','right'):
            self.boat = new_pos
            return True
        else:
            return False

    def set_man(self, new_pos):
        """

        :rtype: object
        """
        if new_pos in ('left', 'right', 'boat'):
            self.man = new_pos
            return True
        else:
            return False

    def set_chicken(self, new_pos):
        if new_pos in ('left', 'right', 'boat'):
            self.chicken = new_pos
            return self.chicken
        else:
            print 'oh no!'
            return False

    def set_fox(self, new_pos):
        if new_pos in ('left', 'right', 'boat'):
            self.fox = new_pos
            return True
        else:
            return False

    def set_corn(self, new_pos):
        if new_pos in ('left', 'right', 'boat'):
            self.corn = new_pos
            return True
        else:
            return False


    def get_man(self):
        return self.man

    def get_boat(self):
        return self.boat

    def get_corn(self):
        return self.corn

    def get_chicken(self):
        return self.chicken

    def get_fox(self):
        return self.fox




