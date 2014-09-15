# Name: Matt Lim
# CMS cluster login name: mlim

'''
Text-based minesweeper game.
Can also be plugged into a GUI version.
Reference: http://www.2flashgames.com/f/f-145.htm
'''

import random, sys

# ----------------------------------------------------------------------
# Utility functions.
# ----------------------------------------------------------------------

def createGrid(nrows, ncols, val=None):
    '''
    Create a 2-dimensional grid (a list of 'nrows' lists, each containing
    'ncols' values) where each location contains the value 'val'.
    '''

    assert nrows >= 0 and ncols >= 0
    lst = [val] * ncols
    board = []
    for i in range(nrows):
        board.append(lst[:])
    return board


def randomLocations(nrows, ncols, n):
    '''
    Return a list of 'n' distinct random board locations in a grid
    with 'nrows' rows and 'ncols' columns.
    '''

    assert nrows >= 0 and ncols >= 0 and n >= 0 \
    and n <= nrows * ncols

    rand_locs = []
    num_locs = 0
    while num_locs < n:
        rand_row = random.randint(0, nrows - 1)
        rand_col = random.randint(0, ncols - 1)
        loc = (rand_row, rand_col)
        if loc not in rand_locs:
            rand_locs.append(loc)
            num_locs += 1

    return rand_locs


def validateLocations(nrows, ncols, locations):
    '''
    Validate a list of locations.  Each location must be a 2-tuple
    of (row, column) values in the range 0 to nrows-1 (row) or
    0 to ncols-1 (column).  Raise an appropriate exception if the
    locations list is invalid in any way, with a specific error message.
    '''

    if type(locations) is not list:
        raise TypeError("Third argument must be a list")

    for loc in locations:
        if type(loc) is not tuple:
            raise TypeError("Each item in the third argument list must \
                    be a tuple")
        elif len(loc) != 2:
            raise ValueError("Each tuple must have exactly two elements")
        else:
            row, col = loc
            if type(row) is not int or type(col) is not int:
                    raise TypeError("Each item in the list must be a tuple \
                            of two integers")
            elif row < 0 or row >= nrows:
                raise ValueError("Row index out of bounds")
            elif col < 0 or col >= ncols:
                raise ValueError("Row index out of bounds")


def adjacentLocations(nrows, ncols, row, col):
    '''
    For a given location, return a list of (row, col) tuples that represent
    all the adjacent locations that are on the board.  Adjacent locations
    are next to the given location in the horizontal, vertical, or diagonal
    directions.

    Examples:
      adjacentLocations(10, 10, 0, 0)
        --> [(0, 1), (1, 0), (1, 1)]
      adjacentLocations(11, 12, 4, 4)
        --> [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]

    The exact order of the locations in the list doesn't matter.
    '''

    adj_locs = []
    for i in range(-1, 2):
        if (row + i) >= 0 and (row + i) < nrows:
            for j in range(-1 ,2):
                if i == 0 and j == 0:
                    pass
                else:
                    if (col + j) >= 0 and (col + j) < ncols:
                        adj_locs.append(((row + i), (col + j)))
    return adj_locs


def gridToString(nrows, ncols, grid, legend):
    '''
    Take a grid (list of lists) of the size of the board and convert it
    to a string ready for printing.

    The legend is a dictionary mapping grid values to one-character strings
    that will represent the grid value.

    Show the column coordinates of the board on top of the grid.
    Show the row coordinates of the board to the left of the grid.

    Example for 4x4 grid (like a Minesweeper 'state' grid);
    display visible squares as 'V', hidden unflagged squares as 'H',
    hidden flagged squares as 'F':

    >>> print gridToString(nrows, ncols, state,
                { 'V' : 'V', 'H' : 'H', 'F' : 'F' })

        0   1   2   3
      +---+---+---+---+
    0 | H | V | V | V |
      +---+---+---+---+
    1 | H | H | V | V |
      +---+---+---+---+
    2 | H | H | V | V |
      +---+---+---+---+
    3 | H | V | V | V |
      +---+---+---+---+

    Assume that the grid cannot be larger than 99x99.
    Assume that the grid contents are one-character strings.
    '''
    # Check that the legend is valid.
    for val in legend.values():
        if len(val) != 1:
            raise ValueError('invalid legend value: %s' % val)

    # Start with a blank line.
    result = '\n'

    # Next line: row indices.
    result += ' ' * 5
    for c in range(ncols):
        result += '%2s  ' % str(c)
    result += '\n'

    # Next line: grid line.
    grid_line = ' ' * 4 + '+'
    for _ in range(ncols):
        grid_line += '---+'
    grid_line += '\n'
    result += grid_line

    # Alternate row lines and grid lines.
    for r in range(nrows):
        # Row index.
        result += ' %2s |' % str(r)
        # Values in the row.
        for c in range(ncols):
            result += '%2s |' % str(legend[grid[r][c]])
        result += '\n'
        result += grid_line

    return result

# ----------------------------------------------------------------------
# Error classes.
# ----------------------------------------------------------------------

