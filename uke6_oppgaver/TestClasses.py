import oppgave_1_2_1
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
        
        #run the test
        self.assertEqual(oppgave_1_2_1.run('temp_InputFile.txt', 'temp_OutputFile.txt'), '7210112144321061011033210410111610111432991041141051151161059711032451321343214032504932971411111351071111091681571021149732107145147149110115150100321281301541351371391411431761481501521861561411591611631651671691411711731751461931791811841311331871381571912091781952151971581601623216417420310917017217419217818011010021319618821814422019415322315719922722916616823220523420817715023824012921415524319024526015124815525022620123025523320723626121226424221726828127119627420022820227825728024621123924122326714226921022227319827529327720432206235298262301266286304288307135291252294313315259210318284302321219270324224251276254329258288333185335189322298339326342231279316270347265216350337306272325309292253356296358332283348320363305221366340310370295314345317375361136336379247290368327312256386297359389285378323381354311343399330346403349244406395225369328411387402300334377416352407396355385412388425376362428338430419397410357331237414427287429418341409371400373447436390303364380452383421445413239')        
        
        # print sizes
        print "Filesize input: " + str(os.path.getsize('temp_InputFile.txt'))
        print "Filesize output: " + str(os.path.getsize('temp_OutputFile.txt'))
        
        # Check if the output file  is less than the input file
        self.assertLessEqual(os.path.getsize('temp_OutputFile.txt'), os.path.getsize('temp_InputFile.txt'),)
        
        # remove test files
        os.remove('temp_InputFile.txt')
        os.remove('temp_OutputFile.txt')