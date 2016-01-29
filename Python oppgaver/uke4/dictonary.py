

# Create a dictinary
def createDictionary () :
    binary2ascii = {}
    
    # Add binary code, and associate it with ASCII 
    for i in range(0,128) :
        binary2ascii[format(i,'08b')] = chr(i)
    
    # return the dictinary 
    return binary2ascii  
    
    
        
# get binary code from string
def toAscii(binary2ascii, binaryCode) :
    
    setence = "" # The ascii sentence generated
    binaryShortCode = "" # to store the dividing binary code
    
    # Loop trough every number of the binary code, and generate achii char's
    for c in binaryCode :
        
        if  len(binaryShortCode) == 8 :
            setence = setence + binary2ascii[binaryShortCode]
            binaryShortCode = "";
            
        else :
            binaryShortCode = binaryShortCode + c
            
    return setence
        



print toAscii(createDictionary(), '011101000011101000011101000011101000011101000')