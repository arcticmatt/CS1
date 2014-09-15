from Tkinter import *
import random

# Graphics commands.

<your code goes here>

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    <your code goes here>

def button_handler(event):
    '''Handle left mouse button click events.'''
    <your code goes here>


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    <your code goes here>

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()

