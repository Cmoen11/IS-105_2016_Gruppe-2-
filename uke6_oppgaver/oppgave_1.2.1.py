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

def run():
    sourcecode = "hamlet.txt"
    sourcecode2 = "output.txt"
    f = open(sourcecode, 'r') # Open a file with filename <sourcecode>
    kuk = open(sourcecode2, 'w') # Open a file with filename <sourcecode>
    temp_holder = {}
    table = code()
    byte = ""
    string = ""
    #antallByte = 0
    byte = f.read(1)
    print len(byte)
    global code_for_string
    
    #print encode(byte)
    
    
    if (byte != "") :
        temp_holder = encode(string, byte, table)
        string = temp_holder['string']
        table = temp_holder['table']
        print table
    # Kjør så lenge det er bytes i dokumentet
    while (byte != "") :
        # Hent ut en byte fra dokumentet
        byte = f.read(1)
        # Skriv til dokumentet, så lenge byte ikke er null
        if (byte != "") :
            temp_holder = encode(string, byte, table)
            string = temp_holder['string']
            table = temp_holder['table']
    
    # legg til siste 'path' i code_for_string
    for k,v in table.iteritems():
        if v == string :
            code_for_string.append(k)         
    
    
    print table
    kuk.write(', '.join(map(str,code_for_string)))    
    
run()