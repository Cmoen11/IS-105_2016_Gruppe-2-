binary2ascii = {}

# Create a dictinary
def createDictionary () :
    global binary2ascii
    for i in range(0,128) :
        binary2ascii[format(i,'08b')] = chr(i)

        
# get binary code from string        
def toBinary(text) :
    global binary2ascii
    for c in text :
        print binary2ascii[format('b','08b')]
        
      

    

createDictionary()
toBinary(raw_input("Transform this text to binary: "))