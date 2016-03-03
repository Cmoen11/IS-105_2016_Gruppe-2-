class Position :
    def __init__(self):
        self.position_A = ["Corn", "Fox", "Chicken"]
        self.position_B = []

    def position_a_add(self, passenger):
        self.position_A.append(passenger)

    def position_a_remove(self, passenger, boat_pos):
        if not self.check_boat_position_a(boat_pos):
            return False

        if passenger in self.position_A:
            self.position_A.remove(passenger)
            return passenger

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