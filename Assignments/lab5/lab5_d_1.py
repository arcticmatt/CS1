from Tkinter import *
import random

# Graphics commands.

def draw_circle(x, y):
    '''Does: Draws a filled circle of the current color
    and a randomly-chosen diameter between 10 and 50 pixels,
    centered at the current position of the mouse cursor.
    Arguments:
    -- x: The x coordinate of the button click.
    -- y: The y coordinate of the button click.
    Returns: A circle.'''

    diameter = random.randint(10, 51)
    radius = diameter / 2
    remainder = diameter % 2
    circle = canvas.create_oval(x - radius + remainder, y - radius + \
            remainder , x + radius, y + radius, outline = color, \
            fill = color, width = 4) \

    return circle

def random_color():
    '''Does: Generates a random color value
    in a form recognized by the Tkinter graphics package.
    Arguments: None.
    Returns: A color in the form #XXXXXX, where X is a
    hexadecimal digit.'''

    hex_sequence = ['0', '1', '2', '3', '4', '5', '6', '7', '8', \
            '9', 'a', 'b', 'c', 'd', 'e', 'f']
    rand_color = '#'
    for i in range(0, 6):
        rand_color += random.choice(hex_sequence)
    return rand_color

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    global color
    global circles

    key = event.keysym
    if key == 'q':
        quit()
    elif key == 'c':
        color = random_color()
    elif key == 'x':
        for circle in circles:
            canvas.delete(circle)
        circles = []

def button_handler(event):
    '''Handle left mouse button click events.'''

    circles.append(draw_circle(event.x, event.y))

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    color = random_color()
    circles = []

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()

