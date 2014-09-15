'''
Partial test suite for Minesweeper code.
'''

import nose
from nose.tools import assert_raises
import random
from final import *

def test_createGrid():
    grid = createGrid(3, 4, 0)
    assert grid == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    grid[0][0] = 1
    assert grid == [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    grid[0][1] = 2
    grid[0][2] = 3
    grid[0][3] = 4
    grid[1][0] = 5
    grid[1][1] = 6
    grid[1][2] = 7
    grid[1][3] = 8
    grid[2][0] = 9
    grid[2][1] = 10
    grid[2][2] = 11
    grid[2][3] = 12
    assert grid == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    grid = createGrid(4, 3, 'f')
    assert grid == [['f', 'f', 'f'],
                    ['f', 'f', 'f'],
                    ['f', 'f', 'f'],
                    ['f', 'f', 'f']]
    grid[0][2] = 'o'
    assert grid == [['f', 'f', 'o'],
                    ['f', 'f', 'f'],
                    ['f', 'f', 'f'],
                    ['f', 'f', 'f']]
    grid[0][0] = 1
    grid[0][1] = 2
    grid[0][2] = 3
    grid[1][0] = 4
    grid[1][1] = 5
    grid[1][2] = 6
    grid[2][0] = 7
    grid[2][1] = 8
    grid[2][2] = 9
    grid[3][0] = 10
    grid[3][1] = 11
    grid[3][2] = 12
    assert grid == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    grid = createGrid(3, 3, None)
    assert grid == [[None, None, None], [None, None, None], [None, None, None]]
    grid[1][0] = 0
    assert grid == [[None, None, None], [0, None, None], [None, None, None]]
    grid[0][0] = 1
    grid[0][1] = 2
    grid[0][2] = 3
    grid[1][0] = 4
    grid[1][1] = 5
    grid[1][2] = 6
    grid[2][0] = 7
    grid[2][1] = 8
    grid[2][2] = 9
    assert grid == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def test_randomLocations():
    for i in range(100):
        nrows = random.randint(3, 10)
        ncols = random.randint(3, 10)
        n = random.randint(5, nrows * ncols)
        locs = randomLocations(nrows, ncols, n)
        assert len(locs) == n
        # Make sure all locations are unique.
        unique_locs = []
        for l in locs:
            (row, col) = l
            assert row >= 0
            assert col >= 0
            assert row < nrows
            assert col < ncols
            assert l not in unique_locs
            unique_locs.append(l)

def test_validateLocations():
    # Here we check not only that the correct exception
    # was raised but also that there is an argument
    # representing the error message.
    with assert_raises(TypeError) as e:
        validateLocations(5, 6, 0)
    assert len(e.exception.args) == 1
    arg = e.exception.args[0]
    assert type(arg) is str
    assert len(arg) >= 10

    with assert_raises(TypeError) as e:
        validateLocations(5, 6, [0])
    assert len(e.exception.args) == 1
    arg = e.exception.args[0]
    assert type(arg) is str
    assert len(arg) >= 10

    with assert_raises(ValueError) as e:
        validateLocations(5, 6, [(0, 0, 0)])
    assert len(e.exception.args) == 1
    arg = e.exception.args[0]
    assert type(arg) is str
    assert len(arg) >= 10

    with assert_raises(TypeError) as e:
        validateLocations(5, 6, [('foo', 0)])
    assert len(e.exception.args) == 1
    arg = e.exception.args[0]
    assert type(arg) is str
    assert len(arg) >= 10

    with assert_raises(TypeError) as e:
        validateLocations(5, 6, [(1.0, 0)])
    assert len(e.exception.args) == 1
    arg = e.exception.args[0]
    assert type(arg) is str
    assert len(arg) >= 10

    with assert_raises(ValueError) as e:
        validateLocations(5, 6, [(-1, 0)])
    assert len(e.exception.args) == 1
    arg = e.exception.args[0]
    assert type(arg) is str
    assert len(arg) >= 10

    with assert_raises(ValueError) as e:
        validateLocations(5, 6, [(5, 0)])
    assert len(e.exception.args) == 1
    arg = e.exception.args[0]
    assert type(arg) is str
    assert len(arg) >= 10

    with assert_raises(TypeError) as e:
        validateLocations(5, 6, [(0, 'foo')])
    assert len(e.exception.args) == 1
    arg = e.exception.args[0]
    assert type(arg) is str
    assert len(arg) >= 10

    with assert_raises(TypeError) as e:
        validateLocations(5, 6, [(0, 1.0)])
    assert len(e.exception.args) == 1
    arg = e.exception.args[0]
    assert type(arg) is str
    assert len(arg) >= 10

    with assert_raises(ValueError) as e:
        validateLocations(5, 6, [(0, -1)])
    assert len(e.exception.args) == 1
    arg = e.exception.args[0]
    assert type(arg) is str
    assert len(arg) >= 10

    with assert_raises(ValueError) as e:
        validateLocations(5, 6, [(0, 6)])
    assert len(e.exception.args) == 1
    arg = e.exception.args[0]
    assert type(arg) is str
    assert len(arg) >= 10

def test_adjacentLocations():
    locs1 = adjacentLocations(5, 6, 0, 0)
    assert type(locs1) is list
    assert len(locs1) == 3
    assert (0, 1) in locs1
    assert (1, 0) in locs1
    assert (1, 1) in locs1
    locs2 = adjacentLocations(6, 5, 5, 4)
    assert type(locs2) is list
    assert len(locs2) == 3
    assert (5, 3) in locs2
    assert (4, 3) in locs2
    assert (4, 4) in locs2
    locs3 = adjacentLocations(5, 5, 4, 0)
    assert type(locs3) is list
    assert len(locs3) == 3
    assert (4, 1) in locs3
    assert (3, 0) in locs3
    assert (3, 1) in locs3
    locs4 = adjacentLocations(3, 3, 0, 2)
    assert type(locs4) is list
    assert len(locs4) == 3
    assert (0, 1) in locs4
    assert (1, 1) in locs4
    assert (1, 2) in locs4
    locs5 = adjacentLocations(5, 6, 0, 3)
    assert type(locs5) is list
    assert len(locs5) == 5
    assert (0, 2) in locs5
    assert (0, 4) in locs5
    assert (1, 2) in locs5
    assert (1, 3) in locs5
    assert (1, 4) in locs5
    locs6 = adjacentLocations(5, 6, 2, 0)
    assert type(locs6) is list
    assert len(locs6) == 5
    assert (1, 0) in locs6
    assert (1, 1) in locs6
    assert (2, 1) in locs6
    assert (3, 0) in locs6
    assert (3, 1) in locs6
    locs7 = adjacentLocations(5, 6, 2, 5)
    assert type(locs7) is list
    assert len(locs7) == 5
    assert (1, 4) in locs7
    assert (1, 5) in locs7
    assert (2, 4) in locs7
    assert (3, 4) in locs7
    assert (3, 5) in locs7
    locs8 = adjacentLocations(5, 6, 4, 3)
    assert type(locs8) is list
    assert len(locs8) == 5
    assert (3, 2) in locs8
    assert (3, 3) in locs8
    assert (4, 2) in locs8
    assert (4, 4) in locs8
    assert (3, 4) in locs8
    locs9 = adjacentLocations(5, 6, 2, 2)
    assert type(locs9) is list
    assert len(locs9) == 8
    assert (1, 1) in locs9
    assert (1, 2) in locs9
    assert (1, 3) in locs9
    assert (2, 1) in locs9
    assert (2, 3) in locs9
    assert (3, 1) in locs9
    assert (3, 2) in locs9
    assert (3, 3) in locs9

if __name__ == '__main__':
    nose.runmodule()

