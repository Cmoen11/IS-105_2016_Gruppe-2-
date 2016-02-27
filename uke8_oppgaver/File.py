from loremipsum import get_sentences
import os


class CreateFile:

    def __init__(self, sentences, needle, pos, filename):
        self.needle = " " + needle + " "                           # needle, so the program has something to look for
        self.pos = pos                                             # where the needle is going to be placed
        self.filename = filename
        self.sentences = sentences

        # Create file
        self.sentences_list = self.generate_sentences()             # Generate the sentences
        self.temp_file = self.create_temp_file()                    # Create temp file
        self.write_to_file()                                        # Write the sentences to file

    def create_temp_file(self):
        return open(self.filename, 'w+')                    # Create file with the selected filename

    def generate_sentences(self):
        return get_sentences(self.sentences)                # Create x placeholder sentences

    def write_to_file(self):
        pos = 0                                             # To keep track on where to put the needle
        for item in self.sentences_list:                    # Go trough sentence in the list
            if pos == self.pos:                             # Check the pos, if pos = needle -> write needle.
                self.temp_file.write(self.needle)           # Write needle
            else:
                self.temp_file.write(item)                  # Write Sentence
            pos += 1

    def close_file(self):
        self.temp_file.close()                              # Close file

    def get_file(self):
        return self.temp_file                               # return file

    def get_filename(self):
        return self.filename                                # return filename

    def get_filesize(self):
        return os.path.getsize('temp_InputFile.txt')        # get size of the file

    def delete_file(self):
        os.remove(self.get_filename())
