# -*- coding: utf-8 -*-
import unittest
import Boat
import Position


class TestBoat(unittest.TestCase):
    def setUp(self):
        self.boat = Boat.Boat()                                             # Create the boat object
        self.position = Position.Position()                                 # Create the position object

    def testAddPassenger_PersonNotInBoat(self):
        self.assertEqual(
            self.boat.add_passenger(                                                    # Add passenger to the boat.
                self.position.position_a_remove("Corn", self.boat.get_position())),     # remove the passenger
            True)

    def testAddPassenger_PersonIsInBoat(self):
        self.boat.add_person()                                                          # Add person to the boat.
        self.assertEqual(
            self.boat.add_passenger(                                                    # Add passenger to the boat
                self.position.position_a_remove("Corn", self.boat.get_position())),     # remove the passenger
            False)

    def testRemovePassenger_PersonNotInBoat(self):
        self.boat.add_passenger(
            self.position.position_a_remove("Corn", self.boat.get_position())  # Add passenger and remove from position
        )

        if self.assertEqual(self.boat.remove_passenger(), 'Corn', self.boat.get_position()):    # Remove passenger
            self.assertEqual(self.position.position_a_add("Corn"), True)    # Add the passenger to the position

    def testRemovePassenger_PersonIsInBoat(self):
        self.boat.add_passenger(
            self.position.position_a_remove("Corn", self.boat.get_position())  # Add passenger and remove from position
        )
        self.boat.add_person()
        self.assertEqual(self.boat.remove_passenger(), None)              # try to remove the passenger
