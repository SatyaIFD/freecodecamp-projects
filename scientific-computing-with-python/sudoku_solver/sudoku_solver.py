class Board:
    # Initializes the board with the given board.
    def __init__(self, board):
        self.board = board

    # String representation of the board.
    def __str__(self):
        board_str = ''
        # For each row, convert the numbers to strings (0 becomes a '*')
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)  # Join the numbers with spaces
            board_str += '\n'  # Add a newline after each row
        return board_str

    # Finds the first empty cell (0 represents an empty cell).
    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                # Tries to find the first index with value 0 (empty cell)
                col = contents.index(0)
                return row, col
            except ValueError:
                pass  # If no 0 is found in this row, move to the next row
        return None  # If no empty cell is found, return None

    # Checks if a number is valid in a given row.
    def valid_in_row(self, row, num):
        return num not in self.board[row]

    # Checks if a number is valid in a given column.
    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9))

    # Checks if a number is valid in the 3x3 square that contains the given row and column.
    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3  # Starting row of the 3x3 square
        col_start = (col // 3) * 3  # Starting column of the 3x3 square
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False  # If number is found in the square, return False
        return True

    # Checks if placing a number in the empty cell is valid (in terms of row, column, and square).
    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    # Solves the Sudoku using backtracking algorithm.
    def solver(self):
        # Find the next empty cell (if any)
        if (next_empty := self.find_empty_cell()) is None:
            return True  # If there are no empty cells, the puzzle is solved
        for guess in range(1, 10):  # Try guessing numbers from 1 to 9
            if self.is_valid(next_empty, guess):  # If the guess is valid
                row, col = next_empty
                self.board[row][col] = guess  # Place the guessed number on the board
                if self.solver():  # Recursively try to solve the rest of the puzzle
                    return True  # If successful, return True
                self.board[row][col] = 0  # If the guess leads to an unsolvable state, reset the cell
        return False  # Return False if no valid guesses were found

# Main function to solve the Sudoku puzzle
def solve_sudoku(board):
    gameboard = Board(board)  # Create a Board object
    print(f'Puzzle to solve:\n{gameboard}')  # Print the initial puzzle
    if gameboard.solver():  # Try to solve the puzzle using the solver
        print(f'Solved puzzle:\n{gameboard}')  # If solved, print the solution
    else:
        print('The provided puzzle is unsolvable.')  # If unsolvable, print a message
    return gameboard  # Return the solved (or unsolved) board

# Example puzzle to test the solver
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
solve_sudoku(puzzle)  # Call the function to solve the Sudoku puzzle
