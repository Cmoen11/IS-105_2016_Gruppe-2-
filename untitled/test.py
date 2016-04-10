from tkinter import *
import time

root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


# move able items/boat
boat = Canvas(bottomFrame, width=700, height=100)
boat.pack()

brown_boat = boat.create_rectangle(100,100,150,60, fill="red")

#Land A
land_A = Canvas(bottomFrame, width=100, height=30)
land_A.pack(side=LEFT)

land_a = land_A.create_rectangle(0, 0, 100, 50, fill="brown")

# water
water_c = Canvas(bottomFrame, width=500, height=30)
water_c .pack(side=LEFT)

water = water_c.create_rectangle(0, 0, 600, 50, fill="blue")



#Land B
land_B = Canvas(bottomFrame, width=100, height=30)
land_B.pack(side=LEFT)

land_b = land_B.create_rectangle(0, 0, 100, 50, fill="brown")

root.title('River crossing')


def boat_move_right_no_items():
    for x in range(0,90):
        boat.move(1,5,0)
        boat.update()
        time.sleep(0.02)
def boat_move_left_no_items():
    for x in range(0,90):
        boat.move(1,-5,0)
        boat.update()
        time.sleep(0.02)

while True:
    boat_move_right_no_items()
    boat_move_left_no_items()
root.mainloop()