import timeit

'''
This class will hold every search method
'''


class Search:
    def __init__(self):
        pass

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
