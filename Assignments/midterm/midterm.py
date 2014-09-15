# Name: Matt Lim
# CMS cluster login name: mlim
import random

# Problem 1.1
# 1. Multi-line string is enclosed in single quotes instead of triple.
# 2. Uses == for assignment instead of =
# 3. Needs to say "and line[0] <= 'Z'" instead of "and <= 'Z'"
# 4. Strings do not have the append method, so caps.append(line)
#    and uncaps.append(line) will not work.
# 5. line[0] is not valid syntax if line is a string or a character. In this
#    case, line should be a string, but is actually a character.

# Problem 1.2
# Errors with compute_stats
# 1. In the while loop, numbers gets reset every time through, so it will
#    always be empty.
# 2. In the while loop when a 0 is entered, return is used instead of break.
#    So the function will exit early and the desired values won't be returned.
# 3. The function doesn't return the values, and instead incorrectly tries to
#    print them.
# 4. The standard deviation is not correctly calculated.
# Errors with test_stats
# 5. Passes arguments to a function stats which doesn't exist.

# Problem 1.3
# 1. Docstring is not grammatically correct
# 2. Docstring is not a full sentence.
# 3. Bad operator spacing
# 4. Uninformative variable names.
# 5. Inconsistent indentation



# Problem 2.1
def cube_root(x, tolerance):
    '''Does: Computes the cube root of a number to a particular
    tolerance using Newton's method.
    Arguments:
    -- x: The number to find the cube root of.
    -- tolerance: The precision of the computed square root.
    Returns: The cube root, to a certain precision.'''

    assert (x > 0 and tolerance > 0)
    guess = 1.0
    while abs(x - guess**3) > tolerance:
        print guess
        guess = guess + (x - guess**3) / (3*guess**2)
    return guess

# Problem 2.2
def print_squares(n):
    '''Does: Prints a square-shaped pattern of asterisks and spaces
    that is a 2x2 grid of hollow squares, with sides of n asterisks long.
    Arguments:
    -- n: The number of asterisks on each side of the square.
    Returns: Void.'''

    assert (n > 4 and n % 2 != 0)
    asterisks = '*' * n
    others = '*' + ((n - 3) / 2) * ' ' + '*' + \
            ((n-3) / 2) * ' ' + '*'
    print asterisks
    for i in range((n - 3) / 2):
        print others
    print asterisks
    for i in range((n - 3) / 2):
        print others
    print asterisks

# Problem 2.3
def pi_approx(n):
    '''Does: Approximates the mathematical constant pi. Does this
    by generating n number of random coordinate pairs (x, y) where
    both x and y are between 0 and 1. It then counts how many
    of these coordinate pairs fall inside a circle of radius 1
    with center (0, 0). The ratio of pairs in the circle to total pairs
    multiplied by 4 is an estimate of pi.
    Arguments:
    -- n: The number of coordinates to randomly generate.
    Returns: Returns an approximation of pi.'''

    total = 0
    in_circle = 0

    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            in_circle += 1
        total += 1

    return in_circle / float(total) * 4

def pi_sequence(k):
    '''Does: Prints out approximations to pi by calling
    pi_approx (k+1) times with n equal to 1, 10, 100, ... 10**k.
    Arguments:
    -- k: The maximum power of 10 to use as an argument to pi_approx.
    Returns: Void.'''

    for i in range(k + 1):
        pi = pi_approx(10**i)
        print ('%10d\t%g' % (10**i, pi))



# Problem 3.1
buzz_phrases = \
  [('integrated',    'management',        'options'),
   ('total',         'organizational',    'flexibility'),
   ('systematized',  'monitored',         'capabilities'),
   ('parallel',      'reciprocal',        'mobility'),
   ('functional',    'digital',           'programming'),
   ('responsive',    'logistical',        'concepts'),
   ('optimal',       'transitional',      'time-phase'),
   ('synchronized',  'incremental',       'projections'),
   ('compatible',    'third-generation',  'hardware'),
   ('balanced',      'policy',            'contingencies')]
def buzz():
    '''Does: Generates a random 3-word buzz phrase, choosing one
    word randomly from each column.
    Arguments: None.
    Returns: The random buzz phrase.'''

    buzz_list = []
    for i in range(3):
        buzz_list.append(buzz_phrases[random.randint(0, 9)][i])
    buzz = ' '.join(buzz_list)
    return buzz

