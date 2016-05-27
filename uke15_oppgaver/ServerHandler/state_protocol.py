from uke15_oppgaver.core.tape import Database


def state_protocol(tape, request):
    request_fragment = request.split()
    if request_fragment[0] == 'move':

        if request_fragment[1] == 'man':
            if request_fragment[2] == 'left':
                if tape.boat == 'left' and tape.man == 'boat':
                    return True
                else:
                    return False
            elif request_fragment[2] == 'right':
                if tape.boat == 'right' and tape.man == 'boat':
                    return True
                else:
                    return False
            elif request_fragment[2] == 'boat':
                if (tape.man in 'left' and tape.boat in 'left') or (tape.man in 'right' and tape.boat in 'right'):
                    return True
                else:
                    return False

        elif request_fragment[1] == 'chicken':
            if request_fragment[2] == 'left':
                if tape.boat == 'left' and tape.chicken == 'boat' and tape.man == 'left':
                    return True
                else:
                    return False
            elif request_fragment[2] == 'right':
                if tape.boat == 'right' and tape.chicken == 'boat' and tape.man == 'right':
                    return True
                else:
                    return False
            elif request_fragment[2] == 'boat':
                if (tape.boat in 'left' and tape.chicken in 'left' and tape.man in 'left') \
                        or (tape.boat in 'right' and tape.chicken in 'right' and tape.man in 'right'):
                    return True
                else:
                    return False

        elif request_fragment[1] == 'corn':
            if request_fragment[2] == 'left':
                if tape.boat == 'left' and tape.corn == 'boat' and tape.man == 'left':
                    return True
                else:
                    return False
            elif request_fragment[2] == 'right':
                if tape.boat == 'right' and tape.corn == 'boat' and tape.man == 'right':
                    return True
                else:
                    return False
            elif request_fragment[2] == 'boat':
                if (tape.boat in 'left' and tape.corn in 'left' and tape.man in 'left') \
                        or (tape.boat in 'right' and tape.corn in 'right' and tape.man in 'right'):
                    return True
                else:
                    return False

        elif request_fragment[1] == 'fox':
            if request_fragment[2] == 'left':
                if tape.boat == 'left' and tape.fox == 'boat' and tape.man == 'left':
                    return True
                else:
                    return False
            elif request_fragment[2] == 'right':
                if tape.boat == 'right' and tape.fox == 'boat' and tape.man == 'right':
                    return True
                else:
                    return False
            elif request_fragment[2] == 'boat':
                if (tape.boat in 'left' and tape.fox in 'left' and tape.man in 'left') \
                        or (tape.boat in 'right' and tape.fox in 'right' and tape.man in 'right'):
                    return True
                else:
                    return False


    elif request_fragment[0] == 'get':
        pass
