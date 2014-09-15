#Ex B.1:
import random
def random_size(lower, upper):
    '''Does: Returns a random even integer
    greater than or equal to lower and less than
    or equal to upper.
    Arguments: Non-negative even integers that are lower
    and upper bounds.
    Returns: A random even integer in between the two arguments,
    inclusive.'''

    assert(lower >= 0 and upper >= 0)
    assert(lower % 2 == 0 and upper % 2 == 0)
    assert(lower < upper)

    rand_int = random.randint(lower, upper)
    if (rand_int % 2 != 0):
        rand_int += 1

    return rand_int

#Ex B.2:
def random_position(max_x, max_y):
    '''Does: Returns a random positive pair of integers
    with each less than its respective max.
    Arguments: The max x and max y.
    Returns: A random (x,y) tuple with
    x and y non-negative and x <= xmax, y <= ymax.'''

    assert(max_x >= 0 and max_y >= 0)

    rand_x = random.randint(0, max_x)
    rand_y = random.randint(0, max_y)

    return (rand_x, rand_y)

#Ex B.3:
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

#Ex B.4:
def count_values(my_dict):
    '''Does: Counts the number of distinct values
    a dictionary contains.
    Arguments: The dictionary to count the values.
    Returns: The number of distinct values in the dictionary.'''

    my_values = my_dict.values()
    distinct_values = []

    for value in my_values:
        if value not in distinct_values:
            distinct_values.append(value)
    return len(distinct_values)

#Ex B.5:
def remove_value(my_dict, my_value):
    '''Does: Removes all key/value pairs from
    the dictionary which have the passed value.
    Arguments: The dictionary to possibly alter and
    the value to be removed.
    Returns: Void.'''

    my_values = my_dict.values()
    my_keys = my_dict.keys()
    del_keys = []

    for (i, value) in enumerate(my_values):
        if value == my_value:
            del_keys.append(my_keys[i])
    for key in del_keys:
        del my_dict[key]

#Ex B.6:
def split_dict(my_dict):
    '''Does: Splits a dictionary containing strings as keys
    into two. One has keys starting with a-m (lower or uppercase)
    and one has keys starting with n-z (lower or uppercase).
    Arguments: The dictionary to be split.
    Returns: Void'''

    # Get list of keys. Split into a-m and n-z, ignoring case.
    # Then, for each list of keys, add the key and the value to a new dict.

    my_keys = my_dict.keys()
    dict1 = {}
    dict2 = {}

    for key in my_keys:
        if key[:1].lower() <= 'm' and key[:1].lower() >= 'a':
            dict1[key] = my_dict[key]
        elif key[:1].lower() >= 'n' and key[:1].lower() <= 'z':
            dict2[key] = my_dict[key]

    return (dict1, dict2)

#Ex B.7:
def count_duplicates(my_dict):
    '''Does: Counts the number of values that appear two
    or more times in a dictionary.
    Arguments: The dictionary in question.
    Returns: The number of values that appear two or more times
    in the dictionary.'''

    my_values = my_dict.values()
    distinct_values = []
    duplicate_values = []

    for value in my_values:
        if value not in distinct_values:
            distinct_values.append(value)
        elif value not in duplicate_values:
            duplicate_values.append(value)
    return len(duplicate_values)
