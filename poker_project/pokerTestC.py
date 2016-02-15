import unittest
import Poker
import Pointcalc_Poker

class TestRoyalFlush(unittest.TestCase):
    
    pokerCards = []
    def setUp(self):
        i = 0
        startCard = 8
        self.pokerCards = []
        for i in range(0,5) :
            obj = Poker.PokerCard(0, startCard)
            self.pokerCards.append(obj)
            startCard += 1
             
    def test_testCalculatePoints_royalFLush(self):
        self.assertEqual(Pointcalc_Poker.checkRoyalFlush(self.pokerCards), 500000)



class TestStraightFlush(unittest.TestCase):
    pokerCards = []
    def setUp(self):
        i = 0
        startCard = 4
        pokerCards = []
        for i in range(0,5) :
            obj = Poker.PokerCard(0, startCard)
            self.pokerCards.append(obj)
            startCard += 1
             
    def test_testCalculatePoints_StraightFlush(self):
        self.assertEqual(Pointcalc_Poker.checkStraightFlush(self.pokerCards), 480000)
        
        
class TestFourOfaKind(unittest.TestCase):
    cards = []
    pokerCards = []
    def setUp(self) :
        self.cards = [
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,9),
            Poker.PokerCard(2,10),
            Poker.PokerCard(2,0),
            Poker.PokerCard(2,1),

            ]            
        self.pokerCards = [
            Poker.PokerCard(1,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(3,2),
            Poker.PokerCard(4,2),
            Poker.PokerCard(5,2),

            ]          
            
    # A test where cards are four of a kind.         
    def test_testCalculatePoints_FourOfAKind(self):
        global pokerCards
        self.assertEqual(Pointcalc_Poker.checkFourOfaKind(self.pokerCards), 160002)
    
    # A test where no cards are four of a kind.    
    def test_testCalculatePoints_FourOfAKind_2(self):
        self.assertEqual(Pointcalc_Poker.checkFourOfaKind(self.cards), 0)    
        

class TestPair(unittest.TestCase):
    pokerCards = []
    def setUp(self):
        self.pokerCards = []
        
        # this is a pair of fours
        self.pokerCards.append(Poker.PokerCard(0,2))
        self.pokerCards.append(Poker.PokerCard(1,2))
        
        # the three remaining cards
        for i in range (5,8) :
            obj = Poker.PokerCard(0,i)
            self.pokerCards.append(obj)            
                
            
        self.cards = [
                    Poker.PokerCard(2,6),
                    Poker.PokerCard(2,7),
                    Poker.PokerCard(2,12),
                    Poker.PokerCard(2,3),
                    Poker.PokerCard(2,12),
        
                    ]        
    def test_testCalculatePoints_testPair(self):
        self.assertEqual(Pointcalc_Poker.checkPair(self.pokerCards), 102)
    def test_testCalculatePoints_testPair(self):
            self.assertEqual(Pointcalc_Poker.checkPair(self.cards), 112)
    

class TestFullHouse(unittest.TestCase):
    pokerCards = []
    cards = []
    def setUp(self):
        self.pokerCards = []
        self.cards = []

        self.cards = [
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,2),

            ]       
        
    def test_testCalculatePoints_TestFullHouse(self):
            self.assertEqual(Pointcalc_Poker.checkFullHouse(self.cards), 140000)        
  
class TestFlush(unittest.TestCase): 
    pokerCards = []
    pokerCards2 = []
    def setUp(self):
        self.pokerCards = [
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,1),
      
        ]
        self.pokerCards2 = [
            Poker.PokerCard(1,9),
            Poker.PokerCard(2,4),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,11),
      
        ]        

    def test_testCalculatePoints_flush(self):
        self.assertEqual(Pointcalc_Poker.calculatePoints(self.pokerCards), 120000)
    def test_testCalculatePoints_flush2(self):
        self.assertEqual(Pointcalc_Poker.calculatePoints(self.pokerCards2), 29)    

class TestStraight(unittest.TestCase):
    pokerCards = []
    cards = []
    def setUp(self):
        i = 0 
        self.pokerCards = [
            Poker.PokerCard(2,0),
            Poker.PokerCard(2,1),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,4),
      
        ]
        
    def test_testCalcualtePoints7(self):
        self.assertEqual(Pointcalc_Poker.checkStraight(self.pokerCards), 100004)
    

class TestThreeOfaKind(unittest.TestCase):
    pokerCards = []
    cards = []
    def setUp(self):
        i = 0
        self.pokerCards = [
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,3),
            Poker.PokerCard(2,2),
            Poker.PokerCard(2,1),
      
        ]
        
        
    def test_testCalculatePoints_ThreeOfAKind(self):
        self.assertEqual(Pointcalc_Poker.checkThreeOfaKind(self.pokerCards), 80040)
        
        

    
if __name__ == '__main__':
    unittest.main()
    
    