# Problem 3.2
def split_name(name):
    '''Does: Splits a name into two parts, according to the rules
    of the name game.
    Arguments:
    -- name: The name to be split.
    Returns: A tuple of the split names.'''

    vowels = 'aeiouAEIOU'
    index = 0
    for char in name:
        if char not in vowels:
            index += 1
        else:
            break
    return (name[:index], name[index:].lower())

def name_game(name):
    '''Does: Outputs 'The Name Game' with a given name.
    Arguments:
    -- name: The string of the name to be inserted into the song.
    Returns: Void.'''

    first, last = split_name(name)

    b_last = 'B' + last
    f_last = 'F' + last
    m_last = 'M' + last

    if first == 'B':
        b_last = last[:1].upper() + last[1:]
    if first == 'F':
        f_last = last[:1].upper() + last[1:]
    if first == 'M':
        m_last = last[:1].upper() + last[1:]

    print('%s, %s, bo-%s\n' % (name, name, b_last))
    print('Bo-nana-fana fo-%s\n' % (f_last))
    print('Fee fi mo-%s\n' % (m_last))
    print('%s!\n' % (name))

# Problem 3.3
def hangman(word, max_guesses):
    '''Does: Plays a game of hangman.
    Arguments:
    -- word: A string of the word to be guessed.
    -- max_guesses: The max number of guesses.
    Returns: Void.'''

    wrong_guesses = 0
    wrong_characters = ''
    hidden_list = []
    for i in range(len(word)):
        hidden_list.append('-')

    while wrong_guesses <= max_guesses:
        guess = raw_input('Enter a character: ')
        if guess >= 'a' and guess <= 'z':
            if guess in word:
                for (i, char) in enumerate(word):
                    if char == guess:
                        hidden_list[i] = guess
            else:
                wrong_guesses += 1
                wrong_characters += guess
            current_string = ''.join(hidden_list)
            print('\nGuess: %s\n' % (current_string))
            print('Number wrong: %d\n' %(wrong_guesses))
            print('Wrong characters: %s\n' % (wrong_characters))
            if current_string == word:
                print('You win. Gratz\n')
                return
        else:
            print('Please enter a lower-case alphabetic ' \
                'character between a and z\n')

    print('You lose. The word was %s\n' % (word))



# Problem 4.1
def roman_to_decimal(roman):
    '''Does: Takes a roman numeral and converts it to its
    corresponding decimal number.
    Arguments: A string that is a valid roman numeral.
    Returns: An integer that is the roman numeral in decimal format.'''

    roman_dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, \
            'D' : 500, 'M' : 1000, 'IV' : 4, 'IX' : 9, 'XL' : 40, \
            'XC' : 100, 'CD' : 400, 'CM' : 900}
    count = 0
    decimal = 0
    while count < len(roman):
        next_one = roman[count:count + 1]
        if count < len(roman) - 1:
            next_two = roman[count:count + 2]
            if roman[count:count+2] in roman_dict:
                decimal += roman_dict[next_two]
                count += 2
            else:
                decimal += roman_dict[next_one]
                count += 1
        else:
            decimal += roman_dict[next_one]
            count += 1

    return decimal

# Problem 4.2
def invert(my_dict):
    '''Does: Inverts a dictionary (flips the key/value pairs).
    If values are repeated, the keys corresponding to these values
    will be put in a list (as will all other keys).
    Arguments:
    -- my_dict: The dictionary to be inverted.
    Returns: Returns the inverted dictionary.'''

    new_dict = {}
    keys = my_dict.keys()
    vals = my_dict.values()
    used_vals = []

    for (i, val) in enumerate(vals):
        if val not in used_vals:
            new_vals = []
            for key in keys:
                if my_dict[key] == val:
                    new_vals.append(key)
            new_dict[val] = new_vals
            used_vals.append(val)

    return new_dict

# Problem 4.3
def hangman_from_file(file_name, length, max_guesses):
    '''Does: Gets a random word that is lower-case, has no white space,
    and is of length length, and plays hangman with it.
    Arguments:
    -- file_name: The name of the file to be read for the random word.
    -- length: The length of the word to get.
    -- max_guesses: The maximum number of guesses the user will get in hangman.
    Returns: Void.'''

    my_file = open(file_name, 'r')
    words = []
    for line in my_file:
        my_line = line.strip()
        my_line_lower = my_line.lower()
        if my_line_lower == my_line and len(my_line) == length:
            words.append(my_line)
    rand_word = random.choice(words)
    hangman(rand_word, max_guesses)
