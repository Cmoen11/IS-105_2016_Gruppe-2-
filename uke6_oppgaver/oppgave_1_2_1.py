# -*- coding: utf-8 -*-

code_for_string = []


def code():
    '''
    Implements an initial table for LZW algorithm 
   
    '''
    
    table1 = {}
    # Generere 128 text elementer
    for i in range(0,128) :
        table1[i] = chr(i)    
    return table1    

def encode(string, byte, table) :
    '''
    Gå igjennom og se først om den forrige sybomlet + nåværnde symbolet ligger i listen allerede. 
    Om den gjør det. Legg den til i listen og append nøkkelen til code_for_string, som blir da 
    den ferdige komprimerte koden vi får utdelt. 
    '''
    global code_for_string
    symbol = byte
    
    #Sjekk om string + symbol allerede finnes i tabel, om det gjør det, sett string = string + symbol
    if(string + symbol) in table.values():
        string = string + symbol
    else :
        # Legg til key til code for string, for å da få "kodene" for å forme teksten.
        for k,v in table.iteritems():
            if v == string :
                code_for_string.append(k)
                
        # legge en sperre, for hvor den skal starte på nytt igjen i tabellen.        
        if (len(table) >= 4095) :
            table = code()
        
        # legg til string + symbol til tabel    
        table[max(table.keys())+1] = string + symbol
        string = symbol
    
    return {'table':table, 'string':string}

def run(inputFile, outputFile):

    f = open(inputFile, 'r') # Open a file that are beeing compressed.
    outputFile = open(outputFile, 'w') # Open output file. 
    temp_holder = {}
    table = code() #add text-elements to our table.
    byte = "" # String to hold our current byte.
    string = "" # String to hold the last byte, for adding it later to the table
    byte = f.read(1) # read the first byte.
    
    global code_for_string # Call the global code_for_string, so it can be edited.
    
    # First run of the first byte we read earlier.
    if (byte != "") :
        # Encode the first byte
        temp_holder = encode(string, byte, table)
        # add the return values to our local strings.
        string = temp_holder['string']
        table = temp_holder['table']
        
    # Kjør så lenge det er bytes i dokumentet
    while (byte != "") :
        # Hent ut en byte fra dokumentet
        byte = f.read(1)
        # Skriv til dokumentet, så lenge byte ikke er null
        if (byte != "") :
            # Encode the byte
            temp_holder = encode(string, byte, table)
            # Add the return values to the local verables.
            string = temp_holder['string']
            table = temp_holder['table']
    
    # legg til siste 'path' i code_for_string
    for k,v in table.iteritems():
        if v == string :
            # Append key to our output table
            code_for_string.append(k)         
    
    # write code to output file, and strip it for extra chars, like (space,[]).
    outputFile.write(''.join(map(str,code_for_string)))
    

    toString = ''.join(map(str,code_for_string))
    return toString


if __name__ == '__main__':
    run('hamlet2.txt', 'output.txt') 
    

