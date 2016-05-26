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


def createBar(data1, data2, title, name):
    '''
        Create a barchart that show the performance of slow and fast speed.S
    :param fast:    the time the fast speed tok.
    :param slow:    The time the slow speed tok
    :param title:   The title on the chart.
    :param name:    Name of the file
    '''
    plotly.offline.init_notebook_mode() # run at the start of every notebook
    plotly.offline.plot({
    "data" : [
        Scatter(
            x=['Fast needleplacement pos 50', 'slow needleplacement pos 50', 'fast needleplacement pos 19999', 'slow needleplacement pos 19999'],
            y=[data1['fast'], data1['slow'], data2['fast'], data2['fast']]
        )

    ],
    "layout": Layout(title=title),

},
    filename=name+'.html')

def run_NeedlePlacement(needle, total, times):
    file = File.CreateFile(
            total,                                # How many symbols that are to be generated and added
            needle,                               # Where the needle is to be added(can't be higher than sentences)
            "temp_InputFile.txt")                 # The filename

    each_letter = EachLetter(                     # Create a object to test from
                'temp_InputFile.txt',             # the temp file created earlier
                "1")                              # The needle to look for

    fast = each_letter.run_test_fast(times)
    slow = each_letter.run_test_slow(times)
    file.close_file()
    file.delete_file()                        # Delete file 1

    return {'fast': fast, 'slow':slow}

# For each word
def run():

    # needle placement on pos 1 of 200.
    data1 = run_NeedlePlacement(20, 10000, 1000)

    # needle placement on pos 200 of 200.
    data2 = run_NeedlePlacement(19999, 10000, 1000)

    createBar(data1, data2, 'going through 10000 symbols', 'test1')




if __name__ == '__main__':
    run()
