import timeit

# This goes trough every letter of the selected file 
class eachLetter :
    def __init__ (self):
        self.needle = 'T'
        self.fileName = "shakespare.txt"
        self.prepare = open(self.fileName, 'r').read()
    
    # Go trough every letter, and look for match, return True back when match is found
    def search_fast(self):
        for item in self.prepare:
            if item == self.needle:
                return True
        return False
    
    # Go trough every letter, look for match, set Return_value to true and return after running trough every letter
    def search_slow(self):
        return_value = False
        for item in self.prepare:
            if item == self.needle:
                return_value = True
        return return_value
    
    # Run test and print out time taken for running the tests
    def runTest(self) :
            n = 1 # time how long n action's take
            benchmark = timeit.Timer(self.search_slow)
            print ("Search-slow :", benchmark.timeit(n), "seconds to go trough " + str(n) + " times")
            
            benchmark = timeit.Timer(self.search_fast)
            print ("Search-fast :", benchmark.timeit(n), "seconds to go trough " + str(n) + " times")

# this goes through every word in the selected file
class eachWord :
    def __init__ (self):
        self.needle = 'The'
        self.fileName = "shakespare.txt"
        self.prepare = open(self.fileName, 'r').read()
        
    # Go trough every word, and look if they match, return True back when match is found
    def search_fast(self):
        self.words = self.prepare.split()
        for word in self.words :
            if word == self.needle :
                return True
        return False
    
    # Go trough every word, and look if they match, set Return_value to true and return after running trough every word
    def search_slow(self):
        return_value = False
        self.words = self.prepare.split()
        for word in self.words:
            if word == self.needle:
                return_value = True
        return return_value
    
    # Run test and print out time taken for running the tests
    def runTest(self) :
        n = 1000 # time how long n action's take
        benchmark = timeit.Timer(self.search_slow)
        print ("Search-slow :", benchmark.timeit(n), "seconds to go trough " + str(n) + " times")
        
        benchmark = timeit.Timer(self.search_fast)
        print ("Search-fast :", benchmark.timeit(n), "seconds to go trough " + str(n) + " times")    



# For each word
print ("For hvert ord")
eachWords = eachWord()
eachWords.runTest()

print ("For hver bokstav(byte)")

# For each letter
eachLetters = eachLetter()
eachLetters.runTest()

