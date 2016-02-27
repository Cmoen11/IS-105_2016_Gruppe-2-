import Search
# -*- coding: utf-8 -*-

'''
This python document include two classes, one is for checking each symbol in a file, and another one for checking each
word in the selected file.

To call each class, you need to give it a number on how many test i

'''


class EachLetter(Search.Search):

    def __init__(self, filename, needle):
        self.needle = needle                                    # the word we're looking for
        self.fileName = filename                                # The file we're searching trough
        input_file = open(self.fileName, 'r')                   # Open file
        self.prepare = input_file.read()                        # read file
        input_file.close()                                      # close file
        pass


class EachWord (Search.Search):
    def __init__(self, filename, needle):
        self.needle = needle                                    # the word we're looking for
        self.fileName = filename                                # The file we're searching trough
        input_file = open(self.fileName, 'r')                   # Open file
        self.prepare = input_file.read().split()                # read file and split each word
        input_file.close()                                      # close file
        pass


# For each word
def run():
    print("For hvert ord")
    each_words = EachWord('shakespare.txt', 'The')
    each_words.run_test(10)
    print
    print("For hver bokstav(byte)")

    # For each letter
    each_letters = EachLetter('shakespare.txt', 'T')
    each_letters.run_test(1)

if __name__ == '__main__':
    run()
