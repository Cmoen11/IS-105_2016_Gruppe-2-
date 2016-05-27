from uke15_oppgaver.core.tape import Database


def state_protocol(tape, request):
    request_fragment = request.split()
    if request_fragment[0] == 'move':
        print request_fragment

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

        elif request_fragment[1] == 'boat':
            if request_fragment[2] in ('left','right') and tape.man == 'boat':
                return True
            else:
                return False

    elif request_fragment[0] == 'ID':
        return True

    elif request_fragment[0] == 'get':
        return True

    else:
        return False



if __name__ == "__main__":
    print state_protocol(
        Database(), 'move fox right'
    )