class MinesweeperMoveError(Exception):
    '''
    Instances of this class are raised when an invalid move is selected
    in a Minesweeper game.
    '''
    pass

# ----------------------------------------------------------------------
# The class representing the game.
# ----------------------------------------------------------------------

class Minesweeper:
    '''
    Implements a text-based minesweeper game.
    Also can be used as the compute engine for a GUI-based
    minesweeper game.
    '''

    def __init__(self, nrows, ncols, nbombs, bomb_locations=None):
        '''
        Initialize the minesweeper game.
        nrows:  number of rows
        ncols:  number of columns
        nbombs: number of bombs
        bomb_locations: (row, column) coordinates of bombs, or None
        '''

        if type(nrows) is not int or type(ncols) is not int \
                or type(nbombs) is not int:
            raise TypeError("Row, column, and nbombs args must be integers")
        elif nrows < 5 or ncols < 5:
            raise ValueError("Row and column args must be greater than \
                    or equal to 5")
        elif nbombs < 1:
            raise ValueError("Nbombs arg must be greater than \
                    or equal to 1")
        elif bomb_locations != None:
            validateLocations(nrows, ncols, bomb_locations)
            if nbombs != len(bomb_locations):
                raise ValueError("The length of the list of bomb locations \
                        should be the same number as nbombs")

        self.nrows = nrows
        self.ncols = ncols
        self.bombs = []
        if bomb_locations != None:
            for i in range(nbombs):
                self.bombs.append(bomb_locations[i])
        else:
            rand_locs = randomLocations(nrows, ncols, nbombs)
            for loc in rand_locs:
                self.bombs.append(loc)
        self.state = createGrid(nrows, ncols, 'H')
        self.count = createGrid(nrows, ncols, 0)
        self.computeCounts()


    def computeCounts(self):
        '''
        For each square on the grid, count the number of adjacent bombs
        and store this in the 'count' field at the correct location.
        If that square has a bomb, store the number -1 at that location.
        '''

        # This method _must_ use the adjacent_squares method to compute
        # the adjacent locations or else most of the credit will be removed.
        for loc in self.bombs:
            row, col = loc
            self.count[row][col] = -1
        for i in range(self.nrows):
            for j in range(self.ncols):
                if self.count[i][j] != - 1:
                    adj_locs = adjacentLocations(self.nrows, self.ncols, i, j)
                    for loc in adj_locs:
                        row, col = loc
                        if self.count[row][col] == -1:
                            self.count[i][j] += 1


    def show(self, row, col):
        '''
        Make a square visible unless it's flagged.
        If the square is already visible, has N adjacent bombs,
        and has N adjacent flagged squares, also make all neighboring
        squares visible unless they are flagged and contain bombs.
        Then update the board.
        Trying to show a flagged square is an error.
        '''

        assert row >= 0 and row < self.nrows \
        and col >= 0 and col < self.ncols

        state = self.state[row][col]
        shown_state = self.count[row][col]
        num_flags = 0

        if state == 'H':
            self.state[row][col] = 'V'
        elif state == 'F':
            raise MinesweeperMoveError("Cannot expose a flagged square")
        elif state == 'V':
            adj_locs = adjacentLocations(self.nrows, self.ncols, row, col)
            for loc in adj_locs:
                my_row, my_col = loc
                if self.state[my_row][my_col] == 'F':
                    num_flags += 1
            if shown_state == num_flags:
                for loc in adj_locs:
                    my_row, my_col = loc
                    if self.state[my_row][my_col] != 'F':
                        self.state[my_row][my_col] = 'V'

        self.update()


    def toggleFlag(self, row, col):
        '''
        Toggle a hidden square's flagged state.
        '''

        assert row >= 0 and row < self.nrows \
        and col >= 0 and col < self.ncols

        state = self.state[row][col]
        if state == 'H':
            self.state[row][col] = 'F'
        elif state == 'F':
            self.state[row][col] = 'H'
        else:
            raise MinesweeperMoveError("Cannot toggle flag for visible square")


    def showAll(self):
        '''
        Make all squares visible.
        '''

        for i in range(self.nrows):
            for j in range(self.ncols):
                self.state[i][j] = 'V'


    def propagate(self):
        '''
        For every visible square that has no adjacent bombs,
        make all adjacent squares that do not contain bombs visible.
        Return True if any squares changed from hidden to visible;
        otherwise return False.
        '''

        is_states_changed = False
        for i in range(self.nrows):
            for j in range(self.ncols):
                if self.state[i][j] == 'V' \
                and self.count[i][j] == 0:
                    adj_locs = adjacentLocations(self.nrows, self.ncols, \
                            i, j)
                    for loc in adj_locs:
                        row, col = loc
                        if self.state[row][col] == 'H' \
                        and self.count[row][col] != -1:
                            self.state[row][col] = 'V'
                            is_states_changed = True
        return is_states_changed


    def update(self):
        '''Continue propagating until the board stops changing.'''
        # Note that this is not the most efficient way to update the
        # board after a move, but it will be fast enough for this game.
        while self.propagate():
            pass


    def isWin(self):
        '''
        Return True if the game is over and the player has won.
        The game is won if all the hidden squares are flagged and contain bombs,
        and none of the visible squares contain bombs.
        '''

        for i in range(self.nrows):
            for j in range(self.ncols):
                state = self.state[i][j]
                count = self.count[i][j]
                if (state == 'V' and count == -1) \
                or (state == 'F' and count != -1) \
                or (state == 'H'):
                    return False
        return True


    def isLoss(self):
        '''
        Return True if the game is over and the player has lost.
        The game is lost if any of the visible squares contain bombs.
        '''

        for i in range(self.nrows):
            for j in range(self.ncols):
                if self.state[i][j] == 'V' and self.count[i][j] == -1:
                    return True
        return False

    def makeDisplayGrid(self):
        '''
        Combine the count and state grids to make a grid for display.
        Return the grid as a list of list of strings (not ints).

        Format for each element of the grid:

          Hidden unflagged squares are represented by the character 'X'.
          Hidden flagged squares are represented by the character 'F'.
          Visible bombs are represented by the character 'B'.
          Squares with no adjacent bombs are represented by the character ' '
            (a blank character).
          Squares with adjacent bombs are represented by the characters
            '1' to '8' depending on how many adjacent bombs there are to
            that location.
        '''

        grid = []
        for r in range(self.nrows):
            row = []
            for c in range(self.ncols):
                if self.state[r][c] == 'H':
                    char = 'X'
                elif self.state[r][c] == 'F':
                    char = 'F'
                # Otherwise the square is visible.
                elif (r, c) in self.bombs:
                    char = 'B'
                else:
                    count = self.count[r][c]
                    if count == 0:
                        char = ' '
                    else:
                        char = str(count)
                row.append(char)
            grid.append(row)
        return grid


    def displayCounts(self):
        '''
        Print the count grid.  For debugging.
        '''

        # A count can only be an int in the range [-1, 8].
        legend = { -1 : 'B', 0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4',
                    5 : '5', 6 : '6', 7 : '7', 8 : '8' }
        print gridToString(self.nrows, self.ncols, self.count, legend)


    def displayState(self):
        '''
        Print the visible grid.  For debugging.
        '''

        legend = { 'V' : 'V', 'H' : 'H', 'F' : 'F' }
        print gridToString(self.nrows, self.ncols, self.visible, legend)


    def display(self):
        '''
        Print the state of the board.
        '''

        legend = {}
        for char in 'XBF 12345678':
           legend[char] = char
        print gridToString(self.nrows, self.ncols,
                           self.makeDisplayGrid(), legend)


    def makeMove(self, input):
        '''
        Make a single move given a line of text as input.

        All commands must start with a letter:
        q -> quit
        s M N -> show the square at row M, column N
        f M N -> toggle the flag state of the hidden square at row M, column N

        Return 'L' if the game is a loss after this move,
        'W' if the game is a win after this move, 'O' if the game
        is ongoing after this move, or 'Q' if the game is manually quit.
        '''

        words = input.split()
        command = words[0]

        if command == 'q':
            return 'Q'

        if len(words) != 3:
            err_msg = 'invalid move; need row, column coordinates'
            raise MinesweeperMoveError(err_msg)

        row, col = words[1:]

        try:
            row = int(row)
            col = int(col)
        except ValueError:
            err_msg = 'invalid move; coordinates must be integers'
            raise MinesweeperMoveError(err_msg)

        if row < 0 or row >= self.nrows or col < 0 or col > self.ncols:
            err_msg = 'invalid move; coordinates are out of range'
            raise MinesweeperMoveError(err_msg)

        if command == 's':
            self.show(row, col)
        elif command == 'f':
            self.toggleFlag(row, col)
        else:
            err_msg = 'invalid move command: %s' % command
            raise MinesweeperMoveError(err_msg)

        if self.isLoss():
            return 'L'

        if self.isWin():
            return 'W'

        return 'O'


    def run(self):
        '''Play the game.'''

        self.display()

        while True:
            input = raw_input('minesweeper> ')
            try:
                status = self.makeMove(input)
                if status == 'W':
                    self.showAll()
                    self.display()
                    print 'Game over! All bombs found! You win!'
                    break
                elif status == 'L':
                    self.showAll()
                    self.display()
                    print 'Game over! You lose!'
                    break
                elif status == 'Q':
                    print 'Quitting...'
                    break
                else:  # ongoing
                    self.display()
            except MinesweeperMoveError as e:
                print >> sys.stderr, e


if __name__ == '__main__':
    usage = 'usage: python %s nrows ncols nbombs' % sys.argv[0]
    try:
        nrows = int(sys.argv[1])
        ncols = int(sys.argv[2])
        nbombs = int(sys.argv[3])
        m = Minesweeper(nrows, ncols, nbombs)
        m.run()
    except IndexError:
        print >> sys.stderr, usage
        sys.exit(1)
    except ValueError as e:
        print >> sys.stderr, usage
        print >> sys.stderr, e
        sys.exit(1)

