# -*- coding: utf-8 -*-
import random 
from random import randint
import Pointcalc_Poker
import CalculateWinner

def deal(pokerCards) :
    '''
    Create 6 player and deal out 5 cards to each player
    '''
    players = []
    i = 0
    y = 0 # card number
    
    # Create 6 players
    for i in range(0,6) :
        cardToPlayer = []
        x = 0
        # Give each 6 player 5 cards
        for x in range(0,5):
            cardToPlayer.append(pokerCards[y])
            y += 1
            
        players.append(Player(cardToPlayer))
        
    return players

def generateCards():
    '''
    Generate cards and then shuffle them
    @return shuffled deck
    '''
    pokerCards = [] #The veriable that holds all the cards
    deck = 20 # How many deck that is created
    y = 0 # For loop
    
    # create deck(s)
    for y in range(0,deck) :
        
        i = 0                   # For loop
        x = 0                   # for loop
        symbole = 0             # deligere symbole
        value = 0               # Deligere value
        
        
        '''
        Generate a deck of cards
        '''
        for x in range (0,4) :
            for i in range(0,13) :
                obj = PokerCard(symbole, value)
                pokerCards.append(obj)
                value += 1
            symbole += 1
            value = 0
    
    
    #Shufle the deck and return it
    return random.sample(pokerCards,len(pokerCards))    
   


'''
Each card is a object of pokercard
'''
class PokerCard:

    def __init__ (self, symbol, value) :
        '''
        Symbole er da hvilken type kort det er. 
        Value er da hvilken verdi kortet har
        
        '''
        self.symbol = symbol
        self.value = value
    def __repr__(self):
            return repr((self.symbol, self.value))        
    # Return value of the card 
    def getValue(self) :
        return self.value

    # Return the symboleValue
    def getSymbol(self) :
        return self.symbol
    
    # Set the value over to string for reading
    def getStringValue(self) :
        value = ["2","3","4","5","6","7","8","9","10","Knekt","Dronning","Konge","Ess"]
        return value[self.value]
    
    # set the symbole value over to string for reading
    def getStringSymbol(self) :
        symbol_name = ['Spar', 'kløver', 'hjerter', 'ruter']
        return symbol_name[self.symbol]


'''
Each player is a object og the clas
'''
class Player :
    def __init__ (self, cards) :
        '''
        Give the player random name
        '''
        #possible names
        names = ["Christian", "Erlend", "Ola", "Tommy Woa", "Merethe<3", "Benny", "Janis"]
        
        # set the deck of the player
        self.cards = cards
        self.points = Pointcalc_Poker.calculatePoints(cards)
        
        #set the random name
        self.name = names[randint(0, 6)]
        
    # Return the name of the player    
    def getName(self):
        return self.name
    
    # return the cards of the player
    def getCards(self):
        return self.cards

    def getPoints(self):
        return self.points
 
    def getHandName(self):
        points = self.points
        if points < 200 :                                        # 2 of a kind
            return "2 like(Par)"    
        elif (points >= 80000) and (points < 85000) :            # 3 of a kind
            return "3 like(Three of a kind)"
        elif (points >= 100000) and (points < 105000) :          # Straight
            return "Straight"
        elif (points >= 120000) and (points < 130000) :          # Flush
            return "Flush"
        elif (points >= 140000) and (points < 150000) :          # Full house
            return "Fult hus"
        elif (points >= 160000) and (points < 170000) :          # 4 of a kind
            return "Fire like"
        elif (points >= 480000) and (points < 490000) :          # Straight flush
            return "Straight flush"
        elif (points >= 500000) and (points < 520000) :          # Royal flush
            return "Royal flush"
        else:
            return "Ingen ting"
# Do stuff...  
            


cards = generateCards()
players = deal(cards)

i = 0
for i in range(0,len(players)) :
    print 
    obj = players[i].getCards()
    print players[i].getName()

    x = 0
    while len(obj) > x :
        print obj[x].getStringSymbol() + " " + obj[x].getStringValue()
        x += 1
    
    point = str(players[i].getPoints())
    handname = players[i].getHandName()
    print ("players scores " + point )
    print handname
    
print 
print "winner is:"
print CalculateWinner.CalculateWinner(players).getName()
print
obj = CalculateWinner.CalculateWinner(players).getCards()
print"med disse kortene:"
x = 0

while len(obj) > x :
    print obj[x].getStringSymbol() + " " + obj[x].getStringValue()
    x += 1
        