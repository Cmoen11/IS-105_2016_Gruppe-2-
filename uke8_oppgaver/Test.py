# -*- coding: utf-8 -*-
import unittest
import Ica_05
import File


class TestFile(unittest.TestCase):
    '''
    Check that slow uses longer time than fast search.
    '''
    def setUp(self) :

        # Generate a File
        self.gen_file = File.CreateFile(
            200,                                  # How many symbols that are to be generated and added
            20,                                   # Where the needle is to be added(can't be higher than sentences)
            "temp_InputFile.txt")                 # The filename
        self.gen_file.close_file()                # close file.

    def testSlowAndFastEachLetter(self):
        print ('test 1 (Denne sjekker om fast er raskere enn slow): \n')
        each_word = Ica_05.EachLetter(                      # Create a object to test from
                'temp_InputFile.txt',                       # the temp file created earlier
                "1")                                        # The needle to look for

        self.assertGreaterEqual(                            # Check if the slow test is greater than the fast one
            each_word.run_test_slow(100),                   # Run the slow test 100 times
            each_word.run_test_fast(100))                   # run the fast test 100 times

        print "File size: " + str(self.gen_file.get_filesize())

        # Delete the testfile
        self.gen_file.delete_file()




class testTwoFiles(unittest.TestCase):
    '''
    Check slow search, with two files. One bigger than the other
    '''
    def setUp(self) :
        # Generate a File
        self.gen_file1 = File.CreateFile(
            200,                                  # How many symbols that are to be generated and added
            20,                                   # Where the needle is to be added(can't be higher than sentences)
            "temp_InputFile1.txt")                # The filename
        self.gen_file1.close_file()               # close file.

        self.gen_file2 = File.CreateFile(
            400,                                  # How many sentences that are to be generated and added
            20,                                   # Where the needle is to be added(can't be higher than sentences)
            "temp_InputFile2.txt")                # The filename
        self.gen_file2.close_file()               # close file.

    def test_two_files_words(self):
        print '\ntest 2 (2 filer, der den ene er større enn den andre, her er det kun test_slow som blir kjørt.): \n'
        file1 = Ica_05.EachLetter(                          # Create a object to test from
            'temp_InputFile1.txt',                          # the temp file created earlier
            "1")                                            # The needle to look for

        file2 = Ica_05.EachLetter(                          # Create a object to test from
            'temp_InputFile2.txt',                          # the temp file created earlier
            "1")

        self.assertLessEqual(                               # Check if the biggest file used longer time.
            file1.run_test_slow(100),                       # Run the slow test 100 times
            file2.run_test_slow(100))                       # run the fast test 100 times

        print "File size: " + str(self.gen_file1.get_filesize())
        print "File size: " + str(self.gen_file2.get_filesize())

        self.gen_file1.delete_file()                        # Delete file 1
        self.gen_file2.delete_file()                        # delete file 2


class TestNeedlePlacement(unittest.TestCase):
    '''
    This test function will find out if there will take any longer time if the needle is placed either early in the
    document or late in the document
    '''
    def setUp(self) :

        # Generate file, place needle in the beginning of the file
        self.gen_file1 = File.CreateFile(
            200,                                  # How many symbols that are to be generated and added
            0,                                    # Where the needle is to be added(can't be higher than sentences)
            "temp_InputFile1.txt")                # The filename
        self.gen_file1.close_file()               # close file.


        # Generate a file, place the needle in the end of the file.
        self.gen_file2 = File.CreateFile(
            200,                                  # How many symbols that are to be generated and added
            201,                                  # Where the needle is to be added(can't be higher than sentences)
            "temp_InputFile2.txt")                # The filename
        self.gen_file2.close_file()               # close file.

    def testSlowAndFastEachLetter(self):

        # File 1

        print 'test 1 (Check when the needle is in the very beginning of the document): \n'
        file1 = Ica_05.EachLetter(                              # Create a object to test from
                'temp_InputFile1.txt',                          # the temp file created earlier
                "1")                                            # The needle to look for

        self.assertGreaterEqual(                                # Check if the slow test is greater than the fast one
            file1.run_test_slow(1000),                          # Run the slow test 100 times
            file1.run_test_fast(1000))                          # run the fast test 100 times

        print "File size: " + str(self.gen_file1.get_filesize())


        # File 2
        print '\n test 2 (Check when the needle is in the very last of the document): \n'
        file2 = Ica_05.EachLetter(                              # Create a object to test from
                'temp_InputFile1.txt',                          # the temp file created earlier
                "1")                                            # The needle to look for
        self.assertGreaterEqual(                                # Check if the slow test is greater than the fast one
            file1.run_test_slow(1000),                          # Run the slow test 100 times
            file2.run_test_fast(1000))                          # run the fast test 100 times

        print "File size2: " + str(self.gen_file2.get_filesize())

        # Delete the testfile
        self.gen_file1.delete_file()
        self.gen_file2.delete_file()