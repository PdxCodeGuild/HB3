
from tkinter import *
# import time

WIDTH = 500
HEIGHT = 500
LINEWIDTH = 4
TRANSCOLOUR = 'black'
global old
old = ()

tk = Tk()
tk.title('Virtual whiteboard')
tk.wm_attributes('-alpha',0.5) # Sets window opacity value
# tk.wm_attributes('-transparent')
tk.wm_attributes("-topmost", True)
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

