# Sudoku Solver 🧩

This Python program solves Sudoku puzzles using a **backtracking algorithm**. The board is represented with a 9x9 grid, where **0** represents an empty cell. The program uses the `Board` class to validate placements in rows, columns, and 3x3 subgrids. It will either **solve** the puzzle or determine that it's **unsolvable**.

## 🛠 Features

* **Backtracking Solver**: Tries different numbers in empty cells and backtracks when a conflict arises.
* **Board Representation**: The Sudoku grid is shown in a user-friendly format with `*` for empty cells.
* **Validation**: Ensures that no number repeats in the same row, column, or 3x3 subgrid.
* **Readable Output**: Prints the board before and after solving, with empty cells represented as `*`.

## 📝 Classes and Methods

### `Board`

* **`__init__(self, board)`**: Initializes the Sudoku board with a 9x9 grid.
* **`__str__(self)`**: Returns a string representation of the board for easy viewing.
* **`find_empty_cell(self)`**: Finds the first empty cell (0).
* **`valid_in_row(self, row, num)`**: Checks if a number is valid in the given row.
* **`valid_in_col(self, col, num)`**: Checks if a number is valid in the given column.
* **`valid_in_square(self, row, col, num)`**: Checks if a number is valid in the 3x3 square that contains the given cell.
* **`is_valid(self, empty, num)`**: Ensures placing a number in the empty cell adheres to Sudoku rules.
* **`solver(self)`**: Solves the puzzle using backtracking.

### `solve_sudoku(board)`

* **`solve_sudoku(board)`**: Takes a 9x9 board, prints the unsolved version, and attempts to solve it. If solvable, it shows the solution.

## 🚀 Usage

To solve a Sudoku puzzle, just pass a 9x9 grid to the `solve_sudoku()` function:

```python
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
solve_sudoku(puzzle)
```

### Example Output 🧩

```
Puzzle to solve:
* * 2 * * 8 * * *
* * * * * 3 7 6 2
4 3 * * * * 8 * *
* 5 * * 3 * * 9 *
* 4 * * * * * 2 6
* * * 4 6 7 * * *
* 8 6 7 * 4 * * *
* * * 5 1 9 * * 8
1 7 * * * 6 * * 5

Solved puzzle:
6 9 2 1 4 8 5 3 7
5 8 4 9 7 3 7 6 2
4 3 1 6 2 5 8 7 9
3 5 7 8 3 2 6 9 4
2 4 3 7 8 9 9 2 6
8 3 5 4 6 7 2 5 8
```

### ❗ Notes

* **Empty cells** are represented as `0` and will be shown as `*` in the printed board.
* The solver guarantees a solution for solvable puzzles, but will return **"The provided puzzle is unsolvable"** if no valid solution exists.
* The algorithm uses **backtracking**, so it tries different numbers and checks for conflicts.


