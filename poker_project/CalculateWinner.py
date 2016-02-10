'''
Here we need to do some changes. Because we are in need to have exacly 6 players in order
to have this working. And we've done nothing if we got two or more people with exacly the 
same score.

Basicly the functionallity of the current state is that it's hard coded in to face 6 
players.
*******

EDIT:
Fixed it with sorting the list if the higest score. And just return the first of the list

'''

def CalculateWinner(players) :
  
  players = sortList(players)
  return players[0]
     
def sortList(players) :
  # Sort by points
  # @return a list were the highest score is displayed first
  return sorted(players, key=lambda PokerCards: PokerCards.points, reverse=True)