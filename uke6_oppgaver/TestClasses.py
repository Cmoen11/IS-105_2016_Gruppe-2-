import oppgave_1_2_1
import unittest
import os
class testEncode(unittest.TestCase):
    code_for_string = []
    # test melding.
    def setUp(self) :
        
        # The test text
        self.testText = "testTekst"
        
        # Create a test input file
        self.inputFile = open('temp_InputFile.txt', 'w+')
        
        # write to input testfile
        self.inputFile.write(self.testText)
        self.inputFile.close()
        
        # Create a test output file
        self.outputFile = open('temp_OutputFile.txt', 'w+')    
        self.outputFile.close()
    
    # Test metoder...
    def testEncodeString(self) :
        
        #run the test
        self.assertEqual(oppgave_1_2_1.run('temp_InputFile.txt', 'temp_OutputFile.txt'), '11610111511684101107130')
        
        # print sizes
        print "Filesize input: " + str(os.path.getsize('temp_InputFile.txt'))
        print "Filesize output: " + str(os.path.getsize('temp_OutputFile.txt'))
        
        # remove test files
        os.remove('temp_InputFile.txt')
        os.remove('temp_OutputFile.txt')