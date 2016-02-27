# -*- coding: utf-8 -*-
import unittest
import os
import Ica_05
from loremipsum import get_sentences
from random import randint


class TestFile(unittest.TestCase):
    def setUp(self) :
        needle = " Hello "                    # The needle that is to be placed randomly inside the file
        # Create a test input file
        self.inputFile = open('temp_InputFile.txt', 'w+')
        needle_pos = randint(1, 150)
        sentences_list = get_sentences(4000)

        pos = 0
        for item in sentences_list:
            if(pos == needle_pos):
                self.inputFile.write(needle)
                print 'added needle'
            else:
                self.inputFile.write(item)

            pos += 1

        self.inputFile.close()

    def testSlowAndFastEachWord(self):
        each_word = Ica_05.EachWord('temp_InputFile.txt', "Hello")
        self.assertGreaterEqual(each_word.run_test_slow(100), each_word.run_test_fast(100))
        print "Filesize: " + str(os.path.getsize('temp_InputFile.txt'))

        os.remove('temp_InputFile.txt')

