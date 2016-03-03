class Boat:
    def __init__(self):
        self.person = False                         # Is the person on board?
        self.passenger = []                         # passengers on the boat, in this example it would be animals
        self.position = 1                           # the position of the boat

    '''
        Add the person into the boat.
        :return: True has entered the boat | False if he already is inside the boat.
    '''
    def add_person(self):
        if self.person is not True:                 # if person is not already inside the boat
            self.person = True                      # set the boolean to true to indicate if person is inside
            return True                             # return True
        else:
            return False                            # Return False if the person already is inside the boat.

    '''
        remove the person from the boat.
        :return: True has exited the boat | False if he are not inside the boat.
    '''
    def remove_person(self):
        if self.person is True:                             # if person is not already inside the boat
            self.person = False;                            # set the boolean to true to indicate if person is inside
            return True                                     # return True
        else:
            return False                                    # Return False if the person already is inside the boat.

    '''
        Add a passenger to the boat, only if the boat is empty  The boat can only store one passenger. And the person
        needs to be outside of the boat to add a passenger.
        :param passenger: the passenger that want be come on board
        :return: True if the passenger was accepted, False if the boat is full.
    '''
    def add_passenger(self, passenger):
        if (not self.passenger) and (self.person is False):         # if there are not any passengers on the boat,
            self.passenger.append(passenger)                        # add passenger
            return True                                             # the passenger was accepted onto the boat
        return False                                                # the passenger was not accepted onto the boat

    '''
        remove the current passenger from the boat. and set the passenger list to empty. And the person
        needs to be outside of the boat to remove a passenger.
        :return: the passenger, if there is any passenger on the boat. otherwise return None.
    '''
    def remove_passenger(self):
        if (self.passenger is not None) and (self.person is False):    # check if there is anyone on the boat
            return self.passenger[0]                               # return the passenger
        else:
            return None                                             # there are no passenger to remove.

    '''
        Move the boat to the right
        :return: Return True if the boat was able to move position. || return false if the boat is not able to move.
    '''
    def move_right(self):
        if self.position < 3:                       # if the position is not all the way to the right
            self.position += 1                      # move the boat by 1 to the right

    '''
        Move the boat to the left
        :return: Return True if the boat was able to move position. || return false if the boat is not able to move.
    '''
    def move_left(self):
        if self.position > 1:                       # if the position is not all the way to the left
            self.position -= 1                      # move the boat by 1 to the left

    '''
        Get the position of where the boat is now.
        :return: the postion of the boat
    '''
    def get_position(self):
        return self.position                        # return the state of the boat.
