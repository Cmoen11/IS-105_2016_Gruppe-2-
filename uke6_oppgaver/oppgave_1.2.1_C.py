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
def encode(code_for_string, message):
    table = code()
    
    string = "" 
    code_for_string = []
    
    # Gå igjennom hver eneste bokstav i message og sjekk om symbol + String finnes i listen
    for byte in message:
        symbol = byte
        
        #Sjekk om string + symbol allerede finnes i tabel, om det gjør det, sett string = string + symbol
        if (string + symbol) in table.values():
            string = string + symbol
        
        else:
            # Legg til key til code for string, for å da få "kodene" for å forme teksten.
            for k,v in table.iteritems():
                if v == string:
                    code_for_string.append(k)
                    
            # legg til string + symbol til tabel
            table[max(table.keys())+1] = string + symbol
            string = symbol
            
    # Legg til key til code for string, for å da få "kodene" for å forme teksten.
    for k,v in table.iteritems():
        if v == string:
            code_for_string.append(k)
    
    #print len(table)        
    #return table
    #return code_for_string
    
    

def writeTo(string, byte, table) :
    '''
    Gå igjennom og se først om den forrige sybomlet + nåværnde symbolet ligger i listen allerede. 
    Om den gjør det. Legg den til i listen og append nøkkelen til code_for_string, som blir da 
    den ferdige komprimerte koden vi får utdelt. 
    
    '''
    global code_for_string
    symbol = byte
    
    if(string + symbol) in table.values():
        string = string + symbol
    else :
        for k,v in table.iteritems():
            if v == string :
                code_for_string.append(k)
                print code_for_string
        # legge til i tabel
        table[max(table.keys())+1] = string + symbol
        string = symbol
    
    return {'table':table, 'string':string}

def run():
    sourcecode = "D:\is-110\IS-105_2016_Gruppe-2-\uke6_oppgaver\hamlet.txt"
    f = open(sourcecode, 'r') # Open a file with filename <sourcecode>
    temp_dick = {}
    table = code()
    byte = ""
    string = ""
    antallByte = 0
    byte = f.read(1)
    print byte
    global code_for_string
    
    if (byte != "") :
        temp_dick = writeTo(string, byte, table)
        string = temp_dick['string']
        table = temp_dick['table']
        print string
        print table
    # Kjør så lenge det er bytes i dokumentet
    while (byte != "") :
        # Hent ut en byte fra dokumentet
        byte = f.read(1)
        antallByte +=1
        print byte
        # Skriv til dokumentet, så lenge byte ikke er null
        if (byte != "") :
            temp_dick = writeTo(string, byte, table)
            string = temp_dick['string']
            table = temp_dick['table']
    
    # legg til siste 'path' i code_for_string
    for k,v in table.iteritems():
        if v == string :
            code_for_string.append(k)         
         
    print code_for_string       
    
run()