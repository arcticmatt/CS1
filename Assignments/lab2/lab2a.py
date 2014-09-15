# Matt Lim
#Ex B.1:
def complement(dna_string):
  '''Does: Returns complement of a DNA sequence
  Arguments: String argument represents DNA sequence
  Returns: Returns string that represents the DNA complement'''

  dna_complement = ''
  for x in dna_string:
    if x == 'A':
      dna_complement += 'T'
    elif x == 'T':
      dna_complement += 'A'
    elif x == 'G':
      dna_complement += 'C'
    elif x == 'C':
      dna_complement += 'G'
  return dna_complement

#Ex B.2:
def list_complement(dna_list):
  '''Does: Returns complement of a DNA sequence
  Arguments: List argument represents DNA sequence
  Returns: Nothing'''

  for (i, e) in enumerate(dna_list):
    if e == 'A':
      dna_list[i] = 'T'
    elif e == 'T':
      dna_list[i] = 'A'
    elif e == 'G':
      dna_list[i] = 'C'
    elif e == 'C':
      dna_list[i] = 'G'

#Ex B.3:
def product(num_list):
  '''Does: Calculates products of a list of numbers
  Arguments: A list whose product will be calculated
  Returns: An int that is the product'''

  product = 1;
  for num in num_list:
    product *= num
  return product

#Ex B.4:
def factorial(fact_int):
  '''Does: Calculates factorial of an int
  Arguments: Int whose factorial will be calculated
  Returns: Int that is the factorial'''

  return product(range(1, fact_int + 1))

#Ex B.5:
import random
def dice(m, n):
  '''Does: Calculates sum of n rolls of an m-sided dice
  Arguments: m is the sidedness of the dice, n is the number
  of rolls
  Returns: The sum of all the rolls'''

  die_sum = 0;
  for x in range(n):
    die_sum += random.choice(range(1, m + 1))
  return die_sum

#Ex B.6:
def remove_all(mylist, int_remove):
  '''Does: Removes all of one value from a list
  Arguments: mylist is the list from which the value is removed,
  int_remove is the value to be removed
  Returns: Nothing'''

  while mylist.count(int_remove) > 0:
    mylist.remove(int_remove)

#Ex B.7:
def remove_all2(mylist, int_remove):
  '''Does: Removes all of one value from a list
  Arguments: mylist is the list from which the value is removed,
  int_remove is the value to be removed
  Returns: Nothing'''

  count = mylist.count(int_remove)
  for x in range(count):
    mylist.remove(int_remove)

def remove_all3(mylist, int_remove):
  '''Does: Removes all of one value from a list
  Arguments: mylist is the list from which the value is removed,
  int_remove is the value to be removed
  Returns: Nothing'''

  while int_remove in mylist:
    mylist.remove(int_remove)

#Ex B.8:
def any_in(list1, list2):
  '''Does: Determines if any elements of one list
  are equal to any elements of a second one
  Arguments: Two lists to be compared
  Returns: A boolean that tells whether or not any common elements
  were found'''

  for x in list1:
    if x in list2:
      return True
  return False

#Ex C.1.a:
# The problem is that a is being assigned to 0, instead of
# being tested to see if it equals 0. Fix it by using ==.
#if a == 0:
  #print 'a is zero!'

#Ex C.1.b:
# Using single quotes in the arguments creates a syntax error.
# This problem can be fixed by not using single quotes
def add_suffix(s):
  return s + '-Caltech'

#Ex C.1.c:
# The problem is that 's' will not be the string equivalent
# of s. It will just be the string 's'. To fix it,
# get rid of the single quotes
def add_suffix(s):
  return s + '-Caltech'

#Ex C.1.d:
# The problem is that you cannot
# concatenate a list and a string. To fix this
# use the append method.
lst = ['foo', 'bar', 'baz']
lst.append('bam')

#Ex C.1.e:
# The problem is that lst.reverse() doesn't return
# anything so when you run append(0) on lst2
# you get an error ('NoneType' object has no attribute 'append)
# Fix this by not returning anything, because the list has now
# been changed and no return is needed
def reverse_and_append_zero(lst):
  lst.reverse()
  lst.append(0)

#Ex C.1.f:
# The problem is that list and str are types,
# so you cannot perform operations with them.
# To fix this problem, use different argument names
def append_string_letters_to_list(mylist, mystr):
  letters = list(mystr)
  mylist.append(letters)

#Ex C.2:
# It prints 30 and not 50 because c gets assigned
# to b + a before a gets changed to 30. Thus,
# c = 10 + 20 instead of c = 20 + 30

#Ex C.3:
# The first one would work because add_and_double_1
# returns an integer value, which gets multiplied by 2.
# The second one does not work because add_and_double_2
# does not return anything, so 2 is not being multiplied
# by anything. Basically, printing a result simply shows
# the result, and doesn't let you do anything with it; returning
# a result does.

#Ex C.4:
# The first one would work because the sum_of_squares_1
# actually takes two arguments and returns the sum of their
# squares. The second one would not work because
# the method does not take any parameters.
# The difference is that passing a value as an argument does not
# not require any user input while getting it interactively does.

#Ex C.5:
# This function won't work because strings do not support item
# assignment. This is because strings are immutable.

#Ex C.6:
# This function does not work because
# one must double lst[x], where x is the index
# of the element one wants to double. Doubling
# item does nothing to the list.
