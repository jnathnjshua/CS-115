#
# life.py - Game of Life lab
#
# Name:Jonathan Joshua
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#

import random, sys

def createOneRow(w):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(w, h) function."""
    row = []
    for col in range(w):
        row += [0]
    return row

def createBoard(w, h):
    """returns a 2d array with "h" rows and "w" cols"""
    A = []
    for row in range(h):
        A += [createOneRow(w)]
    return A

def printBoard(A):
    """this function prints the 2d list-of-listsA without spaces (using sys.stdout.write)"""
    for row in A:              
        for col in row:         
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(w, h):
    """creates an empty board and then modifies itso that it has a diagonal strip of "on" cells. """
    A = createBoard(w, h)
    for row in range( h):
        for col in range(w):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w, h):
    """returns a 2d array of all live cells - with the value of 1 - except for a one-cell-wide border of empty cells (with the value of 0) around the edge of the 2d array."""
    A = createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = 1
    return A

def randomCells(w, h):
    """returns an array of randomly-assigned 1's and 0's except that the outer edge of the array is still completely empty (all 0's) as in the case ofinnerCells."""
    A = createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = random.choice([0,1])
    return A

def copy(A):
    """which will make a deep copy of the 2d array A."""
    h = len(A)
    w = len(A[0])
    newA = createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if A[row][col] == 1:
                newA[row][col] = 1
    return newA

def innerReverse(A):
    """takes an old 2d array (or "generation") and then creates a new generation of the same shape and size (either with copy, above, or createBoard)."""
    h = len(A)
    w = len(A[0])
    newA = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if A[row][col] == 1:
                newA[row][col] = 0
            else: 
                newA[row][col] = 1
    return newA


def countNeighbors(row, col, A):
    """returns the number of live neighbors for a cell in the board A at a particular row and col."""
    neighbors = 0
    for x in [-1, 0, 1]:
        for a in [-1, 0, 1]:
            if A[row+x][col+a] == 1:
                neighbors += 1
    if A[row][col] == 1:
        return neighbors - 1
    else:
        return neighbors

def next_life_generation(A):
    """makes a copy of A and then advanced onegeneration of Conway's game of life withinthe *inner cells* of that copy.The outer edge always stays 0."""
    newA = copy(A)
    h = len(A)
    w = len(A[0])
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if countNeighbors(row, col, A) < 2:
                newA[row][col] = 0
            elif countNeighbors(row, col, A) > 3:
                newA[row][col] = 0
            elif countNeighbors(row, col, A) == 3:
                newA[row][col] = 1
    return newA
