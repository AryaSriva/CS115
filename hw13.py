class Board(object):

    def __init__(self, width = 7, height = 6):
        self.width = width
        self.height = height
        self.arr = []
        for j in range(height):
            row = []
            for i in range(width):
                row += [' ']
            self.arr += [row] 

    def __str__(self):
        s = ""
        for j in range(self.height):
            for i in range(self.width):
              s += " |" + self.arr[j][i] + "| "
            s += "\n"
        s += "\n"
        for i in range(self.width):
            s += "-"
        return s

    def allowsMove(self, col):
        '''checks if a checker can be placed in a given column in the Board'''
        if col > self.width or col < 0:
            return False
        board = self.arr
        for j in range(0, self.height):
            print(board[col][j])
            if " " in board[col][j]:
                return True
        return False

    def addMove(self, col, ox):
        '''adds an ox, where ox is a "X" or an "O" in the given column col'''
        if self.allowsMove(col):
            for row in range(self.height - 1, -1):
                if " " == self.arr[col][row]:
                    self.arr[col][row] = ox

    def setBoard( self, moveString ): 
        """ takes in a string of columns and places 
            alternating checkers in those columns, 
            starting with 'X' 
             
            For example, call b.setBoard('012345') 
            to see 'X's and 'O's alternate on the 
            bottom row, or b.setBoard('000000') to 
            see them alternate in the left column. 
 
            moveString must be a string of integers 
        """ 
        nextCh = 'X'   # start by playing 'X' 
        for colString in moveString: 
            col = int(colString) 
            if 0 <= col <= self.width: 
                self.addMove(col, nextCh) 
            if nextCh == 'X': nextCh = 'O' 
            else: nextCh = 'X'

    def winsFor(self, ox):
        board = self.arr
        for j in range(3, self.height - 3):
            for i in range(3, self.width - 3):
                if board[i-3][j] == ox and board[i-2][j] == ox and board[i-1][j] == ox and board[i][j] == ox:
                    return True
                elif board[i+3][j] == ox and board[i+2][j] == ox and board[i+1][j] == ox and board[i][j] == ox:
                    return True
                elif board[i][j-3] == ox and board[i][j-2] == ox and board[i][j-1] == ox and board[i][j] == ox:
                    return True
                elif board[i][j+3] == ox and board[i][j+2] == ox and board[i][j+1] == ox and board[i][j] == ox:
                    return True
                elif board[i+1][j-1] == ox and board[i+2][j-2] == ox and board[i+3][j-3] == ox and board[i][j] == ox:
                    return True
                elif board[i-1][j+1] == ox and board[i-2][j+2] == ox and board[i-3][j+3] == ox and board[i][j] == ox:
                    return True
                

    def hostGame(self):
        '''runs a loop allowing users to play the game until one player wins'''
        print("Welcome to Connect Four!")
        print(self.__str__())
        i = 0 
        while not self.winsFor("X") and not self.winsFor("O"):
            if i % 2 == 0:
                ox = "X"
            else:
                ox = "O"
            choice = int(input(ox+ "'s choice: "))
            if self.allowsMove(choice):
                self.addMove(choice, ox)
                print(self.__str__())
            else:
                print("Woops that's not a valid column!")
            
            
board = Board()
board.setBoard("012345")
print(board.__str__())
            
            
