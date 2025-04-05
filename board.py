'''
board.py
4/2/2025
Harry Lynch
Implementation of a basic Sudoku Board class with capabilities of being instantiated
from a csv, checking the validity (no duplicates within a row, col, or 3x3 grid),
and printing a formatted version of the board to the console for easy viewing.
'''
import csv

class SudokuBoard:
    '''Constructor'''
    def __init__(self, grid: list[list[int]]):
        self.grid: list[list[int]] = grid

    '''
    from_csv
    Static helper method used to create a new SudokuBoard from a csv.
    NOTE: Referenced stack overflow to figure out how to make a method static w/ the decorator
          This makes it so from_csv can be called independent of an instance of SudokuBoard-- fitting my use case
    '''
    @staticmethod
    def from_csv(file_path: str) -> "SudokuBoard":
        # Open the provided csv filepath and assign to the board in the order
        # the csv provides
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            grid = [[int(cell) for cell in row] for row in reader]
        # Return an instance of a SudokuBoard with the newly-instantiated grid
        return SudokuBoard(grid)

    '''
    is_valid
    Checks if an assignment of num at [row][col] is valid given the current board state
    '''
    def is_valid(self, row: int, col: int, num: int) -> bool:
        # Check both col and row
        for i in range(9):
            # If a duplicate is found return false
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
            
        # Check each 3x3 grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for row_offset in range(3):
            for col_offset in range(3):
                # If a duplicate is found return false
                if self.grid[start_row + row_offset][start_col + col_offset] == num:
                    return False
        # If neither check resulted in a false return, we have a valid board
        return True
    '''
    print
    Iterates over the current board state and prints the value in each row and a
    '.' for each empty cell (cells containing a 0)
    '''
    def print(self) -> None:
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else '.' for num in row))
