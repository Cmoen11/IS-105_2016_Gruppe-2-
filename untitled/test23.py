import time
from tkinter import *
animation = Tk()

canvas = Canvas(animation, width=800, height=600)
canvas.pack()
canvas.create_rectangle(0,0,20,20, fill="brown")

for x in range(0,100):
    canvas.move(1,5,0)
    animation.update()
    time.sleep(0.02)