# -*- coding: utf-8 -*-
import unittest
import os
import Ica_05
from loremipsum import get_sentences
from random import randint


class TestFile(unittest.TestCase):
    '''
    Check that slow uses longer time than fast search.
    '''
    def setUp(self) :
        needle = " Hello "                                  # The needle that is to be placed randomly inside the file
        self.inputFile = open('temp_InputFile.txt', 'w+')   # Create a test input file
        needle_pos = randint(1, 150)                        # Randomly set the position to the needle from 1,150
        sentences_list = get_sentences(4000)                # Create 4000 placeholder sentences

        pos = 0                                             # To keep track on where to put the needle
        for item in sentences_list:                         # Go trough sentence in the list
            if pos == needle_pos:                           # Check the pos, if pos = needle -> write needle.
                self.inputFile.write(needle)                # Write needle
            else:
                self.inputFile.write(item)                  # Write Sentence
            pos += 1                                        # plus the pos with 1 for each run

        self.inputFile.close()

    def testSlowAndFastEachWord(self):
        print 'test 1: \n'
        each_word = Ica_05.EachWord(                        # Create a object to test from
                'temp_InputFile.txt',                       # the temp file created earlier
                "Hello")                                    # The needle to look for

        self.assertGreaterEqual(                            # Check if the slow test is greater than the fast one
            each_word.run_test_slow(100),                   # Run the slow test 100 times
            each_word.run_test_fast(100))                   # run the fast test 100 times

        print "File size: " + str(os.path.getsize('temp_InputFile.txt'))

        os.remove('temp_InputFile.txt')                     # Delete the temp file 




class testTwoFiles(unittest.TestCase):
    '''
    Check slow search, with two files. One bigger than the other
    '''
    def setUp(self) :
        needle = " Hello "                                  # The needle that is to be placed randomly inside the file

        input_file1 = open('temp_InputFile1.txt', 'w+')  # Create a test input1 file
        input_file2 = open('temp_InputFile2.txt', 'w+')  # Create a test input2 file

        needle_pos = randint(1, 150)                        # Randomly set the position to the needle from 1,150
        sentences_list_1 = get_sentences(4000)              # Create 4000 placeholder sentences
        sentences_list_2 = get_sentences(8000)              # Create 4000 placeholder sentences

        # For the file 1
        pos = 0                                             # To keep track on where to put the needle
        for item in sentences_list_1:                       # Go trough sentence in the list
            if pos == needle_pos:                           # Check the pos, if pos = needle -> write needle.
                input_file1.write(needle)                   # Write needle
            else:
                input_file1.write(item)                     # Write Sentence
            pos += 1                                        # plus the pos with 1 for each run
        input_file1.close()

        # For the file 2
        pos = 0                                             # To keep track on where to put the needle
        for item in sentences_list_2:                       # Go trough sentence in the list
            if pos == needle_pos:                           # Check the pos, if pos = needle -> write needle.
                input_file2.write(needle)                   # Write needle
            else:
                input_file2.write(item)                     # Write Sentence
            pos += 1                                        # plus the pos with 1 for each run
        input_file2.close()

    def test_two_files_words(self):
        print '\n test 2: \n'
        file1 = Ica_05.EachWord(                            # Create a object to test from
            'temp_InputFile1.txt',                          # the temp file created earlier
            "Hello")                                        # The needle to look for

        file2 = Ica_05.EachWord(                            # Create a object to test from
            'temp_InputFile2.txt',                          # the temp file created earlier
            "Hello")

        self.assertLessEqual(                               # Check if the biggest file used longer time.
            file1.run_test_slow(100),                           # Run the slow test 100 times
            file2.run_test_slow(100))                           # run the fast test 100 times

        print "File1 size: " + str(os.path.getsize('temp_InputFile1.txt'))
        print "File2 size: " + str(os.path.getsize('temp_InputFile2.txt'))

        os.remove('temp_InputFile1.txt')                    # Delete the temp1 file
        os.remove('temp_InputFile2.txt')                    # Delete the temp2 file
