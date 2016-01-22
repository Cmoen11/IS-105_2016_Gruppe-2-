#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

alternativer = ["Stein","Saks","Papir"]

def run() :
    # Player chooses & Computer randomly choose
    play()
    

# Player chooses & Computer randomly choose
def play() :
    # player choose
    inputChoose = raw_input("Vennligst velg mellom Stein(0), Saks(1) eller Papir(2) : ")
       
    # Parse the string over to int
    try:
        userChoosed = int(inputChoose)
    except ValueError :
        print "Vennligst fyll ut med tall."
        play()
    
    if (0 > userChoosed) or (userChoosed > 2):  
        print "Vennligst velg et tall mellom 0 - 2"
        play()
        

        
    else :
        # Computer random choose
        gameChoosed = randint(0,2)    
    
        # Print out game status
        getStatus(userChoosed, gameChoosed)    
    
        # calculate who the winner is
        calculateWinner(userChoosed, gameChoosed)
    
# get status
def getStatus(userChoosed, gameChoosed) :
    print "***************************************************"
    print "Spiller kaster "  + alternativer[userChoosed] + " | Maskin kaster " + alternativer[gameChoosed]
    print "***************************************************"
    


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
    

    
    #print a break line
    print "***************************************************"
    
    # Ask user if he wants to play again    
    playAgain()    

# ask the user if he wants to play again    
def playAgain() :
    # Give the user able to choose
    answer = raw_input("Spill igjen, Y or N: ")
    # Set the answer to uppercase
    answer = answer.upper()
    if (answer == "Y") or (answer == "N") :
        
        if (answer == "Y") : 
            run()
    else :
        errorMessage(1)
    
# display error message
def errorMessage(errorMessage):
    
    
    # if user has entered inn wrong under "play again"
    if (errorMessage is 1) :
        print "Vennligst tast inn Y eller N"
        playAgain()    


# run the program
run()