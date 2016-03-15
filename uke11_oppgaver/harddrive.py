# -*- coding: utf-8 -*-


class SSD:
    def __init__(self):
        self.file_space = []                             # This will actually be the place to store our data
        self.SPACE_EACH_BLOCK = 8                        # Sets the block limit to 8 bits. (2^3)
        self.TOTAL_BLOCK_SPACE = 32                      # Sets the limit for blocks 32 / 256 bits(2^8)
        self.FILE_SPACE_ROOT = "C:/"                     # the filestructer root
        self.AVAILABLE_BLOCKS = []

        self.create_empty_blocks()                       # Set up potions
        self.get_available_block()                       # fills the AVAILABLE_BLOCKS list with index's of free potions


    def add(self, filename, content, localisation):
        '''
        Add a file to our SSD disk
        :param filename: The name of the file
        :param content: What the file includes
        :return: True if the file was saved into the SSD, false if there was not any room for it.
        '''
        self.get_available_block()                                   #  fills the AVAILABLE_BLOCKS list free index's
        size = len(content) / 8                                      # find out the input block number
        blocks_free = self.AVAILABLE_BLOCKS                          # find out how much free blocks left

        if size <= blocks_free:                                      # check if there is enough free blocks to write
            block_content = ""                                       # string to hold the bits while added
            version = 0                                              # sector related blocks together

            for bit in content:                                      # for each bit in content
                if len(block_content) < self.SPACE_EACH_BLOCK:       # block_content is less than 8
                    block_content = block_content + bit              # add to block_content
                else:
                    version = version + 1
                    self.write(0, filename, block_content, version, localisation)  # Write to block
                    block_content = bit                              # reset block_content

            version = version + 1
            self.write(0, filename, block_content, version, localisation)         # add the last block.
        else:
            print "Ikke nok ledig plass til å skrive inn dette."



    def create_empty_blocks(self):
        self.file_space = []                                        # reset filespace
        for i in range(0, self.TOTAL_BLOCK_SPACE):                  # create x slots to save bits
            self.add_block("", "", "", True)                        # -> set 'em as empty and available

    def get_available_block(self):
        '''
        Go trough every block, and add every available block index to a seperat list to write on.
        :return:
        '''
        count = 0
        self.AVAILABLE_BLOCKS = []
        for block in self.file_space:
            if block['available'] is True:
                self.AVAILABLE_BLOCKS.append(count)      # add index to our available list


            count = count + 1



    def deleteFile(self, filename, localisation):
        '''
        Delete blocks where filename and localisation is the same.
        :param filename: The filename of the file you wish to delete
        :param localisation: the localisation of the file you wish to delete
        :return: True if the file was deleted, False if the file was not deleted or was found.
        '''
        for block in self.file_space:                               # Go trough every block inside the file_space

            if block['filename'] == filename and \
                    block['localisation'] == localisation:      # if filename and localisation match
                        block['available'] = True               # set the portion to true as at this can be overwritten

    def add_block(self, filename, block_content, version, available):
        self.file_space.append({                                    # add to our space
            'filename': filename,                                   # filename for file
            'content': block_content,                               # block_content
            'version': version,                                     # what version of the file it is.
            'localisation': "",                                     # where the file is 'located'
            'available': available                                  # if other files can overwrite
            }
        )

    def write(self, index, filename, content, version, localisation):

        self.file_space[self.AVAILABLE_BLOCKS[index]]['filename'] = filename
        self.file_space[self.AVAILABLE_BLOCKS[index]]['content'] = content
        self.file_space[self.AVAILABLE_BLOCKS[index]]['version'] = version
        self.file_space[self.AVAILABLE_BLOCKS[index]]['localisation'] = self.FILE_SPACE_ROOT + localisation
        self.file_space[self.AVAILABLE_BLOCKS[index]]['available'] = False
        self.AVAILABLE_BLOCKS.pop(index)




lol = SSD()
lol.add('erlends_nude_pic.png', '01001000011001010110110001110000','test/')
lol.add('tommy_nude_pic.png', '01001000011001010110110001110000','test/')
lol.deleteFile('erlends_nude_pic.png', 'C:/test/')
lol.add('Christian_nude_pic.png', '01001000011001010110110001110000','test/')
for block in lol.file_space :
        print block