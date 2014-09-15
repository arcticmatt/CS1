# Matt Lim
import random

def make_random_code():
  '''Does: Makes random string 4 chars long. Each char
  may contain one of 8 chars
  Arguments: None
  Returns: The random string 4 chars long'''

  color = ''
  color_list = ['R', 'G', 'B', 'Y', 'O', 'W']
  for x in range(4):
    color += random.choice(color_list)
  return color

def count_exact_matches(str1, str2):
  '''Does: Counts exact matches in two strings.
  An exact match is the same char at the same index.
  Arguments: Two strings (of length 4)
  Returns: The number of exact matches'''

  count = 0
  for x in range(len(str1)):
    if str1[x] == str2[x]:
      count += 1
  return count

def count_letter_matches(str1, str2):
  '''Does: Counts letter matches in two strings.
  A letter match is having the same char, regardless of the index.
  However, each char can only be matched up once.
  Arguments: Two strings to be compared (of length 4)
  Returns: The number of letter matches'''

  count = 0
  lst1 = list(str1)
  lst2 = list(str2)
  for x in lst1:
    if x in lst2:
      count += 1
      lst2.remove(x)
  return count

def compare_codes(code, guess):
  '''Does: Compares two strings. Find the number of
  exact matches, number of letter matches (excluding exact matches)
  and the number of blanks.
  Arguments: The two strings to be compared.
  Returns: A string representing the number of exact matches (b),
  letter matches (w), and blanks (-)'''

  num_black = count_exact_matches(code, guess)
  num_white = count_letter_matches(code, guess) - num_black
  num_blank = 4 - num_black - num_white
  pegs = ''
  pegs += num_black * 'b'
  pegs += num_white * 'w'
  pegs += num_blank * '-'
  return pegs

def run_game():
  '''Does: Runs a game of Mastermind
  Arguments: None
  Returns: Nothing'''

  print 'New game.'
  secret_code = make_random_code()
  moves = 1
  while (True):
    guess_code = raw_input('Enter your guess: ')
    result = compare_codes(secret_code, guess_code)
    print 'Result: %s' % (result)
    if result == 'bbbb':
      print '''Congratulations! You cracked the code
      in %d moves!''' % (moves)
      break
    moves += 1
  exit()




