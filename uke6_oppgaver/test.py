import lzw
lzw.readbytes("hamlet.txt", buffersize=1024)
enc = lzw.compress(file)
print enc