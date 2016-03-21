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

    def delete_file(self, filename):
        '''
        Delete blocks where filename
        :param filename: The filename of the file you wish to delete
        :return: True if the file was deleted, False if the file was not deleted or was found.
        '''
        file_deleted = 0
        file = self.file_space[self.ON_POSITION]
        blocks = []

        for i in file['has_blocks']:                # for each block inside the directory
            blocks.append(i)                        # add block to que list

        for i in blocks:                                                        # for each block in que
            block = self.file_space[i]                                          # set the block value
            if not block['is_dir']:                                             # if the block is not a directory
                if block['filename'] in filename:                               # if the filename match with block file
                    total_blocks = block['blocks_used']                         # how many chunks the file have used
                    self.file_space[i]['available'] = True                      # delete the file
                    self.file_space[self.ON_POSITION]['has_blocks'].remove(i)   # remove it from directory blocks
                    file_deleted += 1                                           # count the deleted file
                    if total_blocks < file_deleted:                             # if all the files are deleted
                        print 'file deleted: ' + str(file_deleted) + ' bytes'   # print out how much that was deleted
                        break                                                   # break the loop.

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
                    self.file_space[self.ON_POSITION]['has_blocks'].remove(i)   # Remove block from the mother dir
                    deleteList = block['has_blocks']                    # Create a delete list for every file inside dir
                    self.clean_block(i)                                 # Clean the block, so we can write to it
                    self.del_block(deleteList)                          # delete files inside the previous div
                    break

    def del_block(self, deleteList):
        for i in deleteList:                                            # For every block inside the dellist
            if not self.file_space[i]['is_dir']:                        # if not it is another directory
                self.file_space[i]['available'] = True                # set so we're able to write over the block again
            else:
                # if there is another directory, we need to fill up our deletelist once again
                deleteList.append(self.file_space[i]['blocks_used'])    # get the blocks from the directory
                self.clean_block(i)                                     # delete the directory.

    def clean_block(self, index):
        '''
        This will set the block to 'normal' state, that means that the program can write to it without haveing problems.
        :param index: the index of the directory block.
        '''
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

    def go_inside_directory(self, name):
        '''
        Go inside the directory of choice, by looking at the directory name.
        :param name: name of the directory you wish to enter.
        :return:
        '''
        name += '/'
        if self.dirname_exist(name) :
            return False

        for i in self.file_space[self.ON_POSITION]['has_blocks']:                       # for each block in the dir
            if self.file_space[i]['is_dir']:                                            # if dir
                if self.file_space[i]['DirectoryName'] == name:                         # if dir name == name
                    self.ON_POSITION = i                                                # set the pos to the dir
                    print 'moved into directory: '+self.file_space[i]['DirectoryName']  # print out status msg.
                    break                                                               # break out of loop

    def go_outside_directory(self):
        '''
            go out of the directory by looking at the head_dir of that position you're at.
        '''
        self.ON_POSITION = self.file_space[self.ON_POSITION]['head_dir']

    def rename_file(self, file_name, newName):
        if self.filename_exist(newName):                  # check if there is a file with that name already.
            return False
        blocks_renamed = 0
        for i in self.file_space[self.ON_POSITION]['has_blocks']:                      # for each block inside directory
            if not self.file_space[i]['is_dir']:                                       # and is not a directory
                if self.file_space[i]['filename'] == file_name:                        # if filename == file_name
                    self.file_space[i]['filename'] = newName                           # change name
                    blocks_to_rename = self.file_space[i]['blocks_used']
                    blocks_renamed += 1

                #if blocks_renamed == blocks_to_rename:
                    #break

    def rename_dir(self, dir_name, new_dir_name):
        if self.dirname_exist(new_dir_name):
            return False
        for i in self.file_space[self.ON_POSITION]['has_blocks']:                      # for each block inside directory
            if self.file_space[i]['is_dir']:                                           # if block is a directory
                if self.file_space[i]['DirectoryName'] == dir_name :                   # if directory nmae == dir_name
                    self.file_space[i]['DirectoryName'] = new_dir_name                 # set new dirname
                    break                                                              # break loop.

    def filename_exist(self, filename):
        '''
        Check if the filename already exist
        :param filename: filename you want to check
        :return: return true if the file exist, and false if not.
        '''
        for i in self.file_space[self.ON_POSITION]['has_blocks']:           # for each block in directory
            if not self.file_space[i]['is_dir']:                            # if block is not a directory
                if self.file_space[i]['filename'] == filename:              # if filename is equals with our filename
                    return True                                             # -> return true
        return False                                                        # no filename was equal our filename.

    def dirname_exist(self, dirname):
        '''
        Check if the dirname already exist
        :param dirname: dirname you want to check
        :return: return true if the dir exist, and false if not.
        '''
        for i in self.file_space[self.ON_POSITION]['has_blocks']:           # for each block in directory
            if self.file_space[i]['is_dir']:                                # if block is  a directory
                if self.file_space[i]['DirectoryName'] == dirname:               # if dir is equals with our dirname
                    return True                                             # -> return true
        return False                                                        # no dirname was equal our dirname.

    def move_file(self, filename, new_destination):
        pass

