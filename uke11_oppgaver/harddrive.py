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
        self.ON_POSITION = 0                             # index of the map block
        self.create_dir('C:/')                            # Create root.

    def add(self, filename, content, localisation):
        '''
        Add a file to our SSD disk
        :param filename: The name of the file
        :param content: What the file includes
        :param localisation: Where to save the file
        :return: True if the file was saved into the SSD, false if there was not any room for it.
        '''
        self.get_available_block()                                   # fills the AVAILABLE_BLOCKS list free index's
        size = len(content) / self.SPACE_EACH_BLOCK                  # find out the input block number
        blocks_free = self.AVAILABLE_BLOCKS                          # find out how much free blocks left

        if size <= blocks_free:                                      # check if there is enough free blocks to write
            block_content = ""                                       # string to hold the bits while added
            chunk = 0                                                # sector related blocks together

            for bit in content:                                      # for each bit in content
                if len(block_content) < self.SPACE_EACH_BLOCK:       # block_content is less than 8
                    block_content += bit                             # add to block_content
                else:
                    chunk += 1
                    self.write(0, filename, block_content, chunk, localisation, size)  # Write to block
                    block_content = bit                              # reset block_content

            chunk += 1
            self.write(0, filename, block_content, chunk, localisation, size)         # add the last block.
        else:
            print "Ikke nok ledig plass til å skrive inn dette."

    def create_empty_blocks(self):
        self.file_space = []                                        # reset filespace
        for i in range(0, self.TOTAL_BLOCK_SPACE):                  # create x slots to save bits
            self.add_block("", "", "", True, 0)                     # -> set 'em as empty and available

    def get_available_block(self):
        '''
        Go trough every block, and add every available block index to a seperat list to write on.
        :return:
        '''
        count = 0
        self.AVAILABLE_BLOCKS = []                       # clear the available list
        for block in self.file_space:                    # for each block space
            if block['available'] is True:               # if the block space is available
                self.AVAILABLE_BLOCKS.append(count)      # add index to our available list

            count += 1                                   # to know what address the loop is at

    def delete_file(self, filename, localisation):
        '''
        Delete blocks where filename and localisation is the same.
        :param filename: The filename of the file you wish to delete
        :param localisation: the localisation of the file you wish to delete
        :return: True if the file was deleted, False if the file was not deleted or was found.
        '''
        deleted_blocks = 0
        blocks_used = ""
        for block in self.file_space:                           # Go trough every block inside the file_space

            if block['filename'] == filename and \
                    block['localisation'] == localisation:      # if filename and localisation match
                        block['available'] = True               # set the portion to true as at this can be overwritten
                        if blocks_used is "":
                            blocks_used = block['blocks_used']  # so we know how many blocks we need to delete
                        deleted_blocks += 1

            if blocks_used is deleted_blocks:                   # if all the files are deleted, break the loop
                print 'deleted ' + str(deleted_blocks) + ' blocks of data'
                break

    def add_block(self, filename, block_content, chunk, available, size):
        self.file_space.append({                                    # add to our space
            'filename': filename,                                   # filename for file
            'content': block_content,                               # block_content
            'chunk': chunk,                                         # what version of the file it is.
            'localisation': "",                                     # where the file is 'located'
            'available': available,                                 # if other files can overwrite
            'blocks_used': size,                                    # the amount of blocks needed to write file
            'is_dir': False,                                        # if the chuck is a directory.
            'head_dir': 0                                           # set it to root directory.
            }
        )

    def open_directory(self):
        '''
        This function will display the content of the map the user is at
        '''
        print 'I mappen: ' + self.file_space[self.ON_POSITION]['DirectoryName']

        for i in self.file_space[self.ON_POSITION]['has_blocks']:  # For every chunk the dir is in charge of
            print self.file_space[i]                               # print out every information it has.

    def open_file(self, filename):
        '''
        Open file by filename
        :param filename: name of the file you want to open
        :return: Content of the selected file | None if there was no file named that.
        '''
        file = self.file_space[self.ON_POSITION]
        file_content = []                                               # to hold the content from the file
        for i in file['has_blocks']:                                    # for each block in current directory
            if not self.file_space[i]['is_dir']:                            # if the chunk is a file.
                if filename in self.file_space[i]['filename']:              # if filename match the file we're looking for
                    x = self.file_space[i]['chunk'] - 1                     # get the chunk
                    file_content.insert(x, self.file_space[i]['content'])   # add the chunktogheter

        if len(file_content) > 0:                                       # if we have gotten data
            return ''.join(file_content)                                # -> Return the data
        else:
            return None                                                 # if we've not any data, return nothing.

    def write(self, index, filename, content, chunk, localisation, size):
        '''
        Write to first available block
        :param index: select 0 for taking the first block
        :param filename: the filename of the file that are to be saved
        :param content: content of the file
        :param chunk: what chunk of the content it is.
        :param localisation: the tree for where the file are to be saved.
        :return:
        '''
        self.file_space[self.AVAILABLE_BLOCKS[index]]['filename'] = filename
        self.file_space[self.AVAILABLE_BLOCKS[index]]['content'] = content
        self.file_space[self.AVAILABLE_BLOCKS[index]]['chunk'] = chunk
        self.file_space[self.AVAILABLE_BLOCKS[index]]['localisation'] = self.FILE_SPACE_ROOT + localisation
        self.file_space[self.AVAILABLE_BLOCKS[index]]['available'] = False
        self.file_space[self.AVAILABLE_BLOCKS[index]]['blocks_used'] = size
        self.file_space[self.AVAILABLE_BLOCKS[index]]['is_dir'] = False
        self.file_space[self.AVAILABLE_BLOCKS[index]]['head_dir'] = self.ON_POSITION

        self.file_space[self.ON_POSITION]['has_blocks'].append(self.AVAILABLE_BLOCKS[index])

        # Pop out the first list item of the available blocks as it is not available anymore.
        self.AVAILABLE_BLOCKS.pop(index)

    def create_dir(self, dir_name):
        '''
        Rewrite first available, and make it to a directory.
        :param dir_name:
        :param under_dir:
        :return:

        '''
        index = 0
        self.file_space[self.AVAILABLE_BLOCKS[index]] = {
            'DirectoryName': dir_name+'/',                      # what the direction is beeing called
            'has_blocks': [],                                   # what blocks it is in charge of
            'available': False,                                 # if the block can be written over
            'is_dir': True,                                     # if the chunk is a directory.
            'head_dir': self.ON_POSITION                        # set the head directory
        }

        if self.ON_POSITION != 0 :                              # if there is any directory in charge of this
            self.file_space[self.ON_POSITION]['has_blocks'].append(self.AVAILABLE_BLOCKS[index])    # add it.

        directory_address = self.AVAILABLE_BLOCKS[index]        # save the directory address, so we can move to it
        self.AVAILABLE_BLOCKS.pop(index)                        # remove the free block index from our list
        return directory_address                                # return the directory adress.

    def delete_dir(self, dir_name):
        '''
        Delete a directory, inside the directory the user are. And also delete all the files inside the directory.
        :param dir_name: The directory name
        :return:
        '''
        file = self.file_space[self.ON_POSITION]
        file_content = []                                               # to hold the content from the file
        for i in file['has_blocks']:                                    # for each block in current directory
            block = self.file_space[i]
            if block['is_dir']:                                         # if it is a directory
                if block['DirectoryName'] in dir_name:                  # if the directory name match with dir_name.
                    self.file_space[self.ON_POSITION]['has_blocks'].remove(i)
                    deleteList = block['has_blocks']
                    self.clean_block(i)
                    self.del_block(deleteList)
                    self.file_space
                    break

    def del_block(self, deleteList):
        for i in deleteList:
            if not self.file_space[i]['is_dir']:
                self.file_space[i]['available'] = True
            else:
                deleteList.append(self.file_space[i]['blocks_used'])
                self.clean_block(i)

    def clean_block(self, index):
        self.file_space[index] = {
            'filename': '',                                         # filename for file
            'content': '',                                          # block_content
            'chunk': '',                                            # what version of the file it is.
            'localisation': "",                                     # where the file is 'located'
            'available': True,                                      # if other files can overwrite
            'blocks_used': '',                                      # the amount of blocks needed to write file
            'is_dir': False,                                        # if the chuck is a directory.
            'head_dir': 0                                           # set it to root directory.
        }

def dirTest():
    disk = SSD()
    disk.open_directory()
    disk.ON_POSITION = disk.create_dir('lol')
    disk.add("test.png",'01001000011001010110110001110000','lol/')

    disk.open_directory()
    disk.ON_POSITION = disk.create_dir('christian_sine_bilder')
    disk.add("christian.png",'01001000011001010110110001110000','lol/christian_sine_bilder/')
    disk.open_file('christian.png')
    disk.open_directory()
    disk.ON_POSITION = 1
    disk.open_directory()
def delete_dir():
    disk = SSD()
    disk.open_directory()
    disk.ON_POSITION = disk.create_dir('test')
    disk.open_directory()
    disk.ON_POSITION = disk.create_dir('yoo')
    disk.add('fileName', '1001010101010101001010101010', '/')
    disk.open_directory()
    disk.ON_POSITION -= 1
    disk.add('mongo.png', '1001010101010101001010101010', '/')
    disk.open_directory()
    disk.delete_dir('yoo/')
    disk.open_directory()
delete_dir()