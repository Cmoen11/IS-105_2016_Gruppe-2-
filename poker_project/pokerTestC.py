import unittest
import Poker
import Pointcalc_Poker

class TestRoyalFlush(unittest.TestCase):
    
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
             
    def test_testCalculatePoints_royalFLush(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 500000)



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
             
    def test_testCalculatePoints_StraightFlush(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 480000)
        
        
class TestFourOfaKind(unittest.TestCase):
    cards = []
    pokerCards = []
    def setUp(self) :
        global cards
        global pokerCards
        cards = [
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,9),
            Poker.PokerCard(2,10),
            Poker.PokerCard(2,0),
            Poker.PokerCard(2,1),

            ]            
        pokerCards = [
            Poker.PokerCard(1,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(3,2),
            Poker.PokerCard(4,2),
            Poker.PokerCard(5,2),

            ]          
            
    # A test where cards are four of a kind.         
    def test_testCalculatePoints_FourOfAKind(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 160040)
    
    # A test where no cards are four of a kind.    
    def test_testCalculatePoints_FourOfAKind_2(self):
        global cards
        self.assertEqual(Pointcalc_Poker.checkFourOfaKind(cards), 0)    
        

class TestPair(unittest.TestCase):
    pokerCards = []
    def setUp(self):
        global pokerCards
        pokerCards = []
        
        # this is a pair of twos
        pokerCards.append(Poker.PokerCard(0,2))
        pokerCards.append(Poker.PokerCard(1,2))
        
        # the three remaining cards
        i = 5
        for i in range (5,8) :
            obj = Poker.PokerCard(0,i)
            pokerCards.append(obj)            
                

    def test_testCalculatePoints_testPair(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 104)
        

class TestFullHouse(unittest.TestCase):
    pokerCards = []
    cards = []
    def setUp(self):
        i = 0
        global pokerCards
        global cards
        pokerCards = []
        cards = []

        cards = [
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,3),

            ]       
        
    def test_testCalculatePoints_TestFullHouse(self):
            global cards
            self.assertEqual(Pointcalc_Poker.calculatePoints(cards), 140540)        
  
class TestFlush(unittest.TestCase): 
    pokerCards = []
    pokerCards2 = []
    def setUp(self):
        global pokerCards
        global pokerCards2
        pokerCards = [
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,1),
      
        ]
        pokerCards2 = [
            Poker.PokerCard(1,9),
            Poker.PokerCard(2,4),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,12),
      
        ]        

    def test_testCalculatePoints_flush(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards), 120000)
    def test_testCalculatePoints_flush2(self):
        global pokerCards2
        self.assertEqual(Pointcalc_Poker.calculatePoints(pokerCards2), 30)    

class TestStraight(unittest.TestCase):
    pokerCards = []
    cards = []
    def setUp(self):
        i = 0 
        self.pokerCards[
             Poker.PokerCard(1,0),
             Poker.PokerCard(3,1),
             Poker.PokerCard(2,2),
             Poker.PokerCard(2,3),
             Poker.PokerCard(0,4)
            ]
        
    def test_testCalcualtePoints7(self):
        self.assertEqual(Pointcalc_Poker.checkStraight(self.pokerCards), 100000)
    

class TestThreeOfaKind(unittest.TestCase):
    pokerCards = []
    cards = []
    def setUp(self):
        i = 0
        global pokerCards
        pokerCards = [
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,1),
      
        ]
        
        
    def test_testCalculatePoints_ThreeOfAKind(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.checkThreeOfaKind(pokerCards), 80040)
        
        

    
if __name__ == '__main__':
    unittest.main()
    
    
