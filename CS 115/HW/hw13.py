'''
Created on 12/05/19
@author:   Jonathan Joshua
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System." - Jonathan Joshua

CS115 - Hw 13 - Connect 4
'''
import sys
class Board(object):
    def __init__(self, width =7, height=6):
        """a constructor for Board objects that (in addition to self) takes two named arguments, one for the number of height and one for thenumber of columns."""
        self.width = width 
        self.height = height
        self.theboard = [[' ' for _ in range(width)] for _ in range(height)]

    def __str__(self):
        """returns a string (it does not print a string) representingthe Board object that calls it."""
        A= ''
        for r in range(int(self.height)):
            for c in range(int(self.width)):
                if c == int(self.width)-1:
                    A += '|' + self.theboard[r][c] +'|\n'
                else:
                    A += '|' + self.theboard[r][c]
        A += self.width * '--' +'\n'
        for i in range(int(self.width)):
            A += ' ' + str(i)
        return A 
     
    def allowsMove(self,col):
        """should return True if the calling Board object canallow a move into column c (because there is space available)."""
        try:
            for r in range(int(self.height)):
                if self.theboard[r][col] == ' ':
                    return True
        except:
                return False
         
    def addMove(self, col, ox):
        """should add an ox checker, where ox is a variableholding a string that is either "X" or "O", into column col."""
        x= int(self.height) -1
        if self.allowsMove(int(col)) == True:
            while self.theboard[x][col] != ' ':
                x -= 1
            if self.theboard[x][col] == ' ':
                self.theboard[x][col] = ox  
    
    def setBoard(self,move_string):
        """
        takes in a string of columns and places 
        alternating checkers in those columns, 
        starting with 'X' 
         
        For example, call b.setBoard('012345') 
        to see 'X's and 'O's alternate on the 
        bottom row, or b.setBoard('000000') to 
        see them alternate in the left column. 
 
        moveString must be a string of integers
        """
         
        nextCh = 'X'   # start by playing 'X' 
        for widthtring in move_string: 
            col = int(widthtring) 
            if 0 <= col <= self.width: 
                self.addMove(col, nextCh) 
            if nextCh == 'X': nextCh = 'O' 
            else: nextCh = 'X' 
    
    
    def delMove(self, col):
        """should do the "opposite" of addMove. That is, it shouldremove the top checker from the column col."""
        for r in range(int(self.height)):
            if self.theboard[r][col] != ' ':
                self.theboard[r][col] = ' '
                break
    
    
    def winsFor(self, ox):
        """should return True if the given checker, 'X' or 'O', heldin ox, has won the calling Board."""
        #going horizontal
        for r in range(int(self.height)):
            for c in range(int(self.width)):
                try:
                    if (self.theboard[r][c]==ox) and (self.theboard[r][c+1]==ox) and \
                    (self.theboard[r][c+2]==ox) and (self.theboard[r][c+3]==ox):
                        return True
                except:
                    pass
        #goingvertical
        for r in range(int(self.height)):
            for c in range(int(self.width)):
                try:
                    if (self.theboard[r][c]==ox) and (self.theboard[r+1][c]==ox) and \
                    (self.theboard[r+2][c]==ox) and (self.theboard[r+3][c]==ox):
                        return True
                except:
                    pass
        #going diagonal right
        for r in range(int(self.height)):
            for c in range(int(self.width)):
                try:
                    if (self.theboard[r][c]==ox) and (self.theboard[r+1][c-1]==ox) and \
                    (self.theboard[r+2][c-2]==ox) and (self.theboard[r+3][c-3]==ox):
                        return True
                except:
                    pass
        #going diagonal left
        for r in range(int(self.height)):
            for c in range(int(self.width)):
                try:
                    if (self.theboard[r][c]==ox) and (self.theboard[r+1][c+1]==ox) and \
                    (self.theboard[r+2][c+2]==ox) and (self.theboard[r+3][c+3]==ox):
                        return True
                except: 
                    pass
        return False

     
    def hostGame(self):
        """a method that, when called from a connect four board object, willrun a loop allowing the user(s) to play a game."""
        print("Welcome to Connect Four!")
        print(self)
        ox = 'O'
        while self.winsFor(ox)==False:
            if ox == 'O':
                ox = 'X'
                move = input("X's choice:")
                while self.allowsMove(int(move)) == False:
                    move = input("X's choice:")
                self.addMove(int(move), ox)
            elif ox == 'X':
                ox = 'O'
                move = input("O's choice:")
                while self.allowsMove(int(move)) == False:
                    move = input("O's choice:")
                self.addMove(int(move), ox)
            print(self)
        print(ox + " wins -- Congratulations!")
        sys.exit()
