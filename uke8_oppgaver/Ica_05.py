import Search
import plotly
from plotly.graph_objs import Scatter, Layout
from plotly.offline import plot
import File





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


class needlePlacement20():
    '''
    Check that slow uses longer time than fast search.
    '''
    def __init__(self):

        # Generate a File
        self.gen_file = File.CreateFile(
            200,                                  # How many symbols that are to be generated and added
            20,                                   # Where the needle is to be added(can't be higher than sentences)
            "temp_InputFile.txt")                 # The filename
        self.gen_file.close_file()                # close file.

    def testSlowAndFastEachLetter(self):
        print ('test 1 (Denne sjekker om fast er raskere enn slow): \n')
        each_letter = EachLetter(                      # Create a object to test from
                'temp_InputFile.txt',                       # the temp file created earlier
                "1")                                        # The needle to look for


        print "File size: " + str(self.gen_file.get_filesize())
        print '______________________________________________________'
        # Delete the testfile
        self.gen_file.delete_file()
        return each_letter

def createBar(fast, slow, title, name):
    plotly.offline.init_notebook_mode() # run at the start of every notebook
    plotly.offline.plot({
    "data" : [
        Scatter(
            x=['Fast', 'Slow'],
            y=[fast, slow]
        )

    ],
    "layout": Layout(title=title),

},
    filename=name+'.html')

def run_NeedlePlacement(needle, total, times, name):
    file = File.CreateFile(
            total,                                # How many symbols that are to be generated and added
            needle,                               # Where the needle is to be added(can't be higher than sentences)
            "temp_InputFile.txt")                 # The filename

    each_letter = EachLetter(                     # Create a object to test from
                'temp_InputFile.txt',             # the temp file created earlier
                "1")                              # The needle to look for

    fast = each_letter.run_test_fast(times)
    slow = each_letter.run_test_slow(times)
    createBar(fast, slow, "For hvert tegn, hvor needle plassering er satt til pos " + str(needle) + " av " + str(total) + " tegn..", name)
    file.close_file()
    file.delete_file()                        # Delete file 1

# For each word
def run():

    # needle placement on pos 1 of 200.
    run_NeedlePlacement(1, 200, 1000, 'test1')

    # needle placement on pos 200 of 200.
    run_NeedlePlacement(200, 200, 200, 'test2')






if __name__ == '__main__':
    run()
