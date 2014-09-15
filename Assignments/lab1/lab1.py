# Matt Lim

# Ex C.1.1: 9 - 3 -->; 6
# Ex C.1.2: 8 * 2.5 -->; 20.0
# Ex C.1.3: 9 / 2 -->; 4
# Ex C.1.4: 9 / -2 -->; -5
# Ex C.1.5: 9 % 2 -->; 1
# Ex C.1.6: 9 % -2 -->; -1
# Ex C.1.7: -9 % 2 -->; 1
# Ex C.1.8: 9 / -2.0 -->; -4.5
# Ex C.1.9: 4 + 3 * 5 -->; 19
# Ex C.1.10: (4 + 3) * 5 -->; 35

# Ex C.2.1: x = 100 -->; x = 100
# Ex C.2.2: x = x + 10 -->; x = 110
# Ex C.2.3: x += 20 -->; x = 130
# Ex C.2.4: x = x - 40 -->; x = 90
# Ex C.2.5: x -= 50 -->; x = 40
# Ex C.2.6: x *= 3 -->; x = 120
# Ex C.2.7: x /= 5 -->; x = 24
# Ex C.2.8: x %= 3 -->; x = 0

# Ex C.3.1: x += x - x becomes x += 3 - 3 which becomes x += 0. Therefore x = 3.

# Ex C.4.1: 1j + 2.4j -->; 3.4
# Ex C.4.2: 4j * 4j -->; (-16 + 0j)
# Ex C.4.3: (1+2j) / (3+4j) -->; (0.44 + 0.08j)
# Ex C.4.1: (1+2j) * (1+2j) -->; (-3j + 4j)
# Ex C.4.2: 1+2j * 1+2j -->; (1 + 4j)
# They are different because with the parentheses, the two complex numbers
# are multiplied. Without the parentheses, precedence of operators takes
# place. So 1+2j * 1+2j = 1+ (2j*1) + 2j = 1+4j. Thus, Python handles
# complex numbers the same as real numbers.

# Ex C.5.1: cmath.sin(-1.0+2.0j) -->; (-3.165778513216168+1.9596010414216063j)
# Ex C.5.2: cmath.log(-1.0+3.4j) -->; (1.2652585805200263+1.856847768512215j)
# Ex C.5.3: cmath.exp(-cmath.pi * 1.0j) -->; (-1-1.2246467991473532e-16j)
# If you do "math import *" and "cmath import *" then the cmath functions
# that have the same names as the math functions will be used exclusively.
# If you use "import math" and "import cmath" then you can use all
# the functions in each module.

# Ex C.6.1: "foo" + 'bar' -->; 'foobar'
# Ex C.6.2: "foo" 'bar' -->; 'foobar'
# Ex C.6.3: a + b -->; 'foobar'
# Ex C.6.4: a b -->; SyntaxError: invalid syntax

# Ex C.7.1: 'A\nB\nC'

# Ex C.8.1: 80 * '-'

# Ex C.9.1: s = 'first line\nsecond line\nthird line'

# Ex C.10.1:
print 'The rabbit is %d' % x
# Ex C.10.2:
print 'The rabbit is %d years old.' % x
# Ex C.10.3:
print '%g is average' % y
# Ex C.10.4:
print '%g * %d' % (y,x)
# Ex C.10.5:
print '%g * %d is %g' % (y,x,y*x)

# Ex C.11.1:
num = float(raw_input("Enter a number: "))
print num

# Ex C.12.1:
def quadratic(a, b, c, x):
  return a * x * x + b * x + c
# Alternatives below
def quadratic(a, b, c, x):
  return a * x**2 + b * x + c
# Next alternative relies on the math module
def quadratic(a, b, c, x):
  return a * math.pow(x,2) + b * x + c

# Ex C.13.1:
def GC_content(dna_string):
  '''Function calculates ratio of G and C bases in a DNA sequence
  Input argument is a string representing a DNA sequence
  Returns proportion of G and C characters in the string'''
  num_GC = (dna_string.count('G') + dna_string.count('C'))
  prop = num_GC / float(len(dna_string))
  return prop
