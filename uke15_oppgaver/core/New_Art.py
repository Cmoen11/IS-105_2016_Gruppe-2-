# -*- coding: utf-8 -*-
import threading
import time
from Tkinter import *

from state import State
from uke15_oppgaver.ClientHandler import client as s


class Art:
    def __init__(self, master, state, id):

        self.state = state
        self.master = master
        self.id = id


        tape = state.tape

        top_frame = Frame(master)           # This holds items and boat
        top_frame.pack()                    # add frame into our master

        bottom_frame = Frame(master)        # this will hold land A, land b and water
        bottom_frame.pack()                 # add frame into the master

        controll_frame = Frame(master)      # to hold every button
        controll_frame.pack(side=BOTTOM)    # add it to our master

        master.title('River crossing')      # title of our window

        #items land A
        self.items_a_canvas = Canvas(top_frame, width=100, height=100)
        self.items_a_canvas.pack(side=LEFT)

        if tape.corn in 'left':
            self.corn = self.items_a_canvas.create_rectangle(5,100,20,85, fill="yellow")

        if tape.chicken in 'left':
            self.chicken = self.items_a_canvas.create_rectangle(50,100,29,85, fill="green")

        if tape.fox in 'left':
            self.fox = self.items_a_canvas.create_rectangle(80,100,60,85, fill="blue")

        if tape.man in 'left':
            self.man = self.items_a_canvas.create_rectangle(100,100,85,50, fill="black")

        # for the boat
        self.boat_canvas = Canvas(top_frame, width=500, height=100)
        self.boat_canvas.pack(side=LEFT)
        #self.man_boat = self.boat_canvas.create_rectangle(0,100,20,50, fill="black")

        if tape.boat in 'left':
            self.red_boat = self.boat_canvas.create_rectangle(0,100,50,60, fill="red")
        elif tape.boat in 'right':
            self.red_boat = self.boat_canvas.create_rectangle(500,100,450,60, fill="red")
            print 'moved'

        # items land B
        self.items_b_canvas = Canvas(top_frame, width=100, height=100)
        self.items_b_canvas.pack(side=LEFT)
        if tape.corn in 'right':
            self.corn = self.items_b_canvas.create_rectangle(5,100,20,85, fill="yellow")

        if tape.chicken in 'right':
            self.chicken = self.items_b_canvas.create_rectangle(50,100,29,85, fill="green")

        if tape.fox in 'right':
            self.fox = self.items_b_canvas.create_rectangle(80,100,60,85, fill="blue")

        if tape.man in 'right':
            self.man = self.items_b_canvas.create_rectangle(100,100,85,50, fill="black")


        #land A
        self.land_A = Canvas(bottom_frame, width=100, height=30)
        self.land_A.pack(side=LEFT)
        land_a = self.land_A.create_rectangle(0, 0, 100, 50, fill="brown")

        # water
        self.water_c = Canvas(bottom_frame, width=500, height=30)
        self.water_c.pack(side=LEFT)

        water = self.water_c.create_rectangle(0, 0, 600, 50, fill="blue")


        #Land B
        self.land_B = Canvas(bottom_frame, width=100, height=30)
        self.land_B.pack(side=LEFT)

        land_b = self.land_B.create_rectangle(0, 0, 100, 50, fill="brown")

        # controll buttons

        t = self.state.tape
        self.button1 = Button(controll_frame, text="Gå inn/ut i båten", fg="red", command=self.man_go_inside_boat)
        self.button2 = Button(controll_frame, text="Sett kylling inn/ut ", fg="red", command=self.chicken_inorout)
        self.button3 = Button(controll_frame, text="Sett Korn inn/ut ", fg="red", command=self.corn_inorout)
        self.button4 = Button(controll_frame, text="Sett Rev inn/ut ", fg="red", command=self.fox_inorout)
        self.button5 = Button(controll_frame, text="Kryss elven ", fg="red", command=self.boat_move)

        # add buttons to our master
        self.button1.pack(side=LEFT)
        self.button2.pack(side=LEFT)
        self.button3.pack(side=LEFT)
        self.button4.pack(side=LEFT)
        self.button5.pack(side=LEFT)

        server_check = threading.Thread(target=self.check_server)
        server_check.start()

    def client_queue(self):
        while True:
            pass

    def man_go_inside_boat(self):

        # man is at either left or right
        if self.state.tape.man in 'left' or self.state.tape.man in 'right':

            # remove man from either left or right side
            if self.state.tape.man in 'left':                                   # if the man is at left
                self.items_a_canvas.delete(self.man)                            # -> Remove man from left

            elif self.state.tape.man in 'right':                                # if the man is right
                self.items_b_canvas.delete(self.man)                            # -> remove the man from right

            self.state.tape.set_man('boat')                                     # set the new pos to the man

        # man is at boat, and the boat is either left or right.
        elif self.state.tape.man in 'boat' and self.state.tape.boat in 'left':
            self.man = self.items_a_canvas.create_rectangle(100,100,85,50, fill="black")    # add man to the left side
            self.state.tape.set_man('left')                                                 # update the tape

        elif self.state.tape.man in 'boat' and self.state.tape.boat in 'right':
            self.man = self.items_b_canvas.create_rectangle(100,100,85,50, fill="black")    # add man to the right side
            self.state.tape.set_man('right')                                                # update the tape
        if (self.state.tape.man != s.client('(%s) get man' % self.id)):
            self.move_item('man', self.state.tape.man)                            # update the server with new information
        self.check_death()                                                      # Check death

    def boat_move(self):
        if self.state.tape.man in 'boat':                           # if man is inside of the boat
            if self.state.tape.boat in 'left':                      # if boat is left
                self.state.tape.set_boat('right')                   # update the tape with the information
                if (self.state.tape.boat != s.client('(%s) get boat' % self.id)):
                    self.move_item('boat', 'right')        # update the server with new information
                # move the boat
                for x in range(0, 90):                              # move 90 times
                    self.boat_canvas.move(1, 5, 0)                  # move 1 px
                    self.boat_canvas.update()                       # update the canvas
                    time.sleep(0.02)                                # seep for 0.02 seconds

            elif self.state.tape.boat in 'right':                   # if the boat is right
                self.state.tape.set_boat('left')                    # update the tape
                if (self.state.tape.boat != s.client('(%s) get boat' % self.id)):
                    self.move_item('boat', 'left')                      # update the server with new information
                for x in range(0,90):                               # move 90 times
                    self.boat_canvas.move(1,-5,0)                   # move -1 px
                    self.boat_canvas.update()                       # update the canvas
                    time.sleep(0.02)                                # sleep for 0.02 seconds
        self.check_death()                                          # check death

    def chicken_inorout(self):
        if self.state.tape.corn in 'boat' \
                or self.state.tape.fox in 'boat' \
                or self.state.tape.man in 'boat':                   # if either corn, fox or man is inside the boat
            return None                                             # break the action by returning None

        if self.state.tape.chicken in 'boat':                       # if chicken is inside of the boat
            self.state.tape.set_chicken(self.state.tape.boat)       # update the tape as where the chicken is placed.

            # bring up the chicken symbol
            if self.state.tape.boat in 'left':
                self.chicken = self.items_a_canvas.create_rectangle(50,100,29,85, fill="green")
            elif self.state.tape.boat in 'right':
                self.chicken = self.items_b_canvas.create_rectangle(50,100,29,85, fill="green")

        elif self.state.tape.chicken in 'left' and self.state.tape.boat in 'left' \
                or self.state.tape.chicken in 'right' and self.state.tape.boat in 'right':

            self.state.tape.set_chicken('boat')             # set the tape chicken into the boat
            # remove the symbol from either a or b(left or right)
            if self.state.tape.boat in 'left':
                self.items_a_canvas.delete(self.chicken)    # remove the chicken from the left

            elif self.state.tape.boat in 'right':

                self.items_b_canvas.delete(self.chicken)    # remove the chicken from the right

        if (self.state.tape.chicken != s.client('(%s) get chicken' % self.id)):
            self.move_item('chicken', self.state.tape.chicken)
        self.check_death()

    def corn_inorout(self):
        if self.state.tape.chicken in 'boat' \
                or self.state.tape.fox in 'boat' \
                or self.state.tape.man in 'boat':           # if either chicken, fox or man is inside of the boat
            return None                                     # -> Break the method

        if self.state.tape.corn in 'boat':
            self.state.tape.set_corn(self.state.tape.boat)  # Update the tape.

            # bring up the corn symbol
            if self.state.tape.boat in 'left':
                self.corn = self.items_a_canvas.create_rectangle(5,100,20,85, fill="yellow")
            elif self.state.tape.boat in 'right':
                self.corn = self.items_b_canvas.create_rectangle(5,100,20,85, fill="yellow")

        elif self.state.tape.corn in 'left' and self.state.tape.boat in 'left' \
                or self.state.tape.corn in 'right' and self.state.tape.boat in 'right':
            self.state.tape.set_corn('boat')

            # remove the symbol from either a or b(left or right)
            if self.state.tape.boat in 'left':
                self.items_a_canvas.delete(self.corn)
            elif self.state.tape.boat in 'right':
                self.items_b_canvas.delete(self.corn)

        if (self.state.tape.corn != s.client('(%s) get corn' % self.id)):
            self.move_item('corn', self.state.tape.corn)                # update the server with new information
        self.check_death()

    def fox_inorout(self):
        if self.state.tape.chicken in 'boat' \
                or self.state.tape.corn in 'boat' \
                or self.state.tape.man in 'boat':               # if either chicken, corn or man is inside of the boat
            return None                                         # -> break the method by returning None.

        elif self.state.tape.fox in 'boat':
            self.state.tape.set_fox(self.state.tape.boat)       # update the tape

            # bring up the fox symbol
            if self.state.tape.boat in 'left':
                self.fox = self.items_b_canvas.create_rectangle(80,100,60,85, fill="blue")
            elif self.state.tape.boat in 'right':
                self.fox = self.items_b_canvas.create_rectangle(80,100,60,85, fill="blue")

        elif self.state.tape.fox in 'left' and self.state.tape.boat in 'left' \
                or self.state.tape.fox in 'right' and self.state.tape.boat in 'right':
            self.state.tape.set_fox('boat')


            # remove the symbol from either a or b(left or right)
            if self.state.tape.boat in 'left':
                self.items_a_canvas.delete(self.fox)
            elif self.state.tape.boat in 'right':
                self.items_b_canvas.delete(self.fox)

        if (self.state.tape.fox != s.client('(%s) get fox' % self.id)):
            self.move_item('fox', self.state.tape.fox)                # update the server with new information
        self.check_death()

    def check_death(self):
        if self.state.check_lose_combo():
            print('Player dead')
            self.master.title('Game over')
            while True:
                print('game Over')
                self.master.destroy()


    def get_state(self):
        '''
        this will update the state with servers version of state.
        '''
        new_state = State()
        new_state.tape.set_man(s.client('(%s) get man' % self.id))
        new_state.tape.set_boat(s.client('(%s) get boat' % self.id))
        new_state.tape.set_chicken(s.client('(%s) get chicken' % self.id))
        new_state.tape.set_fox(s.client('(%s) get fox' % self.id))
        new_state.tape.set_corn(s.client('(%s) get corn' % self.id))

        #print 'server: ' + state.tape.chicken


        return new_state

    def isAllowedToMove(self):
        request = '%s is allowed' % self.id
        isAllowed = s.client(request)
        #print isAllowed
        if isAllowed == 'True' : isAllowed = True
        elif isAllowed == 'False': isAllowed = False

        if (not isAllowed) :
            self.button1['state'] = 'disabled'
            self.button2['state'] = 'disabled'
            self.button3['state'] = 'disabled'
            self.button4['state'] = 'disabled'
            self.button5['state'] = 'disabled'
        else :
            self.button1['state'] = 'normal'
            self.button2['state'] = 'normal'
            self.button3['state'] = 'normal'
            self.button4['state'] = 'normal'
            self.button5['state'] = 'normal'


    def check_server(self):
        '''
        Send request to the server, and check if current state match server state.
        if not, run the necessary commands to get the state to the server state.
        :return:
        '''
        while True:
            time.sleep(0.10)
            self.isAllowedToMove()                      # Check if user is allowed to move items/person

            server_state = self.get_state()
            server_tape = server_state.tape
            tape = self.state.tape

            #print 'client: ' + tape.chicken
            if server_tape.chicken != tape.chicken:
                self.chicken_inorout()
            elif server_tape.man != tape.man:
                self.man_go_inside_boat()
            elif server_tape.corn != tape.corn:
                self.corn_inorout()
            elif server_tape.boat != tape.boat:
                self.boat_move()
            elif server_tape.fox != tape.fox:
                self.fox_inorout()


    def move_item(self, item, pos):
        '''
        This will change the current state of the selected item to the server.
        :param item:
        :param pos:
        :return:
        '''
        request = self.id+' move '+item+' '+pos
        print 'request sent: ' +request
        s.client(request)




