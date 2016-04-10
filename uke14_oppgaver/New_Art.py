# -*- coding: utf-8 -*-
import time
from Tkinter import *
from state import State


class Art:
    def __init__(self, master):

        self.state = State()

        self.master = master

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
        self.corn = self.items_a_canvas.create_rectangle(5,100,20,85, fill="yellow")
        self.chicken = self.items_a_canvas.create_rectangle(50,100,29,85, fill="green")
        self.fox = self.items_a_canvas.create_rectangle(80,100,60,85, fill="blue")
        self.man = self.items_a_canvas.create_rectangle(100,100,85,50, fill="black")

        # for the boat
        self.boat_canvas = Canvas(top_frame, width=500, height=100)
        self.boat_canvas.pack(side=LEFT)
        #self.man_boat = self.boat_canvas.create_rectangle(0,100,20,50, fill="black")
        self.red_boat = self.boat_canvas.create_rectangle(0,100,50,60, fill="red")


        # items land B
        self.items_b_canvas = Canvas(top_frame, width=100, height=100)
        self.items_b_canvas.pack(side=LEFT)

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
        button1 = Button(controll_frame, text="Gå inn/ut i båten", fg="red", command=self.man_go_inside_boat)
        button2 = Button(controll_frame, text="Sett kylling inn/ut ", fg="red", command=self.chicken_inorout)
        button3 = Button(controll_frame, text="Sett Korn inn/ut ", fg="red", command=self.corn_inorout)
        button4 = Button(controll_frame, text="Sett Rev inn/ut ", fg="red", command=self.fox_inorout)
        button5 = Button(controll_frame, text="Kryss elven ", fg="red", command=self.boat_move)

        # add buttons to our master
        button1.pack(side=LEFT)
        button2.pack(side=LEFT)
        button3.pack(side=LEFT)
        button4.pack(side=LEFT)
        button5.pack(side=LEFT)

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

        self.check_death()                                                      # Check death

    def boat_move(self):
        if self.state.tape.man in 'boat':                           # if man is inside of the boat
            if self.state.tape.boat in 'left':                      # if boat is left
                # move the boat
                for x in range(0, 90):                              # move 90 times
                    self.boat_canvas.move(1, 5, 0)                  # move 1 px
                    self.boat_canvas.update()                       # update the canvas
                    time.sleep(0.02)                                # seep for 0.02 seconds

                self.state.tape.set_boat('right')                   # update the tape with the information

            elif self.state.tape.boat in 'right':                   # if the boat is right
                for x in range(0,90):                               # move 90 times
                    self.boat_canvas.move(1,-5,0)                   # move -1 px
                    self.boat_canvas.update()                       # update the canvas
                    time.sleep(0.02)                                # sleep for 0.02 seconds

                self.state.tape.set_boat('left')                    # update the tape
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

            print('chicken in boat')
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
                self.corn = self.items_b_canvas.create_rectangle(5,100,20,85, fill="yellow")
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
        self.check_death()

    def check_death(self):
        if self.state.check_lose_combo():
            print('Player dead')
            self.master.title('Game over')
            while True:
                print('game Over')
                self.master.destroy()


root = Tk()
art = Art(root)

root.mainloop()

