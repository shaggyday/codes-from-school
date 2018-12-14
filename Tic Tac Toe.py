# Harry Tian & Star Song: a Tic Tac Toe game using Zelle graphics
from graphics import *
import time
import random  
class TicTacToe:
    """Class to represent tic tac toe playable game with simple graphics """
    
    def __init__(self):
        """ No arguments, 2 instance variables are created here - 
        1. the graphics window used to display the game and get mouse clicks
        2. 3x3 list of lists to represent the actual internal game state """
        self.window = GraphWin("Tic-Tac-Toe",700,700)
        self.board = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ]
        self.winner = ""
        # set initial variables for AIblock function
        self.mode = ""
        self.blockX = int()
        self.blockY = int()
        
    def startScreen(self):
        """ draws the empty initial tic tac toe grid and some text instructions """
        # creates initial screen with options 1-player and 2-players
        onePlayer = Circle(Point(250,350),90)
        onePlayer.draw(self.window)
        twoPlayer = Circle(Point(450,350),90)
        twoPlayer.draw(self.window)
        txt1 = Text(Point(250,350), "1-player")
        txt1.setTextColor("red")
        txt1.setSize(27)
        txt1.draw(self.window)
        txt2 = Text(Point(450,350), "2-players")
        txt2.setTextColor("blue")
        txt2.setSize(27)
        txt2.draw(self.window)
        # sets play mode (self.mode) boolean for future use
        click1 = self.window.getMouse()
        if 200 <= click1.x <= 300 and 300 <= click1.y <= 400:
            onePlayer.undraw()
            twoPlayer.undraw()
            txt1.undraw()
            txt2.undraw()
            self.mode = True
        elif 400 <= click1.x <= 500 and 300 <= click1.y <= 400:
            onePlayer.undraw()
            twoPlayer.undraw()
            txt1.undraw()
            txt2.undraw()
            self.mode = False
        # creates game board
        t = Text(Point(350,25), "Click on a square to play your symbol X or O")
        t.setSize(18)
        t.setTextColor("blue")
        line1 = Line(Point(250, 50), Point(250, 650))
        line2 = Line(Point(450, 50), Point(450, 650))
        line3 = Line(Point(50, 250), Point(650, 250))
        line4 = Line(Point(50, 450), Point(650, 450))
        square1 = Rectangle(Point(50, 50), Point(650, 650))
        t.draw(self.window)
        line1.draw(self.window)
        line2.draw(self.window)
        line3.draw(self.window)
        line4.draw(self.window)
        square1.draw(self.window)
    
    def takeTurn(self, player):
        """ waits for a mouse click, then draws an X or an O centered exactly 
        at the point clicked, depending on which player's turn it is """
        #   handles invalid clicks out of the bounds of the grid and not in a currently empty square
        #   check for invalid checks and display text, wait for another click       
        if not self.mode or (self.mode and player == 1):
            click1 = self.window.getMouse()
            t = Text(Point(350,350), "Your click was INVALID!")
            t.setSize(30)
            t.setTextColor("red")
            draw = False # sets boolean so text is not drawn twice
            valid = False
            while not valid:
                if 50 <= click1.x <= 650 and 50 <= click1.y <= 650 and self.board[(click1.y-50)//200][(click1.x-50)//200] == "-":
                    valid = True
                if not valid:
                    if not draw:
                        t.draw(self.window)
                        draw = True
                    click1 = self.window.getMouse()
            if draw:
                t.undraw()
        # alternate turns between the two players
        if player == 1:
            self.xdraw(click1.x, click1.y)
        elif player == 0:
            # differentiates between 1-player and 2-players mode
            if self.mode:
                self.odraw(0,0)
            else:
                self.odraw(click1.x, click1.y)
            
    def xdraw(self, x, y):
        """ draw an x centered on the point x,y """
        # reset x,y coordinates so that its always centered in square
        gridX = (x-50)//200
        gridY = (y-50)//200
        x = gridX*200+150
        y = gridY*200+150
        # draw letter X centered in square        
        lineFive = Line(Point((x - 75), (y - 75)), Point((x + 75), (y + 75)))
        lineSix = Line(Point((x + 75), (y - 75)), Point((x - 75), (y + 75)))
        lineFive.draw(self.window)
        lineSix.draw(self.window)
        # Update the internal game board with the newly added "X" in the appropriate position
        self.board[gridY][gridX] = "X"
        return [lineFive, lineSix]

    def blockCon1(self,symbol,a,b,c,x):
        """ help function that sets boolean for conditions when AI or player has 2-in-a-row """
        if self.board[x][a] == self.board[x][b] == symbol and self.board[x][c] == "-":
            self.blockX = c
            self.blockY = x
            return True
        return False
    
    def blockCon2(self,symbol,a,b,c,x):
        """ help function that sets boolean for conditions when AI or player has 2-in-a-row """
        if self.board[a][x] == self.board[b][x] == symbol and self.board[c][x] == "-":
            self.blockX = x
            self.blockY = c
            return True
        return False

    def blockCon3(self,symbol,a,b,c,x):
        """ help function that sets boolean for conditions when AI or player has 2-in-a-row """
        if x == 1:
            if self.board[a][a] == self.board[b][b] == symbol and self.board[c][c] == '-':
                self.blockX = c
                self.blockY = c
                return True
            return False
        elif x == 2:
            if self.board[a][c] == self.board[b][b] == symbol and self.board[c][a] == '-':
                self.blockX = a
                self.blockY = c
                return True
            return False
        elif x == 3:
            if self.board[a][b] == self.board[b][a] == symbol and self.board[c][c] == '-':
                self.blockX = c
                self.blockY = c
                return True
            return False
        
    def AIblock(self,symbol):
        """ uses help function to return boolean for every 2-in-a-row condition"""
        for x in range(3):
            if self.blockCon1(symbol,2,1,0,x):
                return True
            if self.blockCon1(symbol,0,2,1,x):
                return True
            if self.blockCon1(symbol,1,0,2,x):
                return True
            if self.blockCon2(symbol,2,1,0,x):
                return True
            if self.blockCon2(symbol,0,2,1,x):
                return True
            if self.blockCon2(symbol,1,0,2,x):
                return True
        if self.blockCon3(symbol,2,1,0,1):
            return True
        if self.blockCon3(symbol,1,0,2,1):
            return True
        if self.blockCon3(symbol,0,2,1,1):
            return True
        if self.blockCon3(symbol,2,1,0,2):
            return True
        if self.blockCon3(symbol,0,1,2,2):
            return True
        if self.blockCon3(symbol,2,0,1,3):
            return True

    def odraw(self, x, y):
        """ draw an o centered on the point x,y """
        if self.mode:#odraw for 1-player mode
            AIblockX = self.AIblock("X")
            AIblockO = self.AIblock("O")
            # sets valid coordinates for AI within grid
            A = self.blockX*200+150
            B = self.blockY*200+150
            # calls AIblock function to determine if AI needs to block or not;
            # calls AIblock for "O" first and exclusive from AIblock for "X" so that
            # the win condition for "O" is prioritized before blocking "X" from winning
            if AIblockO:
                self.board[self.blockY][self.blockX] = "O"
            elif AIblockX:
                self.board[self.blockY][self.blockX] = "O"
            # if block is not needed, AI plays a random move
            else:
                valid = False
                while not valid:
                    # reset valid and random coordinates for AI to play in
                    gridA = random.randint(0,2)
                    gridB = random.randint(0,2)
                    if self.board[gridB][gridA] == "-":
                        valid = True
                A = gridA*200+150
                B = gridB*200+150
                self.board[gridB][gridA] = "O"
            circle = Circle(Point(A, B), 75)
            circle.draw(self.window)
            return [circle]
        # draw letter O centered in square
        # sets x,y coordinates so that its always centered in square
        gridX = (x-50)//200
        gridY = (y-50)//200
        x = gridX*200+150
        y = gridY*200+150
        circle = Circle(Point(x, y), 75)
        circle.draw(self.window)
        # Update the internal game board with the newly added "O" in the appropriate position
        self.board[gridY][gridX] = "O"
        return [circle]

    def drawRed(self,symbol,x,y):
        """ make winning 3 symbols red by drawing red symbols over current """
        x = x*200+150
        y = y*200+150
        if symbol == "X":
            lineFive = Line(Point((x - 75), (y - 75)), Point((x + 75), (y + 75)))
            lineSix = Line(Point((x + 75), (y - 75)), Point((x - 75), (y + 75)))
            lineFive.setOutline("red")
            lineSix.setOutline("red")
            lineFive.draw(self.window)
            lineSix.draw(self.window)            
        elif symbol == "O":
            circle = Circle(Point(x, y), 75)
            circle.setOutline("red")
            circle.draw(self.window)
            
    def isWon(self):
        """ currently checks each row, column, and diagonal for 3 identical symbols (other than "-")
        returns True if either player has won, False otherwise; also makes winning 3 symbols red """
        rows = 0
        for row in self.board:
            if row[0] != "-" and row[0] == row[1] == row[2]:
                if row[0] == "X":
                    # update self.winner to be the appropriate symbol X or O for who won; repeat for all win conditions
                    self.winner = "X"
                    for i in range(3):
                        self.drawRed("X",i,rows)
                    return True
                elif row[0] == "O":
                    self.winner = "O"
                    for i in range(3):
                        self.drawRed("O",i,rows)
                    return True
            rows += 1
        for x in range(3):
            if self.board[0][x] == self.board[1][x] == self.board[2][x] and self.board[0][x] != "-":
                if self.board[0][x] == "X":
                    self.winner = "X"
                    for i in range(3):
                        self.drawRed("X",x,i)
                    return True
                elif self.board[0][x] == "O":
                    self.winner = "O"
                    for i in range(3):
                        self.drawRed("O",x,i)
                    return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "-":
            if self.board[0][0] == "X":
                self.winner = "X"
                for i in range(3):
                    self.drawRed("X",i,i)
                return True
            elif self.board[0][0] == "O":
                self.winner = "O"
                for i in range(3):
                    self.drawRed("O",i,i)
                return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != "-":
            if self.board[0][2] == "X":
                self.winner = "X"
                for i in range(3):
                    self.drawRed("X",i,2-i)
                return True
            elif self.board[0][2] == "O":
                self.winner = "O"
                for i in range(3):
                    self.drawRed("O",i,2-i)
                return True
        return False
    
    def gameOver(self):
        """ displays text declaring winner (or draw) and waits for user to click to close window """
        if self.winner == "X":
            t = Text(Point(350,350), "X WON!")
        elif self.winner == "O":
            t = Text(Point(350,350), "O WON!")
        else:
            t = Text(Point(350,350), "DRAW!")
        t.setSize(35)
        t.setTextColor("red")
        t.draw(self.window)
        while self.window.winfo_exists():
            self.window.update()
         
def main():
    """ finished working code to play one game of graphical tic-tac-toe """
    tttGame = TicTacToe()
    tttGame.startScreen()
    curTurn = 1
    while not tttGame.isWon() and curTurn <= 9:
        tttGame.takeTurn(curTurn % 2)
        curTurn += 1
    tttGame.gameOver()
        
if __name__ == "__main__":
    main()
