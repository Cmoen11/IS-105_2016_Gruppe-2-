# -*- coding: utf-8 -*-
'''
'''

TOTALSPACE = 32         # slik at du totalt kun har 32 blokker
SPACE_EACH_BLOCK = 8    # each block can just hold 8 bits.
FreeBlocks = []
filespace = []

# Hver item av filespace er da en block, i blocken bruker jeg dictionary til meta.


def create_block():
    filespace.append(
        {
            'filename':'',
            'content':'',
            'available': True
        }
    )


def create_hardisk():
    # Oppretter 32 blocker, hver av blokkene har en adresse i index, f.eks 1, 2, 3
    for i in range (0, TOTALSPACE):
        create_block()

def get_free_blocks():
    global FreeBlocks
    FreeBlocks = []                            # tømme innholdet i freeblocks
    count = 0
    for block in filespace:                    # for each block space
        if block['available']:                 # if the block space is available
            FreeBlocks.append(count)
        count += 1

def checkSpace(space):
    if space > len(FreeBlocks):
        return False
    return True

def write_block(filename, content):
    global filespace
    global FreeBlocks
    filespace[FreeBlocks[0]] = {
        'filename': filename,
        'content': content,
        'available': False
    }
    FreeBlocks.pop(0)

def writeFile(filename, content):
    total_blocks = int(content) / SPACE_EACH_BLOCK
    if not checkSpace(total_blocks):
        content_each_block = ""
        for bit in content:                                      # for each bit in content
            if len(content_each_block) < SPACE_EACH_BLOCK:       # block_content is less than 8
                content_each_block += bit                             # add to block_content
            else:
                write_block(filename, content_each_block)
                content_each_block = bit                              # reset block_content

        write_block(filename, content_each_block)

create_hardisk()
get_free_blocks()
writeFile('test', '1001010101010010101010')
for i in filespace:
    print i