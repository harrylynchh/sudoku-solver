'''
main.py
4/2/2025
Harry Lynch
Main file for the sudoku solver, takes in input and insantiates an initial board + solver,
runs and instruments the search and prints the results.
'''
import sys
import time
from board import SudokuBoard
from solver import SudokuSolver

# Validate that a csv is passed: MUST BE IN PROPER SUDOKU FORMAT (rows of 9 comma-separated values)
if len(sys.argv) != 2:
    print("Please provide a csv containing a valid sudoku board (SEE README), I have provided two valid examples (sudoku1.csv, sudoku2.csv):")
    print("Usage: python main.py <path_to_csv>")
    quit

file_path = sys.argv[1]
# Create initial board based off the csv and the solver with the initial board
board = SudokuBoard.from_csv(file_path)
solver = SudokuSolver(board)

# Print the original and the solved.
print("Original Sudoku:")
board.print()

# If a valid solution is found:
curr = time.time()
fin: int
if solver.solve():
    fin = time.time()
    print("\nSolved Sudoku:")
    board.print()
else:
    fin = time.time()    
    print("\n*** No solution exists, validate that the given file is a solvable sudoku board in the correct format. (SEE README.md) ***")

# Print the time the search took to complete in seconds to 5 decimal places
print(f"\nThe Recursive Backtracking algorithm w/ MRV reached this conclusion in: {round(fin-curr, 5)}s")