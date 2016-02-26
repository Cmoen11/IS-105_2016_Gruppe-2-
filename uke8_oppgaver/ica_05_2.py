import timeit
needle = 'T'
fileName = "shakespare.txt"
prepare = open(fileName, 'r').read()


def search_fast():
    for item in prepare:
        if item == needle:
            return True
    return False


def search_slow():
    return_value = False
    for item in prepare:
        #print (item)
        if item == needle:
            return_value = True
    return return_value


def runTest() :
    n = 1000 # time how long n action's take
    benchmark = timeit.Timer(search_slow)
    print ("Search-slow :", benchmark.timeit(n), "seconds to go trough " + str(n) + " times")
    
    benchmark = timeit.Timer(search_fast)
    print ("Search-fast :", benchmark.timeit(n), "seconds to go trough " + str(n) + " times")


runTest()