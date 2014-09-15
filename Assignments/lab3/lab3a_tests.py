# lab3a_tests.py

import nose
from lab3a import *

def test_list_reverse():
    assert list_reverse([21, 33, 42, 67, 99]) == [99, 67, 42, 33, 21]
    assert list_reverse([]) == []
    assert list_reverse([1]) == [1]

def test_list_reverse2():
    assert list_reverse2([21, 33, 42, 67, 99]) == [99, 67, 42, 33, 21]
    assert list_reverse2([]) == []
    assert list_reverse2([1]) == [1]

def test_file_info():
    assert file_info('hamlet.txt') == (7996, 32006, 197341)
    assert file_info('macbeth.txt') == (4825, 18092, 113675)

def test_file_info2():
    assert file_info2('hamlet.txt') == \
      { 'lines' : 7996, 'words' : 32006, 'characters' : 197341 }
    assert file_info2('macbeth.txt') == \
      { 'lines' : 4825, 'words' : 18092, 'characters' : 113675 }

def test_longest_line():
    ll1 = '    /Enter KING CLAUDIUS, QUEEN GERTRUDE, ROSENCRANTZ, and GUILDENSTERN/ \n'
    ll2 = "    /Exit LADY MACDUFF, crying 'Murder!' Exeunt Murderers, following her/ \n"
    assert longest_line('hamlet.txt')  == (74, ll1)
    assert longest_line('macbeth.txt') == (75, ll2)

def test_sort_words():
    assert sort_words('') == []
    assert sort_words('foo bar baz') == ['bar', 'baz', 'foo']

if __name__ == '__main__':
    nose.runmodule()



