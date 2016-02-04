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
             
    def test_testCalculatePoints1(self):
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
             
    def test_testCalculatePoints2(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 480000)
        
        
class TestFourLike(unittest.TestCase):
    pokerCards = []
    cards = []
    def setUp(self):
        i = 0
        global pokerCards
        global cards
        pokerCards = []
        cards = []
        for i in range(0,5) :
            obj = Poker.PokerCard(0,0)
            pokerCards.append(obj)
            
        for i in range(0,5) :
            obj = Poker.PokerCard(0,i)
            cards.append(obj)
            
            
    # A test where cards are four of a kind.         
    def test_testCalculatePoints3(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 460000)
    
    # A test where no cards are four of a kind.    
    def test_testCalculatePoints3(self):
        global cards
        self.assertEqual(Pointcalc_Poker.calculatePoints(cards), 0)    



if __name__ == '__main__':
    unittest.main()
    
    
    