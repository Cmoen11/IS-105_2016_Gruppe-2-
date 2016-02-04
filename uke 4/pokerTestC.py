import unittest
import Poker
import Pointcalc_Poker

class TestCalculatePoints(unittest.TestCase):
    
    pokerCards = []
    def setUp(self):
        i = 0
        startCard = 8
        global pokerCards
        pokerCards = []
        for i in range(0,5) :
            obj = Poker.PokerCard(0, startCard)
            pokerCards.append(obj)
            startCard += 1
             
    def test_testCalculatePoints(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.checkRoyalFlush(pokerCards), 500000)



class TestStraightFlush(unittest.TestCase):
    pokerCards = []
    def setUp(self):
        i = 0
        startCard = 4
        global pokerCards
        pokerCards = []
        for i in range(0,5) :
            obj = Poker.PokerCard(0, startCard)
            pokerCards.append(obj)
            startCard += 1
             
    def test_testCalculatePoints(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 480000)


if __name__ == '__main__':
    unittest.main()
    
    
    