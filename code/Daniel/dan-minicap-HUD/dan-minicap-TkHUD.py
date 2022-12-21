
from tkinter import *
# import time

WIDTH = 500
HEIGHT = 500
LINEWIDTH = 3
TRANSCOLOUR = "" # used to be "grey" # leaving fill as "" is supposed to make it transparent?
global old
old = ()

tk = Tk()
tk.title('Virtual whiteboard')
tk.wm_attributes('-alpha',0.5) # Sets main window opacity value
tk.wm_attributes('-transparent', True) # code 'runs' but doesnt work/make it transparent
# tk.wm_attributes('-fullscreen', True)
# tk.wm_attributes("-topmost", True)
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.config(cursor='tcross')
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=TRANSCOLOUR, outline=TRANSCOLOUR)
def buttonmotion(evt):
    global old
    if old == ():
        old = (evt.x, evt.y)
        return
    else:
        canvas.create_line(old[0], old[1], evt.x, evt.y, width=LINEWIDTH)
        old = (evt.x, evt.y)
def buttonclick(evt):
    global old
    canvas.create_line(evt.x-1, evt.y-1, evt.x, evt.y, width=LINEWIDTH)
    old = (evt.x, evt.y)
canvas.bind('<Button-1>', buttonmotion)
canvas.bind('<B1-Motion>', buttonclick)
while True:
    tk.update()
    # time.sleep(0.01)


#### Fullscreen mode is no longer transparent...

