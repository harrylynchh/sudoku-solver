'''
solver.py
4/2/2025
Harry Lynch
File containing the class definition for the SudokuSolver class, the primary
module responsible for carrying out the recursive backtracking aswell as the
Minimum Remaining Value heuristic used to choose the next position in the puzzle
to solve.  Also determines when a puzzle is completely solved.
'''
from board import SudokuBoard

class SudokuSolver:
    def __init__(self, board: SudokuBoard):
        self.board = board

    
    '''
    find_mrv_cell
    Use the Minimum Remaining Value heuristic to find the cell in the puzzle
    with the fewest valid assignment states given the current state of the board.
    Returns None (indicative of done solving) when all cells are filled and 
    the board is still valid.
    '''
    def find_mrv_cell(self) -> tuple[int, int, list[int]]:
        # Initialize a value which holds how many valid states a given cell has
        # and a variable to keep track of which cell is best.
        min_options = 10
        best_cell = None
        # Iterate over the entire board and check each unassigned cell (value of 0)
        for row in range(9):
            for col in range(9):
                if self.board.grid[row][col] == 0:
                    # Plug in each possible value (1-9) and add it to options if
                    # the board is still valid after the assignment
                    options = [num for num in range(1, 10) if self.board.is_valid(row, col, num)]
                    # Check if the evaluated cell is better than our current min, assign if so
                    if len(options) < min_options:
                        min_options = len(options)
                        best_cell = (row, col, options)
        # Return the cell with the fewest valid assignments to then assign
        return best_cell

    '''
    solve
    Core recursive backtracking algorithm which grabs the cell with the fewest
    valid assignments (MRV Heuristic) and recursively attempts each valid assignment.
    If no assignment works, backtrack to the previous set of assignments, else 
    continue forward. 
    '''
    def solve(self) -> bool:
        # Get the cell with the fewest valid assignments to "solve"
        cell = self.find_mrv_cell()
        # Base Case: If there is no mrv cell, the puzzle is solved-- return True
        if not cell:
            return True

        # Unpack the tuple to get coordinates and valid options for the cell
        row, col, options = cell
        
        # For each valid assignment possible, make the assignment and continue
        # recurisvely.
        for num in options:
            self.board.grid[row][col] = num
            if self.solve():
                return True
            self.board.grid[row][col] = 0
        # None of the assignments for the mrv cell worked, so backtrack to the
        # previous mrv cell's assignment
        return False
