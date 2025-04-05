# README.md
## Harry Lynch
### 4/2/2025
### Solving Sudoku Boards
---
# About:

    This program is designed to solve sudoku puzzles using a Constraint-Satisfaction
    Problem approach.  Sudoku requires that each number in a cell holds no duplicates
    within that cell's row, column, and a 3x3 grid surrounding the cell.  With
    Sudoku boards being 9x9, this means that a solved board satisfies the 
    constraint that each row, column, and 3x3 grid contains no duplicate values
    of the numbers (1-9).  This is the constraint upon which this problem is focused.

    Implementation wise, this program uses basic recursive backtracking with the
    help of only the MRV (Minimum Remaining Value) Heuristic which indicates
    the cell in the puzzle with the fewest valid assignments given the current
    state of the board.  This subtle optimization attempts to minimize the number
    of recurisve calls made in the solution process as there is less "branching"
    of the solution tree and as a result less backtracking.  
    
    This implementation could have used addiitonal pruning strategies such as a Degree Heuristic,
    LCV, Forward Checking, and Arc Consistency-- all of which might have improved
    time performance.  However,  I am satisfied with MRV as a simple yet efficient
    way to prune in addition to the basic checking if an assignment would result
    in a satisfied board.

    The solution is comprised of 3 modules, a main for I/O and driver function calling,
    board.py which contains an implementation of a SudokuBoard class, and solver.py
    which contains a class with the facilities to implement the algorithms and 
    heuristics discussed in the above paragraph to execute the process of solving
    a sudoku puzzle.  
---
# Usage:

    - To run the program, execute: python main.py {path_to_csv_file}
        - The csv file provided must be in the following format with three examples
          provided in this project directory (sudoku1.csv, sudoku2.csv, invalid.csv):
            '''
            6,0,8,7,0,2,1,0,0
            4,0,0,0,1,0,0,0,2
            0,2,5,4,0,0,0,0,0
            7,0,1,0,8,0,4,0,5
            0,8,0,0,0,0,0,7,0
            5,0,9,0,6,0,3,0,1
            0,0,0,0,0,6,7,5,0
            2,0,0,0,9,0,0,0,8
            0,0,6,8,0,5,2,0,3
            '''
    - The total time spent in the recursive backtracking algorithm will be reported
      in addition to the solved puzzle (if a valid solution exists).
# Resources:
    
    - I referenced StackOverflow a few times for some of the list comprehension
      and object oriented questions I had while implementing the solver.
        - This StackOverflow question on static methods: https://stackoverflow.com/questions/735975/static-methods-in-python
    - I used time from the python stdlib to handle instrumenting the recurisve
      solution process. 

**No external packages are required to run this program.**