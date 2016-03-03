class Boat:
    def __init__(self):
        self.person = False                         # Is the person on board?
        self.passenger = []                         # passengers on the boat, in this example it would be animals
        self.position = ""                          # the position of the boat

    '''
        Add a passenger to the boat, only if the boat is empty  The boat can only store one passenger
        :param passenger: the passenger that want be come on board
        :return: True if the passenger was accepted, False if the boat is full.
    '''
    def add_passenger(self, passenger):
        if not self.passenger:                      # if there are not any passengers on the boat,
            self.passenger.append(passenger)        # add passenger
            return True                             # the passenger was accepted onto the boat
        return False                                # the passenger was not accepted onto the boat

    '''
        remove the current passenger from the boat. and set the passenger list to empty.
        :return: the passenger, if there is any passenger on the boat. otherwise return None.
    '''
    def remove_passenger(self):
        if len(self.passenger) < 1:                 # check if there is anyone on the boat
            return self.passenger.put(0)            # return the passenger
        else:
            return None                             # if there are not passenger onto the boat, return nothing.

    
    def move_boat(self):
        pass

    def get_position(self):
        return self.position
