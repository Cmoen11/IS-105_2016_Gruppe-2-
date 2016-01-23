#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
import sys
alternativer = ["stein","saks","papir"]
breakLine = "***************************************************"


# Player chooses & Computer randomly choose
def play() :
    # player choose
    inputChoose = raw_input("Vennligst velg mellom Stein(0), Saks(1) eller Papir(2) : ")
       
    # Parse the string over to int
    try:
        userChoosed = int(inputChoose)
    except ValueError :
        userChoosed = lookForSentence(inputChoose)
    
    if (0 > userChoosed) or (userChoosed > 2):  
        print "Vennligst velg et tall mellom 0 - 2"
        play()
        
        
    # Computer random choose
    gameChoosed = randint(0,2)    
    
    # Print out game status
    getStatus(userChoosed, gameChoosed)    
    
    # calculate who the winner is
    calculateWinner(userChoosed, gameChoosed)

# if no numbers is inserted, look for sentence
def lookForSentence(inputChoose) :
    
    # Loop trought options
    i = 0
    for options in alternativer :
        if (options.upper() == inputChoose.upper()) :
            return i
        i += 1
    
    # If there are no such word to choose from, alert user and let them try again
    print "Vennligst skriv inn Stein, saks eller papir"
    play()
        

    
# get status
def getStatus(userChoosed, gameChoosed) :
    print breakLine
    print "Spiller kaster "  + alternativer[userChoosed] + " | Maskin kaster " + alternativer[gameChoosed]
    print breakLine
    

#calculate who the winner is
def calculateWinner(userChoosed, gameChoosed) :
    
    # 0 = Stein
    # 1 = Saks
    # 2 = Papir
    
    # Saks slår papir
    # Stein slår Saks
    # saks slår papir
    
    playerWonText = "Spiller Vinner"
    computerWonText = "Datamaskinen vinner"
    tieText = "Det ble uavgjort"
    
    # alle mulige spill der spiller vinner
    if (userChoosed is 0 and gameChoosed is 1) \
        or (userChoosed is 1 and gameChoosed is 2) \
        or (userChoosed is 2 and gameChoosed is 0) :
        print playerWonText
    
    # alle mulige spill der datamaskinen vinner
    elif (userChoosed is 1 and gameChoosed is 0) \
        or (userChoosed is 2 and gameChoosed is 1) \
        or (userChoosed is 0 and gameChoosed is 2) :
        print computerWonText

    # alle mulige spill der det kan bli uavgjort
    elif (userChoosed is gameChoosed) :
        print tieText
    
    print breakLine
    playAgain()    

# ask the user if he wants to play again    
def playAgain() :
    # Give the user ability to choose
    answer = raw_input("Spill igjen, Y or N: ")
    possibleYesAnswers = ["Yes", "ok", "yeah", "y"]
    possibleNoAnswers = ["No","n","nope"]
    
    # If user has inserted a no answer
    for i in possibleNoAnswers :
        if (answer.upper() == i.upper()):
            print "Takk for at du spilte!"
            sys.exit("Takk for at du spilte!")

    # IF user has inserted a yes answer
    for i in possibleYesAnswers :
        if (answer.upper() == i.upper()):
            play()

    # Answer is not a valid answer
    print "Prøv på nytt"
    playAgain()
    

# run the program
play()
