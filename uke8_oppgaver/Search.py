import timeit
# -*- coding: utf-8 -*-
'''
This class will hold every search method yeah
'''


class Search:
    def __init__(self):
        pass

    def search_fast(self):
        for item in self.prepare:                               # Go trough every symbol in the list
            if item == self.needle:                             # check if the symbol match the needle
                return True                                     # Return true if the needle is founded
        return False                                            # Return false if the needle is not found

    def search_slow(self):
        return_value = False                                    # If results is found
        for item in self.prepare:                               # go trough every symbol in prepare
            if item == self.needle:                             # check if the symbol match the needle
                return_value = True                             # set the boolean to true if found
        return return_value                                     # return the boolean

    def run_test_fast(self, n):

        # Search Fast
        benchmark = timeit.Timer(self.search_fast)              # set up the timer for search_fast
        time = benchmark.timeit(n)                              # run trough the test n times
        average = float(time) / n                               # The average time

        print("Search-fast :", time, "seconds to go trough " + str(n) + " times")
        print("That's an average of " + str(average))

        return average

    def run_test_slow(self, n):
        # Search Slow
        benchmark = timeit.Timer(self.search_slow)              # set up the timer for search_slow
        time = benchmark.timeit(n)                              # run trough the test n times
        average = float(time) / n                               # The average time

        print("Search-slow :", time, "seconds to go trough " + str(n) + " times")
        print("That's an average of " + str(average))

        return average

    def run_test(self, n):
        '''
            Run both test metods
            :param n:   How many times to run the same test
        '''
        self.run_test_fast(n)                                   # fast run
        self.run_test_slow(n)                                   # Slow run