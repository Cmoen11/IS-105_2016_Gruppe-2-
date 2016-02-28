from loremipsum import get_sentences
import os


class CreateFile:

    def __init__(self, symbols, pos, filename):
        self.needle = '1'                                          # needle, so the program has something to look for
        self.pos = pos                                             # where the needle is going to be placed
        self.filename = filename                                   # the name of the file that are to be created.
        self.symbol = symbols                                      # the amount of char's inside the document

        # Create file
        self.temp_file = self.create_temp_file()                    # Create temp file
        self.write_to_file()                                        # Write the characters to file

    def create_temp_file(self):
        return open(self.filename, 'w+')                            # Create file with the selected filename

    def generate_sentences(self):
        return get_sentences(self.symbol)                           # Create x symbols

    def write_to_file(self):
        for i in range(0, self.symbol):                           # run for the amount of symbol's that are requested
            if i == self.pos:                                     # if pos is at the point of needle pos, write 1
                self.temp_file.write(self.needle)                   # write 1
            else:
                self.temp_file.write('0')                           # Write 0

    def close_file(self):
        self.temp_file.close()                              # Close file

    def get_file(self):
        return self.temp_file                               # return file

    def get_filename(self):
        return self.filename                                # return filename

    def get_filesize(self):
        return os.path.getsize(self.filename)        # get size of the file

    def delete_file(self):
        os.remove(self.get_filename())
