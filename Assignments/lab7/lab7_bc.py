# Ex B.1
def mySum(*nums):
    '''Does: Sums an arbitrary number of integers that are greater
    than zero.
    Arguments:
    -- nums: An arbitrary number of arguments, which should all be
    integers greater than zero.
    Returns: The sum.'''


    sum = 0
    for num in nums:
        if type(num) is not int:
            raise TypeError('Arguments must be integers')
        elif num <= 0:
            raise ValueError('Arguments must be greater than 0')
        else:
            sum += num
    return sum


# Ex B.2
def myNewSum(*nums):
    '''Does: Sums an arbitrary number of integers that are greater
    than zero, OR sums a list of integers.
    Arguments:
    -- nums: An arbitrary number of arguments, which should all be
    integers greater than zero, EXOR one list of integers.
    Returns: The sum.'''

    sum = 0
    my_nums = nums
    if len(nums) > 1 and type(nums[0]) is list:
        raise TypeError('Cannot have both a list argument \
            and individual number arguments, or two list arguments')
    elif len(nums) > 0 and type(nums[0]) is list:
        my_nums = nums[0]

    for num in my_nums:
        if type(num) is not int:
            raise TypeError('Arguments must be integers or a list of \
                    integers')
        elif num <= 0:
            raise ValueError('All numbers must be greater than 0')
        else:
            sum += num
    return sum


# Ex B.3
import operator
def myOpReduce(lst, **op):
    '''Does: Either calculates the sum, multiple, or max of a list
    of integers, depending on the keyword argument.
    Arguments:
    -- lst: A list of what should be integers.
    -- op: The keyword argument that can be either '+', '*', or 'max'.
    Returns: The calculation.'''

    if len(op) > 0:
        kw = op[op.keys()[0]]

    if len(op) != 1:
        raise ValueError('Value Error RAISED: Must have one and only one keyword arg');
    elif op.keys()[0] != 'op':
         raise ValueError()
    elif type(kw) is not str:
        raise TypeError('Keyword arg must be a string')

    if kw == '+':
        return sum(lst)
    elif kw == '*':
        multiple = 1
        for num in lst:
            multiple *= num
        return multiple
    elif kw == 'max':
        if len(lst) == 0:
            return 0
        return max(lst)
    else:
        raise ValueError('Keyword must be \'+\', \'*\', or \'max\'')


# Ex C.1
# One problem is that when an error is raised, quit() is run. This is a bit
# too extreme, as it would make more sense to simply raise an error and
# continue on. Another
# problem is that the try/except blocks should be written in the function
# that calls sum_of_key_values, because it is that function that is responsible
# if the keys are not in the dictionary. This is the problem I will fix below.
import sys
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at
    key1 and key2.'''
    return dict[key1] + dict[key2]


# Ex C.2
# One problem is that the try/except blocks should be written in the function
# that calls sum_of_key_values, because it is that function that is responsible
# if the keys are not in the dictionary. This is the problem I will fix below.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at
    key1 and key2.'''
    return dict[key1] + dict[key2]


# Ex C.3
# The main problem here is that the program raises a KeyError in an except
# block that excepts KeyErrors. Another problem is the aforementioned problem
# of writing the try/except block in a function that calls sum_of_key_values.
# The solution below fixes both issues.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at
    key1 and key2.'''
    return dict[key1] + dict[key2]


# Ex C.4
# One problem is that having two try/except blocks is unnecessary, as one
# could combine them into one with the same functionality. Another
# problem is that errors are raised in except blocks.
# Another problem is the aforementioned problem
# of writing the try/except block in a function that calls sum_of_key_values.
# The solution below fixes all these issues.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at
    key1 and key2.'''
    return dict[key1] + dict[key2]


# Ex C.5
# One problem here is that the print statement will not execute,
# because an exception is raised on the line before it.
# Also, the print statement here is not good practice, so to fix
# this code I will just get rid of it and only raise a ValueError.
def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)


# Ex C.6
# One problem here is that instead of printing an error message
# and raising an exception separately, the error message should be put
# as an attribute of ValueError, then printed in the function that calls
# fib.
def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)


# Ex C.7
# The problem here is that a ValueError should be raised
# instead of a TypeError.
from math import exp
def exp_x_over_x(x):
    '''Return the value of e**x / x, for x > 0 and
    e = 2.71828... (base of natural logarithms).'''
    if x < 0:
        raise ValueError('x must be >= 0.0')
    return (exp(x) / x)


# Ex C.8
# The problem here is that Exception is too broad. More specific
# exceptions should be used.
def exp_x_over_x(x):
    '''Return the value of e**x / x, for x > 0 and
    e = 2.71828... (base of natural logarithms).'''
    if type(x) is not float:
        raise TypeError('x must be a float')
    elif x <= 0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)
