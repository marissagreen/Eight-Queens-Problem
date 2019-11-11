#  File: Queens.py

#  Description: Use backtracking and recursion to produce the # of eight-queen solutions for an nxn board.

#  Student Name: Marissa Green

#  Student UT EID: mdg3554

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 3/29/19

#  Date Last Modified: 4/1/19

class Queens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.board = [ ]
    self.n = n
    for i in range (self.n):
      row = [ ]
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution
  def recursive_solve (self, col):
    global solutions # global variable
    if (col == self.n): # there is a solution
      solutions += 1
    else:
      for i in range (self.n):
        if (self.is_valid (i, col)): # solution in this column for a queen
          self.board[i][col] = 'Q'
          if (self.recursive_solve (col + 1)): # solution in the next column for a queen
            return True 
          self.board[i][col] = '*'
      return False # there is no solution

  def solve(self):
    self.recursive_solve(0)
    
solutions = 0 # set up global variable

def main():

  n = int(input("Enter the size of board: "))
  while n < 1 or n > 16:
    n = int(input("Enter the size of board: "))

  # create a chess board
  game = Queens (n)

  # place the queens on the board
  game.solve()

  # num solutions counted in def recursive_solve
  print("Number of solutions:", solutions)

main()
