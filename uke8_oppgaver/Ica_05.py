import timeit
'''
This python document include two classes, one is for checking each symbol in a file, and another one for checking each
word in the selected file.

To call each class, you need to give it a number on how many test i

'''


class EachLetter:
    def __init__(self, filename, needle):
        self.needle = needle                                    # the word we're looking for
        self.fileName = filename                                # The file we're searching trough
        self.prepare = open(self.fileName, 'r').read()          # Open file
        pass

    # Go trough every letter, and look for match, return True back when match is found
    def search_fast(self):
        for item in self.prepare:                               # Go trough every symbol in the list
            if item == self.needle:                             # check if the symbol match the needle
                return True                                     # Return true if the needle is founded
        return False                                            # Return false if the needle is not found

    # Go trough every letter, look for match, set Return_value to true and return after running trough every letter
    def search_slow(self):
        return_value = False                                    # If results is found
        for item in self.prepare:                               # go trough every symbol in prepare
            if item == self.needle:                             # check if the symbol match the needle
                return_value = True                             # set the boolean to true if found
        return return_value                                     # return the boolean

    # Run test and print out time taken for running the tests
    # @param n      The number on how many runs it will run through

    def run_test(self, n):

        # Search Slow
        benchmark = timeit.Timer(self.search_slow)              # set up the timer for search_slow
        time = benchmark.timeit(n)                              # run trough the test n times
        average = float(time) / n                               # The average time

        print("Search-slow :", time, "seconds to go trough " + str(n) + " times")
        print("That's an average of " + str(average))

        # Search Fast
        benchmark = timeit.Timer(self.search_fast)              # set up the timer for search_fast
        time = benchmark.timeit(n)                              # run trough the test n times
        average = float(time) / n                               # The average time

        print("Search-fast :", time, "seconds to go trough " + str(n) + " times")
        print("That's an average of " + str(average))
        pass



class EachWord:
    def __init__(self, filename, needle):
        self.needle = needle                                    # the word we're looking for
        self.fileName = filename                                # The file we're searching trough
        self.words = open(self.fileName, 'r').read().split()    # Open file, and split words
        pass

    # Go trough every word, and look if they match, return True back when match is found
    def search_fast(self):
        for word in self.words:                                 # Go trough every word in the list
            if word == self.needle:                             # check if the word match the needle
                return True                                     # Return true if the needle is founded
        return False                                            # Return false if the needle is not found

    # Go trough every word, and look if they match, set Return_value to true and return after running trough every word
    def search_slow(self):
        return_value = False                                    # If results is found
        for word in self.words:                                 # go trough every word in the list
            if word == self.needle:                             # check if the word match the needle
                return_value = True                             # set the boolean to true if found
        return return_value                                     # return the boolean

    # Run test and print out time taken for running the tests
    # @param n      The number on how many runs it will run trough
    def run_test(self, n):

        # Search Slow
        benchmark = timeit.Timer(self.search_slow)              # set up the timer for search_slow
        time = benchmark.timeit(n)                              # run trough the test n times
        average = float(time) / n                               # The average time

        print("Search-slow :", time, "seconds to go trough " + str(n) + " times")
        print("That's an average of " + str(average))

        # Search Fast
        benchmark = timeit.Timer(self.search_fast)              # set up the timer for search_fast
        time = benchmark.timeit(n)                              # run trough the test n times
        average = float(time) / n                               # The average time

        print("Search-fast :", time, "seconds to go trough " + str(n) + " times")
        print("That's an average of " + str(average))
        pass



# For each word
print("For hvert ord")
eachWords = EachWord('shakespare.txt', 'The')
eachWords.run_test(10)
print()
print("For hver bokstav(byte)")

# For each letter
eachLetters = EachLetter('shakespare.txt', 'T')
eachLetters.run_test(1)
