def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        val1 = dict[key1]
    except KeyError, e:
        print e
        return

    try:
        val2 = dict[key2]
    except KeyError, e:
        print e
        return

    return val1 + val2
