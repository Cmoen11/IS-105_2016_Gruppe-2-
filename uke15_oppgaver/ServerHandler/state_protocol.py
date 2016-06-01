from uke15_oppgaver.core.tape import Database


def state_protocol(tape, request, id):
    request_fragment = request.split()          # split request to fragments.

    # for requesting ID, no need for checking here -> allowed.
    if request_fragment[1] == 'ID':
        return True

    # requesting position, no need for checking here -> allowed.
    elif request_fragment[1] == 'get':
        return True

    elif request_fragment[1] == 'is':
        return True

    # Check if the user is allowed to do stuff
    elif (str(id) != str(request_fragment[0])):
        print 'not allowed do do this action.'
        print id
        print request_fragment[0]
        exit()
        return False

    request_fragment.pop(0)      # remove the ID, because it is not longer relevant.

    # for moving items/ person / boat ...
    if request_fragment[0] == 'move':

        # for moving the man, no need to check.
        if request_fragment[1] == 'man':
            return True

        # for moving the chicken
        elif request_fragment[1] == 'chicken':
            if request_fragment[2] in 'left' and tape.man in 'left' and tape.chicken in 'boat' or\
                request_fragment[2] in 'right' and tape.man in 'right' and tape.chicken in 'boat' or\
                 request_fragment[2] in 'boat' and tape.man in 'right' and tape.boat in 'right' and tape.chicken in 'right' or \
                   request_fragment[2] in 'boat' and tape.man in 'left' and tape.boat in 'left' and tape.chicken in 'left' :
                return True
            else:
                return False

        # for moving the corn
        elif request_fragment[1] == 'corn':
            if request_fragment[2] in 'left' and tape.man in 'left' and tape.corn in 'boat' or\
                request_fragment[2] in 'right' and tape.man in 'right' and tape.corn in 'boat' or\
                 request_fragment[2] in 'boat' and tape.man in 'right' and tape.boat in 'right' and tape.corn in 'right' or \
                   request_fragment[2] in 'boat' and tape.man in 'left' and tape.boat in 'left' and tape.corn in 'left' :
                return True
            else:
                return False

        # for moving the fox
        elif request_fragment[1] == 'fox':
            if request_fragment[2] in 'left' and tape.man in 'left' and tape.fox in 'boat' or\
                request_fragment[2] in 'right' and tape.man in 'right' and tape.fox in 'boat' or\
                 request_fragment[2] in 'boat' and tape.man in 'right' and tape.boat in 'right' and tape.fox in 'right' or \
                   request_fragment[2] in 'boat' and tape.man in 'left' and tape.boat in 'left' and tape.fox in 'left' :
                return True
            else:
                return False

        # for moving the boat
        elif request_fragment[1] == 'boat':
            if request_fragment[2] in ('left','right') and tape.man == 'boat':
                return True
            else:
                return False


    # request not valid.
    else:
        return False



if __name__ == "__main__":
    print state_protocol(
        Database(), 'XX ID REQUEST', 0
    )