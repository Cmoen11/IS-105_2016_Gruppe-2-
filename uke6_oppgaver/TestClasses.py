import oppgave_1_2_1 as compress
import unittest
import os
class testEncode(unittest.TestCase):
    code_for_string = []
    # test melding.
    def setUp(self) :

        # Create a test output file
        self.outputFile = open('temp_OutputFile.txt', 'w+')
        self.outputFile.close()

    # Test metoder...
    def testEncodeString(self) :

                # print sizes
        print "Filesize input: " + str(os.path.getsize('hamlet.txt'))
        print "Filesize output: " + str(os.path.getsize('temp_OutputFile.txt'))

        #compress content of temp_inputfile.txt, and add it into temp_outputfile.
        compress.run('hamlet.txt', 'temp_OutputFile.txt')

        # print sizes
        print "Filesize input: " + str(os.path.getsize('hamlet.txt'))
        print "Filesize output: " + str(os.path.getsize('temp_OutputFile.txt'))

        # Check if the output file  is less than the input file
        self.assertLessEqual(os.path.getsize('temp_OutputFile.txt'), os.path.getsize('hamlet.txt'))

        # remove test files
        #os.remove('temp_InputFile.txt')
        os.remove('temp_OutputFile.txt')