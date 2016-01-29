# -*- coding: utf-8 -*-
import random 
from random import randint


def deal(pokerCards) :
    '''
    Create 5 player and deal out 5 cards to each player
    '''
    players = []
    i = 0
    y = 0 # card number
    for i in range(0,5) :
        cardToPlayer = []
        x = 0
        
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
    pokerCards = []
    
    i = 0                   # For loop
    x = 0                   # for loop
    symbole = 0             # deligere symbole
    value = 0               # Deligere value
    
    for x in range (0,4) :
        for i in range(0,12 ) :
            obj = PokerCard(symbole, value)
            pokerCards.append(obj)
            value += 1
        symbole += 1
        value = 0
    
    pokerCards = random.sample(pokerCards, len(pokerCards))     
    return pokerCards
               

'''
Each card is a object of pokercard
'''
class PokerCard:

    def __init__ (self, symbole, value) :
        '''
        Symbole er da hvilken type kort det er. 
        Value er da hvilken verdi kortet har
        
        '''
        self.symbole = symbole
        self.value = value
        
    # Return value of the card 
    def getValue(self) :
        return self.value

    # Return the symboleValue
    def getSymbole(self) :
        return self.symbole
    
    # Set the value over to string for reading
    def getStringValue(self) :
        value = ["2","3","4","5","6","7","8","9","10","Knekt","Dronning","Konge","Ess"]
        return value[self.value]
    
    # set the symbole value over to string for reading
    def getStringSymbole(self) :
        symbole_name = ['ruter', 'hjerter', 'spar', 'klover']
        return symbole_name[self.symbole]


'''
Each player is a object og the class
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
        
        #set the random name
        self.name = names[randint(0, 6)]
        
    # Return the name of the player    
    def getName(self):
        return self.name
    
    # return the cards of the player
    def getCards(self):
        return self.cards

 
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
        print obj[x].getStringSymbole() + " " + obj[x].getStringValue()
        x += 1
