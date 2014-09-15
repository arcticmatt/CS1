# Matt Lim
'''
lab3b.py
Simple L-system simulator.
'''

# References:
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ----------------------------------------------------------------------
# Example L-systems.
# ----------------------------------------------------------------------

# Koch snowflake.
koch = { 'start' : 'F++F++F',
    'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1',
    '+' : 'R 60',
    '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A',
    'A'     : '-BF+AFA+FB-' ,
    'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1',
    '-' : 'L 90',
    '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G',
    'F'     : 'F-G+F+G-F',
    'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1',
    'G' : 'F 1',
    '+' : 'L 120',
    '-' : 'R 120' }

# ----------------------------------------------------------------------
# L-systems functions.
# ----------------------------------------------------------------------

def iterate(lsys, n):
  '''Does: Takes a starting L-system string and generates the nth version
  of it.
  Arguments: An L-system dictionary and an integer that is the number of
  times to iterate.
  Returns: Returns the string which results from starting
  with the starting string for that L-system and updating n times.'''

  iterated_string = lsys['start']
  for i in range(n):
    iterated_string = update(lsys, iterated_string)
  return iterated_string

def lsystemToDrawingCommands(draw, s):
  '''Does: Loops through a string adds the characters whose values
  are drawing commands to a list.
  Arguments: An L-system dictionary whose keys are characters in L-system
  strings and whose values are drawing commands and an L-system string.
  Returns: The list of drawing commands needed to draw the figure corresponding
  to the L-system string.'''

  lst_draw_commands = []
  if s != None:
    for char in s:
      if char in draw:
        lst_draw_commands.append(draw[char])
  return lst_draw_commands

def bounds(cmds):
  '''Does: Computes the bounding coordinates of a drawing given in commands.
  Arguments: A list of commands.
  Returns: The min and max x and y values.'''

  x_min = 0
  x_max = 0
  y_min = 0
  y_max = 0
  x_temp = 0
  y_temp = 0
  angle_temp = 0
  for cmd in cmds:
    x_temp, y_temp, angle_temp = nextLocation(x_temp, y_temp, angle_temp, cmd)
    if x_temp < x_min:
      x_min = x_temp
    if x_temp > x_max:
      x_max = x_temp
    if y_temp < y_min:
      y_min = y_temp
    if y_temp > y_max:
      y_max = y_temp
  return (x_min, x_max, y_min, y_max)


def nextLocation(x, y, angle, cmd):
  '''Does: Gets the next location and direction of the turtle
  after cmd has executed.
  Arguments: Current x, y, and angle values and the command to be
  executed.
  Returns: The new x, y, and angle in a tuple.'''

  new_x = x
  new_y = y
  new_angle = angle
  lst_directions = cmd.split()
  direction_one = lst_directions[0]
  direction_two = int(lst_directions[1])
  if direction_one == 'F':
    rads = angle * (math.pi / 180)
    new_x = x + math.cos(rads)
    new_y = y + math.sin(rads)
  elif direction_one == 'L':
    new_angle = (angle + direction_two) % 360
  elif direction_one == 'R':
    new_angle = (angle - direction_two) % 360
  return (new_x, new_y, new_angle)

def saveDrawing(filename, bounds, cmds):
  '''Does: Saves file of bounds and drawing commands.
  Arguments: The file name string, bounds tuple, and cmds list.
  Returns: Void.'''

  my_file = open(filename, 'w')
  for number in bounds:
    my_file.write("%f " % (number))
  my_file.write("\n")
  for cmd in cmds:
    my_file.write("%s\n" % (cmd))
  my_file.close()

def update(my_dict, l_system_string):
  '''Does: Generates the next version of the L-system
  by applying the L-system rules to each character of the string
  and combining all the strings into one big string.
  Arguments: A dictionary for a particular L-system and an L-system string.
  Returns: A big string containing the next version of the L-system string.'''

  updated_string = ''
  for char in l_system_string:
    if char not in my_dict:
      updated_string += char
    else:
      updated_string += my_dict[char]
  return updated_string

def makeDrawings(name, lsys, ldraw, imin, imax):
  '''Make a series of L-system drawings.'''

  print 'Making drawings for %s...' % name
  for i in range(imin, imax):
    l = iterate(lsys, i)
    cmds = lsystemToDrawingCommands(ldraw, l)
    b = bounds(cmds)
    saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
  makeDrawings('koch', koch, koch_draw, 0, 6)
  makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
  makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)

