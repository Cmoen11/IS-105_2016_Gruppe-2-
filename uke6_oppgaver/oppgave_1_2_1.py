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

def compress(uncompressed):
    dictionary = {chr(i):i for i in range(97,123)}

    last = 256
    p = ""
    result = []

    for c in uncompressed:                  # for each byte in string
        pc = p+c                            # add it togehter
        if pc in dictionary:                # if string is inside of the dicinoary already
            p = pc                          # set p to be pc.
        else:                               # if not, add it to our dic
            result.append(dictionary[p])    # -> adding it.
            dictionary[pc] = last           # set the dic position
            last += 1                       # ++ last, for next iteration
            p = c                           # set p to C.

    # if there is more in memory, append the last one.
    if p != '':
        result.append(dictionary[p])

    # return the result
    return result


def compressFile(inputFile, outputFile):
    f = open(inputFile, 'r')                            # Open a file that are beeing compressed.
    outputFile = open(outputFile, 'w')                  # Open output file.
    file = f.read()
    outputFile.write(str(compress(file)).strip("[]'"))





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
        if (len(table) >= 4000) :
            print table
            table = code()
            code_for_string = []
        
        # legg til string + symbol til tabel    
        table[max(table.keys())+1] = string + symbol
        string = symbol
    
    return {'table':table, 'string':string}

def run(inputFile, outputFile):
    global code_for_string
    f = open(inputFile, 'r')                            # Open a file that are beeing compressed.
    outputFile = open(outputFile, 'w')                  # Open output file.
    temp_holder = {}
    table = code()                                      #add text-elements to our table.
    byte = ""                                           # String to hold our current byte.
    string = ""                                         # String to hold the last byte, for adding it later to the table
    file = f.read()
    byte = file[0]                                      # read the first byte.

    global code_for_string                              # Call the global code_for_string, so it can be edited.

    # First run of the first byte we read earlier.
    if (byte != "") :
        # Encode the first byte
        temp_holder = encode(string, byte, table)
        # add the return values to our local strings.
        string = temp_holder['string']
        table = temp_holder['table']

    # Kjør så lenge det er bytes i dokumentet
    for i in range (len(file)):

        byte = file[i]

        if (byte != "") :                               # Skriv til dokumentet, så lenge byte ikke er null
            temp_holder = encode(string, byte, table)   # Encode the byte

            string = temp_holder['string']              # Add the return values to the local verables.
            table = temp_holder['table']

    # legg til siste 'path' i code_for_string
    for k,v in table.iteritems():
        if v == string :
            # Append key to our output table
            code_for_string.append(k)

    # write code to output file, and strip it for extra chars, like (space,[]).
    outputFile.write(str(''.join(map(str,code_for_string))))


    toString = ''.join(map(str,code_for_string))
    return toString


if __name__ == '__main__':
    run('hamlet.txt', 'output.txt')
    

