'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku. Adding this.'''

    def __init__(self):
        '''Does: Initializes a board full of zeroes and an
        empty list representing its moves.
        Arguments:
        -- self.
        Returns: Void.'''

        lst = [0] * 9
        board = []
        for i in range(9):
            board.append(lst[:])
        self.board = board
        self.moves = []


    def load(self, filename):
        '''Does: Loads a valid file onto the board.
        Arguments:
        -- filename: A String representing the file name.
        Returns: Void.'''

        my_file = open(filename, 'r')
        board = []
        num_lines = 0
        valid_chars = '0123456789'
        for line in my_file:    # Loop through lines of file
            num_columns = 0
            num_lines += 1
            row = []
            for char in line:   # Loop through chars of line
                num_columns += 1
                if char != '\n' and char in valid_chars:
                    row.append(int(char))
                elif char not in valid_chars and num_columns < 10:
                    my_file.close()
                    raise IOError('Lines must contain digits from 0-9 only')
            # Make sure there are only 9 numbers and 1 new line character
            if num_columns != 10:
                my_file.close()
                raise IOError('Lines must be 9 characters or less, \
                        not including the new-line character')
            board.append(row)

        if num_lines != 9:
            my_file.close()
            raise IOError('File must have exactly 9 lines')
        self.board = board
        my_file.close()


    def save(self, filename):
        '''Does: Saves a board state as a valid file.
        Arguments:
        -- filename: A string representing the name of the newly saved file.
        Returns: Void.'''

        my_file = open(filename, 'w')
        board = self.board
        for row in board:
            for num in row:
                my_file.write(str(num))
            my_file.write('\n')
        my_file.close()


    def show(self):
        '''Does: Prints a board prettily.
        Arguments:
        -- self.
        Returns: Void.'''

        print
        print '   1 2 3 4 5 6 7 8 9 '
        for i in range(9):
            if i % 3 == 0:
                print '  +-----+-----+-----+'
            sys.stdout.write('%d |' % (i + 1))
            for j in range(9):
                if self.board[i][j] == 0:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('%d' % self.board[i][j])
                if j % 3 != 2 :
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('|')
            print
        print '  +-----+-----+-----+'
        print

    def move(self, row, col, val):
        '''Does: Makes a valid move. Raises an error if not a valid move.
        Arguments:
        -- row: Integer representing the row of the move.
        -- col: Integer representing the column of the move.
        -- val: Integer representing the value to input.
        Returns: Void'''

        board = self.board
        moves = self.moves
        box_rows = []
        box_columns = []

        if row in range(3):
            box_rows = range(3)
        elif row in range(3, 6):
            box_rows = range(3, 6)
        elif row in range(6, 9):
            box_rows = range(6, 9)

        if col in range(3):
            box_columns = range(3)
        elif col in range(3, 6):
            box_columns = range(3, 6)
        elif col in range(6, 9):
            box_columns = range(6, 9)

        for char in board[row]:
            if char == val:
                raise SudokuMoveError('Row already \
                        contains that value')
        for line in board:
            if line[col] == val:
                raise SudokuMoveError('Column already \
                        contains that value')
        for my_row in box_rows:
            for my_col in box_columns:
                if board[my_row][my_col] == val:
                    raise SudokuMoveError('Box already \
                            contains that value')

        if board[row][col] == 0:
            pass
        else:
            raise SudokuMoveError('Not a valid move, spot already filled')

        board[row][col] = val
        moves.append((row, col, val))


    def undo(self):
        '''Does: Undoes the latest move on the board and removes it
        from the moves list.
        Arguments:
        -- self.
        Returns: Void.'''

        board = self.board
        moves = self.moves
        move_info = moves.pop()
        row, col, val = move_info
        board[row][col] = 0


    def solve(self):
        '''Does: Runs an infinite loop handling user interaction.
        Takes care of moves, quitting, undoing, and saving, printing the board
        after each command.
        Arguments:
        -- self.
        Returns: Void.'''

        while True:
            try:
                cmd = raw_input('Enter a command: ')
                if cmd == 'q':
                    return
                elif cmd.isdigit() and len(cmd) == 3:
                    self.move(int(cmd[0]) - 1, int(cmd[1]) - 1, int(cmd[2]))
                elif cmd == 'u':
                    self.undo()
                elif len(cmd) > 1 and cmd[0] == 's' \
                        and cmd[1] == ' ':
                    self.save(cmd[2:])
                else:
                    raise SudokuCommandError('Bad command: %s' % cmd)
                self.show()
            except SudokuCommandError, e:
                print e
                print >> sys.stderr, 'Please enter a valid command'
            except SudokuMoveError, e:
                print e
                print >> sys.stderr, 'Please enter a valid move'


if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = raw_input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except IOError, e:
            print e

    s.show()
    s.solve()

