# -*- coding: utf-8 -*-
def calculatePoints(cards) :
    '''
    this method will return back a 'score' of the selected score, in order to find the winner.
    '''
    #Score given:
    points = 0;
    
    '''
    Run trought every "hand" you can get, from the highest to the lowest. Stop when you've reached the higest hand
    and return the points
    '''
    # Royal flush check
    points = checkRoyalFlush(cards)              # Value given if found is 500 000
    if (points > 0 ) :
        return points
     
    #Straight Flush check
    points = checkStraightFlush(cards)           # Value given if found is 480 000
    if (points > 0 ) :
        return points    
        
    #Four of a kind check
    points = checkFourOfaKind(cards)             # Depends on value of the cards.. 
    if (points > 0 ) :                      
        return points       

    #Full house check 
    points = checkFullHouse(cards)               # Valie given if found is 140 000
    if (points > 0 ) :  
        return points
    
    #Flush check
    points = checkFlush(cards)                   # Value given if found is 120 000
    if (points > 0):
        return points
    
    #Sraight check
    points = checkStraight(cards)                # Value given if found is 100 000
    if (points > 0):
        return points
    
    #three like check
    points = checkThreeOfaKind(cards)            # Value given if found is 80 000 + 20 for each card higher than 0
    if (points > 0):
        return points    
    
    # pair of 2's check 
    points = checkPair(cards)                    # Depends on value of the cards.. 
    if (points > 0) :
        return points
    
    
    else :
        points = checkForHighCard(cards)
        return points                              # Player has not got any hand of value
    
    
def checkStraightFlush (cards):
    #Sort the cards
    cards = sortList(cards)
    
    #Check the colour of the card
    color = checkIfAllCardsIsBlack(cards) # if all the cards colour is black
    
    if (color is False) :   # If the colour is not black, check if all is red 
        color = checkIfAllCardsIsRed(cards)
    
    # Check if is a straight flush  
    if (cards[0].getValue() == 4) \
       and (cards[1].getValue() == 5) \
       and (cards[2].getValue() == 6) \
       and (cards[3].getValue() == 7) \
       and (cards[4].getValue() == 8) :
        return 480000
    return 0
def checkFourOfaKind(cards) :
    i = 0
    ekstraPoint = 0
    cards = sortList(cards)
    # Go through each card value and see if any of them are alike. Add also 20 exstra points for each run, so higher card values give higher score
    for i in range(0,12):
        if (cards[0].getValue() == i) \
           and (cards[1].getValue() == i) \
           and (cards[2].getValue() == i) \
           and (cards[3].getValue() == i):
            return 160000 + ekstraPoint
        if (cards[4].getValue() == i) \
           and (cards[3].getValue() == i) \
           and (cards[2].getValue() == i) \
           and (cards[1].getValue() == i) :
                return 160000 + ekstraPoint        
        else:
            ekstraPoint += 20
            
    return 0
def checkFullHouse(cards) : 
    i = 0
    ii = 0
    ekstraPoint = 0
    
    cards = sortList(cards)
    # Go through each card value and see if there is 3 alike and 2 alike.
    for i in range(0,12):
        for ii in range (0,12):
            if(cards[0].getValue() == i) \
              and (cards[1].getValue() == i) \
              and (cards[2].getValue() == i) \
              and (cards[3].getValue() == ii) \
              and (cards[4].getValue() == ii):
                return 140000 + ekstraPoint   
            
            if(cards[1].getValue() == i) \
              and (cards[2].getValue() == i) \
              and (cards[3].getValue() == i) \
              and (cards[4].getValue() == ii) \
              and (cards[0].getValue() == ii):
                return 140000 + ekstraPoint            


            if(cards[2].getValue() == i) \
              and (cards[3].getValue() == i) \
              and (cards[4].getValue() == i) \
              and (cards[0].getValue() == ii) \
              and (cards[1].getValue() == ii):
                return 140000 + ekstraPoint        


            if(cards[3].getValue() == i) \
              and (cards[4].getValue() == i) \
              and (cards[0].getValue() == i) \
              and (cards[1].getValue() == ii) \
              and (cards[2].getValue() == ii):
                return 140000 + ekstraPoint            
            
            if(cards[4].getValue() == i) \
              and (cards[0].getValue() == i) \
              and (cards[1].getValue() == i) \
              and (cards[2].getValue() == ii) \
              and (cards[3].getValue() == ii):
                return 140000 + ekstraPoint   
                      

            
            else: 
                ekstraPoint +=20
        
            
    return 0




