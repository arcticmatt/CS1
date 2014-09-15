from Tkinter import *
import random
from lab4_b import *
from lab4_d2 import draw_square

if __name__ == '__main__':
  root = Tk()
  root.geometry('800x800')
  c = Canvas(root, width=800, height=800)
  c.pack()

  for i in range(0, 50):
    rand_center = random_position(800, 800)
    rand_color = random_color()
    rand_size = random_size(20, 150)

    draw_square(c, rand_color, rand_size, rand_size, \
        rand_center)

  root.bind('<q>', quit)
  root.mainloop()

