# -*- coding: utf-8 -*-

class SSD:
    def __init__(self):
        self.file_space = []                                # This will actually be the place to store our data
        self.SPACE_EACH_BLOCK = 8                           # Sets the block limit to 8 bits. (2^3)
        self.TOTAL_BLOCK_SPACE = 32                         # Sets the limit for blocks 32 / 256 bits(2^8)
        self.FILE_SPACE_ROOT = "C://"                       # the filestructer root

    def add(self, filename, content):
        '''
        Add a file to our SSD disk
        :param filename: The name of the file
        :param content: What the file includes
        :return: True if the file was saved into the SSD, false if there was not any room for it.
        '''
        size = len(content) / 8                                      # find out the input block number
        blocks_free = self.TOTAL_BLOCK_SPACE - len(self.file_space)  # find out how much free blocks left

        if size <= blocks_free:                                      # check if there is enough free blocks to write
            block_content = ""                                       # string to hold the bits while added
            version = 0                                              # sector related blocks together

            for bit in content:                                      # for each bit in content
                if len(block_content) < self.SPACE_EACH_BLOCK:       # block_content is less than 8
                    block_content = block_content + bit              # add to block_content
                else:
                    version = version + 1
                    self.add_block(filename, block_content, version)
                    block_content = bit                              # reset block_content

            version = version + 1
            self.add_block(filename, block_content, version)         # add the last block.
            return True
        else:
            print "Ikke nok ledig plass til å skrive inn dette."
            return False

    def add_block(self, filename, block_content, version):
        self.file_space.append({                                    # add to our space
            'filename': filename,                                   # filename for file
            'content': block_content,                               # block_content
            'version': version,                                     # what version of the file it is.
            'localisation' : self.FILE_SPACE_ROOT + '/test/'        # where the file is 'located'
            }
        )

lol = SSD()
lol.add('lol','01001000011001010110110001110000')
print lol.file_space