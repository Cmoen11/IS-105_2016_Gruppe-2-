# -*- coding: utf-8 -*-

def code():
    '''
    Implements an initial table for LZW algorithm 
   
    '''
    
    table1 = {}
    # Generere 128 text elementer
    for i in range(0,128) :
        table1[i] = chr(i)    
    return table1    
def encode(message):
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
            # Gå igjennom dictinary og og sjekk om value == String, om dette er riktig, append key til code_for_String
            for k,v in table.iteritems():
                if v == string:
                    code_for_string.append(k)
                    
            # legg til string + symbol til tabel
            table[max(table.keys())+1] = string + symbol
            string = symbol
            
    # Gå igjennom listen og og sjekk om value == String, om dette er riktig, append key til code_for_String        
    for k,v in table.iteritems():
        if v == string:
            code_for_string.append(k)
    
    print len(table)        
    print table
    return code_for_string
    
    

def test():
    sourcecode = "D:\is-110\IS-105_2016_Gruppe-2-\uke6_oppgaver\hamlet.txt"
    f = open(sourcecode, mode='rb') # Open a file with filename <sourcecode>
    
    test_message = f.read(2000)
    i = 0
    encode(test_message)
    
test()