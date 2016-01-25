#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
import sys

alternatives = ["rock","scissor","paper"]
breakLine = "***************************************************"

balance = 1000
bet = 0

# Player chooses & Computer randomly choose
def play() :
    global balance
    print "You have now kr: %d on your account!" % balance 
    makeBet()
    # player choose
    inputChoose = raw_input("Please choose between Rock(0), Scissor(1) or Paper(2) : ")
       
    # Parse the string over to int
    try:
        userChoosed = int(inputChoose)
    except ValueError :
        userChoosed = lookForSentence(inputChoose)
    
    if (0 > userChoosed) or (userChoosed > 2):  
        print "Please choose a number between 0 - 2"
        # Resets the bet and returns money to balance
        balance = balance + bet
        bet = None
        # Calls play again
        play()
        
        
    # Computer random choose
    gameChoosed = randint(0,2)    
    
    # Print out game status
    getStatus(userChoosed, gameChoosed)    
    
    # calculate who the winner is
    calculateWinner(userChoosed, gameChoosed)

# if no numbers is inserted, look for sentence
def lookForSentence(inputChoose) :
    
    # Loop through options
    i = 0
    for options in alternatives :
        if (options.upper() == inputChoose.upper()) :
            return i
        i += 1
    
    # If there are no such word to choose from, alert user and let them try again
    # Resets the bet and returns money to balance
    balance = balance + bet
    bet = None
    print "Please insert rock, scissor or paper"
    # Calls Play again
    play()
            

    
# get status
def getStatus(userChoosed, gameChoosed) :
    print breakLine
    print "Player throws "  + alternatives[userChoosed] + " | Computer throws " + alternatives[gameChoosed]
    print breakLine
    

#calculate who the winner is
def calculateWinner(userChoosed, gameChoosed) :
    global balance
    global bet
    # 0 = Stone
    # 1 = Scissor
    # 2 = Paper
    
    # Scissor beats paper
    # Paper beats stone
    # Stone beats scissor
    
    playerWonText = "Player wins!"
    computerWonText = "Computer wins!"
    tieText = "It's a tie!"
    
    # All possibilities where player wins
    if (userChoosed is 0 and gameChoosed is 1) \
        or (userChoosed is 1 and gameChoosed is 2) \
        or (userChoosed is 2 and gameChoosed is 0) :
        print playerWonText
        addMoney()
        
    # All possibilities where computer wins
    elif (userChoosed is 1 and gameChoosed is 0) \
        or (userChoosed is 2 and gameChoosed is 1) \
        or (userChoosed is 0 and gameChoosed is 2) :
        print computerWonText

    # All possibilities where it's a tie
    elif (userChoosed is gameChoosed) :
        print tieText
        balance = balance + bet
        
    
    print breakLine
    playAgain() 
    

# Ask the user if he wants to play again    
def playAgain() :
    
    # Gives the user ability to choose
    answer = raw_input("Play again, Y or N: ")
    possibleYesAnswers = ["Yes", "ok", "yeah", "y"]
    possibleNoAnswers = ["No","n","nope"]
    
    # If user has inserted a no answer
    for i in possibleNoAnswers :
        if (answer.upper() == i.upper()):
            print "Thank you for playing!"
            sys.exit("Thank you for playing!")

    # If user has inserted a yes answer
    for i in possibleYesAnswers :
        if (answer.upper() == i.upper()):
            bet = None
            play()

    # Answer is not a valid answer
    print "Try again!"
    playAgain()
    


def makeBet() :
    
    global balance
    bet = raw_input("Please insert your bet: ")
    try :
        global bet
        bet = int(bet)    
    except ValueError :
        print "Enter a number."
        makeBet()
        
    # Removes money from balance
    if (bet <= balance) and (bet > 0) :
        balance = balance - bet 
    else :
        print "You don't have enough money for this bet or have entered a negative value."
        makeBet()
        
def addMoney() :
    global balance
    balance = balance + (bet*2)
    print "Profit has been transferred to your account!"


    
# Run the program

play()