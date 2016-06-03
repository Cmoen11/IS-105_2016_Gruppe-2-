import oppgave_1_2_1 as compress
import unittest
import os
class testEncode(unittest.TestCase):
    code_for_string = []
    # test melding.
    def setUp(self) :
        
        # The test text
        self.testText = "Hey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansand Hey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansandHey, jeg heter christian - jeg er 21 ar og kommmer fra kristiansand"
        
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

        #compress content of temp_inputfile.txt, and add it into temp_outputfile.
        compress.run('temp_InputFile.txt', 'temp_OutputFile.txt')

        # print sizes
        print "Filesize input: " + str(os.path.getsize('temp_InputFile.txt'))
        print "Filesize output: " + str(os.path.getsize('temp_OutputFile.txt'))

        # Check if the output file  is less than the input file
        self.assertLessEqual(os.path.getsize('temp_OutputFile.txt'), os.path.getsize('temp_InputFile.txt'),)
        
        # remove test files
        os.remove('temp_InputFile.txt')
        os.remove('temp_OutputFile.txt')

    def