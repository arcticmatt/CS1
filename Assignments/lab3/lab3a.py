# Matt Lim
# Ex B.1:
def list_reverse(lst):
  '''Does: Returns the reverse of a list
  without reversing the original list.
  Arguments: A list to base the reversed list off of.
  Returns: A reversed list.'''

  lst2 = lst[:]
  lst2.reverse()
  return lst2

# Ex B.2:
def list_reverse2(lst):
  '''Does: Returns the reverse of a list
  without reversing the original list.
  Arguments: A list to base the reversed list off of.
  Returns: A reversed list.'''

  lst2 = []
  for x in range(len(lst) - 1, -1, -1):
    lst2.append(lst[x])
  return lst2

# Ex B.3:
def file_info(file_name):
  '''Does: Gets the number of lines, words, and chars
  in a file.
  Arguments: The file name as a string.
  Returns: A tuple of line/word/char numbers.'''

  my_file = open(file_name, 'r')
  num_lines = 0
  num_words = 0
  num_chars = 0
  for line in my_file:
    num_lines += 1
    num_words += len(line.split())
    num_chars += len(line)
  my_file.close()
  return(num_lines, num_words, num_chars)

# Ex B.4:
def file_info2(file_name):
  '''Does: Takes a file and creates a dictionary
  of line/word/char numbers.
  Arguments: The file name as a string.
  Returns: A dictionary of line/word/char numbers'''

  lines, words, chars = file_info(file_name)
  my_dictionary = {'lines' : lines, 'words': words, \
      'characters' : chars}
  return my_dictionary

# Ex B.5:
def longest_line(file_name):
  '''Does: Gets the max line length and the max line
  itself.
  Arguments: The file name.
  Returns: A tuple of the max line length and the max line
  itself.'''

  my_file = open(file_name, 'r')
  max_line = ''
  max_line_length = 0
  for line in my_file:
    if (len(line) > max_line_length):
      max_line_length = len(line)
      max_line = line
  my_file.close()
  return (max_line_length, max_line)

# Ex B.6:
def sort_words(split_string):
  '''Does: Splits a string into a list of words and sorts them.
  Arguments: The string to be split.
  Returns: The sorted split string.'''

  lst = split_string.split()
  lst.sort()
  return lst

# Ex B.7:
# 11011010 in decimal = 2 + 2^3 + 2^4 + 2^6 + 2^7 = 218
# The largest eight-digit binary number
# in decimal is 255, which can be written
# in binary as 11111111

# Ex C.2.1:
# 1. No spaces after commas.
# 2. No spaces between multiplication or addition signs.
# 3. Non descriptive function name.
def sum_cubes(a, b, c):
  return a * a * a + b * b * b + c * c * c

# Ex C.2.2:
# 1. Bad variable names (too long) and bad variable and function names (styles)
# 2. Comments are not grammatically correct.
# 3. No space after the # (for the comment)
# 4. Line is too long.
def sum_of_cubes(a, b, c, d):
  # Returns the sum of the cubes of a, b, c, and d.
  return a * a * a + b * b * b + c * c * c + d * d * d

# Ex C.2.3:
# 1. No blank lines between functions.
# 2. Inconsistent indentation.
def sum_of_squares(x ,y):
  return x * x + y * y


def sum_of_three_cubes(x, y, z):
  return x * x * x + y * y * y + z * z * z




