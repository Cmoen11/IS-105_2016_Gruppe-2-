
binary2ascii = {}


for i in range(0,128) :
    
    binary2ascii[format(i,'08b')] = chr(i)









 print binary2ascii[format(56, '08b')] 