def checkFlush(cards) :
    if (checkForSameType(cards)) :
        return 120000
    return 0
def checkStraight(cards) :
    return 0
def checkThreeOfaKind(cards) :
    i = 0
    ekstraPoint = 0
    
    # Sett kortene i stigende rekkefølge
    cards = sortList(cards)
    for i in range(0,12):
        #Sjekk om det er 3 like i stigende rekkefølge
        if(cards[0].getValue() == i) \
          and (cards[1].getValue() == i) \
          and (cards[2].getValue() == i) :
            return 80000 + ekstraPoint
        
        #Sjekk om det er 3 like  fra høyt til lavt
        elif(cards[1].getValue() == i) \
            and (cards[2].getValue() == i) \
            and (cards[3].getValue() == i) :
            return 80000 + ekstraPoint
        
        # sjekk i midten av bunken
        elif (cards[2].getValue() == i) \
            and (cards[3].getValue() == i) \
            and (cards[4].getValue() == i) :
            
            return 80000 + ekstraPoint
        
        
        else:
            ekstraPoint += 20
                
    return 0
                
                
def checkRoyalFlush (cards) :
    
    #Sort the cards
    cards = sortList(cards)
    #Check the colour of the card
    color = checkIfAllCardsIsBlack(cards) # if all the cards colour is black
    
    if (color is False) :   # If the colour is not black, check if all is red 
        color = checkIfAllCardsIsRed(cards)
    
    
    if (color) : # if either all of the cards is red or black
        #Check if is royal flush
        if (cards[0].getValue() == 8) \
            and (cards[1].getValue() == 9) \
            and (cards[2].getValue() == 10) \
            and (cards[3].getValue() == 11) \
            and (cards[4].getValue() == 12):            
            return 500000
    return 0

def checkIfAllCardsIsBlack(cards) :
    cardsBlack = 0 # To hold on how many black card that is been found
    i = 0 # for loop
    
    # Run trough every card, and increment by one
    for i in cards :
        if (i.getSymbol() == 0) or (i.getSymbol() == 1) :
            cardsBlack += 1
    # if all the cards is black, return true, if not return false.      
    if (cardsBlack == 5) :
        return True
    return False
 
def checkIfAllCardsIsRed(cards) :
    cardsRed= 0 # To hold on how many red card that is been found
    i = 0 # For loop
    
    # Run trough every card, and increment by one
    for i in cards :
        if (i.getSymbol() == 3) or (i.getSymbol() == 4) :
            cardsRed += 1
    
    # if all the cards is red, return true, if not return false.    
    if (cardsRed == 5) :
        return True
    return False            

def checkPair(cards) :
    i = 0
    # For each card
    for i in range(0,5):
        # for et pair + ekstra like kort
        pair_point = 2 
        #ekstra points
        ekstraPoint = 0
        # Check each card
        x = 0
        for x in range(0, 5):

            # Jump over current card 
            if (x is not i) :
                if (cards[i].getValue() == cards[x].getValue()) :
                    #print "match found!"
                    
                    # Check if the pair is higher than 0 (pair in 2's)
                    if (cards[i].getValue() > 0) : 
                        
                        y = 0    
                        
                        for y in range (0,14) :
                            if (cards[i].getValue() == y) :
                                break
                            else :
                                # Add exstra point
                                ekstraPoint += 1
                    
                    # Add points            
                    return pair_point + ekstraPoint + 100   
                
                
def checkForHighCard(cards):
    # add each card value to the score
    score = 0
    for card in cards :
        score = score + card.getValue()
    return score
        
def checkForSameType(cards):
    i = 0
    for i in range(0,4) :
        if (cards[0].getSymbol() == i) \
           and (cards[1].getSymbol() == i) \
           and (cards[2].getSymbol() == i) \
           and (cards[3].getSymbol() == i) \
           and (cards[4].getSymbol() == i) :
            return True
    return False
        
def sortList(cards) :
    return sorted(cards, key=lambda PokerCards: PokerCards.value, reverse=False)

    