'''
MinesweeperGUI.py: a graphical minesweeper game.
'''


from Tkinter import *
import random, sys
import tkFont
import tkMessageBox
import final

class MinesweeperGUI:
    '''
    Instances of this class provide a graphical user interface
    for the 'minesweeper' game.
    '''

    def __init__(self, nrows, ncols, nbombs):
        self.game = final.Minesweeper(nrows, ncols, nbombs)
        self.nrows = nrows
        self.ncols = ncols
        self.root = Tk()
        self.root.title('Minesweeper')
        self.font = tkFont.Font(name = 'Helvetica', size = 24)
        self.bgColor = 'skyblue'
        maxsize = 10000  # ugly hack to allow large boards
        self.frame = Frame(self.root, width = maxsize , height = maxsize)
        self.frame.pack()
        self.makeLabels()
        self.done = False

    def makeLabels(self):
        '''Make a grid of labels representing game squares.'''
        self.label = []
        for r in range (self.nrows):
            self.label.append([])
            # now buttons[row] is the empty list
            for c in range(self.ncols):
                label = Label(self.frame, text=' ', width=3, relief=RAISED,
                              font=self.font, fg='red')
                label.bind('<Button-1>', self.make_click_function1(r, c))
                label.bind('<Button-2>', self.make_click_function2(r, c))
                label.grid(row = r, column = c)
                self.label[r].append(label)

    def make_click_function1(self, r, c):
        '''
        Make a callback function for the board position at 
        row = r, column = c.  Left-clicking on this position
        calls "show" on the board at that location.
        '''
        def click(event):
            try:
                self.game.show(r, c)
                self.update()
            except final.MinesweeperMoveError as e:
                tkMessageBox.showinfo('ERROR', str(e))
        return click

    def make_click_function2(self, r, c):
        '''
        Make a callback function for the board position at 
        row = r, column = c.  Right-clicking on this position
        calls "toggleFlag" on the board at that location.
        '''
        def click(event):
            try:
                self.game.toggleFlag(r, c)
                self.update()
            except final.MinesweeperMoveError as e:
                tkMessageBox.showinfo('ERROR', str(e))
        return click

    def update(self):
        '''
        Update the state of all labels based on the game state.
        '''
        for r in range(self.nrows):
            for c in range(self.ncols):
                state = self.game.state[r][c]
                count = self.game.count[r][c]
                label = self.label[r][c]
                if state == 'H':
                    label['relief'] = RAISED
                    label['text'] = ''
                elif state == 'F':
                    label['relief'] = RAISED
                    label['text'] = 'F'
                else:
                    label['relief'] = SUNKEN
                    label['bg'] = self.bgColor
                    assert state == 'V'
                    if count == 0:
                        label['text'] = ''
                    elif count == -1:  # bomb
                        label['text'] = 'B'
                    else:
                        label['text'] = str(count)
    
    def showAll(self):
        self.game.showAll()
        self.update()

    def lose(self):
        self.showAll()
        tkMessageBox.showinfo('FAILURE', 'YOU LOSE!\n\nSorry, you hit a bomb.')
        self.done = True

    def win(self):
        self.showAll()
        tkMessageBox.showinfo('SUCCESS', 'YOU WIN!')
        self.done = True

if __name__ == '__main__':
    try:
        nrows  = int(sys.argv[1])
        ncols  = int(sys.argv[2])
        nbombs = int(sys.argv[3])
        if nrows < 5 or ncols < 5 or nbombs < 1:
            raise ValueError()  # no error message because it's caught below
        m = MinesweeperGUI(nrows, ncols, nbombs)
        while not m.done:
            try:
                m.root.update()
                if m.game.isLoss():
                    m.lose()
                    m.done = True
                elif m.game.isWin():
                    m.win()
                    m.done = True
            except final.MinesweeperMoveError as e:
                tkMessageBox.showinfo('ERROR', str(e))
    except IndexError:
        print >> sys.stderr, 'usage: python MinesweeperGUI.py nrows ncols nbombs'
        sys.exit(1)
    except ValueError:
        print >> sys.stderr, 'usage: python MinesweeperGUI.py nrows ncols nbombs'
        print >> sys.stderr, '  (nrows, ncols must be integers >= 5)'
        print >> sys.stderr, '  (nbombs must be an integers >= 1)'
        sys.exit(1)

