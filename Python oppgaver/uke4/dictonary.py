

# Create a dictinary
def createDictionary () :
    binary2ascii = {}
    
    for i in range(0,128) :
        binary2ascii[format(i,'08b')] = chr(i)
        
    toAscii(binary2ascii, '011101000011101000011101000011101000011101000')
    
        
# get binary code from string
def toAscii(binary2ascii, binaryCode) :
    
    print binaryCode 
    i = 0
    setence = ""
    binaryShortCode = ""
    for c in binaryCode :
        if (i == 8) :
            i = 0
            setence = setence + binary2ascii[binaryShortCode]
            binaryShortCode = "";
            
        else :
            binaryShortCode = binaryShortCode + c
            print binaryShortCode
            i = i + 1
    
    
    print setence
        

createDictionary()