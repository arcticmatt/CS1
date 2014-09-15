from Tkinter import *
import random
import math

# Graphics commands.

class Point:
    '''Instances of this class are two-dimensional
    points in Euclidean space (w/real valued coordinates).'''

    def __init__(self, x, y):
        '''Constructor that initializes the x, y coordinates'''
        self.x = x
        self.y = y

def draw_star(x, y):
    '''Does: Draws a star, with (points) number of points.
    The radius is between 50 and 100 inclusive and is randomly generated.
    Arguments:
    -- x: The x coordinate of the button click.
    -- y: The y coordinate of the button click.
    Returns: Void.'''

    radius = random.randint(50, 101)
    # Angle difference between adjacent points
    angle_diff = (2 * math.pi) / points

    for i in range(points):
        # Starting angle
        angle1 = (3 * math.pi) / 2 + i * ((2 * math.pi) / points)
        # Ending angle for the first line
        angle2 = angle1 + angle_diff * ((points - 1) / 2)
        # Ending angle for the second line
        angle3 = angle2 + angle_diff
        pt1 = Point(x + radius * math.cos(angle1), \
                y + radius * math.sin(angle1))
        pt2 = Point(x + radius * math.cos(angle2), \
                y + radius * math.sin(angle2))
        pt3 = Point(x + radius * math.cos(angle3), \
                y + radius * math.sin(angle3))
        draw_line(pt1, pt2)
        draw_line(pt1, pt3)


def draw_line(pt1, pt2):
    '''Does: Draws a line between two points.
    Arguments:
    -- pt1: A Point object representing the point to start the line at.
    -- pt2: A Point object representing the point to end the line at.
    Returns: A list of lines drawn on the canvas.'''

    global lines

    line = canvas.create_line(pt1.x, pt1.y, pt2.x, pt2.y,
            fill = color, width = 2)
    lines.append(line)
    return lines

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
    global lines
    global points

    key = event.keysym
    if key == 'q':
        quit()
    elif key == 'c':
        color = random_color()
    elif key == 'x':
        for line in lines:
            canvas.delete(line)
        lines = []
    elif key == 'plus':
        points += 2
    elif key == 'minus':
        if points > 5:
            points -= 2

def button_handler(event):
    '''Handle left mouse button click events.'''

    draw_star(event.x, event.y)

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    color = random_color()
    lines = []
    points = 5

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()

