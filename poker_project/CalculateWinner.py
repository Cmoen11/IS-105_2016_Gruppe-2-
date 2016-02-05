

def CalculateWinner(players) :
  
  # Find 3 candicates
  winner1 = returnHighestObject(players[0], players[1]) 
  winner2 = returnHighestObject(players[2], players[3])
  winner3 = returnHighestObject(players[4], players[5]) 
  
  # Find the winner
  if (winner1.getPoints() > winner2.getPoints()) \
     and (winner1.getPoints() > winner3.getPoints()) :
    return winner1
  
  if (winner2.getPoints() > winner1.getPoints()) \
     and (winner2.getPoints() > winner3.getPoints()) :
    return winner2
  
  if (winner3.getPoints() > winner1.getPoints()) \
     and (winner3.getPoints() > winner1.getPoints()) :
    return winner3  
    
    
#This method take's tho objects, 
#will return the object with highest value variable back



def returnHighestObject (obj1, obj2):
    
    if obj1.getPoints() > obj2.getPoints():
        return obj1
    elif obj1.getPoints() == obj2.getPoints():
        #Need to look for highest card...
        return obj1
    elif obj1.getPoints() < obj2.getPoints():
      return obj2
    
