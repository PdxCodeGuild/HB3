#---------------------------------
# PDX Code Guild: HB3
# Mini Capstone: Heads-Up Display (HUD) Overlay
# Author: Daniel Smith
# Date: 2022.12.13
#---------------------------------

# My HUD project turned into a whiteboard for now lol...

# HUD Overlay Project
# Idea is to begin with a transparent window background,
# then build visible/opaque elements inside of it,
# and format and connect those elements to sensor data on the backend.

from tkinter import *

WIDTH = 500
HEIGHT = 500
LINEWIDTH = 4
TCOLOR = "grey" # leaving fill as "" will make the layer transparent.
old = ()

def buttonmotion(event):
    old = (event.x, event.y)
def buttonclick(event):
    canvas.create_line(event.x-3, event.y-3, event.x, event.y, width=LINEWIDTH)
    old = (event.x, event.y)

root = Tk()
root.title('Whiteboard - Click to Draw')
root.wm_attributes('-alpha',0.2) # Sets the main window opacity value, gets overridden by canvas transparency value.
root.wm_attributes("-topmost", True)
# root.wm_attributes('-fullscreen', True) #### Fullscreen mode disables the window transparency.

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
root.wm_attributes('-alpha',0.6) # overrides root transparency value.
canvas.pack()
canvas.config(cursor='tcross')
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=TCOLOR, outline=TCOLOR)

canvas.bind('<Button-1>', buttonmotion)
canvas.bind('<B1-Motion>', buttonclick)

# Button for closing  
exitbutton = Button(root, text="Exit", command=root.destroy)
exitbutton.pack(side = BOTTOM)

root.mainloop()