class Position :
    def __init__(self):
        self.position_A = ["Corn", "Fox", "Chicken"]                # The items / animals the selected position has
        self.position_B = []                                        # The items / animals the selected position has

    '''
        Append passenger to the position A or B
        :return: True if he either appended to A or B | False if pos was 3, because 3 is in the middle of sea.
    '''
    def position_add(self, passenger, boat_pos):
        if boat_pos == 1:                                           # if the boat is at position A
            self.position_A.append(passenger)                       # Append selected passenger to pos A
            return True

        elif boat_pos == 3:                                         # if the boat is at position B
            self.position_B.append(passenger)                       # Append the passenger to position B
            return True

        else:
            return False


    '''
        remove a passenger from position A.
        :return: return passenger if the passenger is at the position
    '''
    def position_a_remove(self, passenger, boat_pos):

        # If the passenger is at position a, and the boat is at position a.
        if (passenger in self.position_A) and (self.check_boat_position_a(boat_pos)):
            self.position_A.remove(passenger)                       # remove the passenger from the position
            return passenger                                        # return the passenger that has been removed
        return False                                                # boat or passenger are not at A.


    def position_b_add(self, passenger):
        self.position_B.append(passenger)

    def position_b_remove(self, passenger, boat_pos):
        if not self.check_boat_position_b(boat_pos) :
            return False

        if passenger in self.position_A:
            self.position_B.remove(passenger)
            return passenger

    '''
        Check if the boat is near position A.
        :return: return True if the boat is pos 1 || return false if the boat is not near.
    '''
    def check_boat_position_a(self, boat_position):
        if boat_position == 1:
            return True
        return False

    '''
        Check if the boat is near position B.
        :return: return True if the boat is pos 3 || return false if the boat is not near.
    '''
    def check_boat_position_b(self, boat_position):
        if boat_position == 3:
            return True
        return False