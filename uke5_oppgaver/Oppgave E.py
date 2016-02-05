# -*- coding: utf-8 -*-

import sys


#Denne algoritmen skal oversette bokstavene a,b,c,d,e og f til den binære koden som er basert på et hoffman tre.
#Den skal også kunne oversette binære koder tilbake til bokstaver som representerer de forskjellige fakultetene.

#



# Dictionary with the codeword translations of the different variables
codeWordsToBinary = {'A': '00', 'B': '01', 'C': '100', 'D': '101', 'E': '110', 'F': '111'}
binaryToCodeWords = {'00': 'A', '01': 'B', '100': 'C', '101': 'D', '110': 'E', '111': 'F'}



# Gets user input (A-F) and translates it into it's binary counter part
def getBinaryCode() :
       
    stringToBinary = ''
    
    userInput = raw_input('Skriv inn bokstaver mellom A til F: ')
    userInput = userInput.upper()
    
    for key in userInput:
        stringToBinary = stringToBinary + codeWordsToBinary[key]
        
    print stringToBinary
        

# Gets use input (0 and 1) and translates it into it's letter counter part
def getWordsFromBinary() :
    
    binaryToString = ''
    chunk =  ''
    
    userInput = raw_input('Skriv inn tall mellom 0 og 1: ')
    
    for key in userInput:
        
        chunk = chunk + key
        if binaryToCodeWords.has_key(chunk):
            binaryToString = binaryToString + binaryToCodeWords[chunk]
            chunk = ""
    print binaryToString

# Starts the program, and runs the chosen method dependong on user input
def startProgram() :
    
    
    print '-' * 10, 'Binært til bokstaver og bokstaver til binært', '-' * 10
    userInput = raw_input('Skriv inn 1 for binary til bokstaver og 2 for motsatt og 3 for å avslutte: ')
    
    if userInput == '1':
        getBinaryCode()
        
    elif userInput == '2':
        getWordsFromBinary()
    elif userInput == '3':
        sys.exit()
    else:
        startProgram()
        
        

startProgram()