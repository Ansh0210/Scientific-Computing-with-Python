class Board:
    # Initialize the Board with a 2D list representing the Sudoku puzzle
    def __init__(self, board):
        self.board = board

    # Return a string representation of the board for printing
    def __str__(self):
        # Define the upper, middle, and lower boundary lines of the board
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines

        for index, line in enumerate(self.board):
            row_list = []
            # Split each line into 3 parts for the Sudoku's 3x3 subgrids
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                # Join the numbers in each part with '|'
                row_square = '|'.join(str(item) for item in part)
                row_list.extend(row_square)
                # Add the subgrid separator except for the last subgrid
                if square_no != 3:
                    row_list.append('║')

            # Form a row string, replacing '0' with spaces for readability
            row = f'║ {" ".join(row_list)} ║\n'
            row_empty = row.replace('0', ' ')
            board_string += row_empty

            # Add separators between rows or at the bottom of the board
            if index < 8:
                if index % 3 == 2:
                    board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                else:
                    board_string += middle_lines
            else:
                board_string += lower_lines

        return board_string

    # Find the next empty cell (represented by 0) on the board
    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    # Check if a number can be placed in a specific row without conflicts
    def valid_in_row(self, row, num):
        return num not in self.board[row]

    # Check if a number can be placed in a specific column without conflicts
    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9))

    # Check if a number can be placed in a specific 3x3 subgrid without conflicts
    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    # Check if placing a number in the given position is valid according to Sudoku rules
    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    # Recursive function to solve the Sudoku puzzle
    def solver(self):
        # Base case: if there are no empty cells, the puzzle is solved
        if (next_empty := self.find_empty_cell()) is None:
            return True
        else:
            # Try all possible numbers (1-9) in the empty cell
            for guess in range(1, 10):
                # If a number is valid, place it and recursively attempt to solve the rest of the puzzle
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    # Backtrack if not solvable with current placement
                    self.board[row][col] = 0

        # If no solution found, return False
        return False

# Function to solve a Sudoku puzzle and print the result
def solve_sudoku(board):
    gameboard = Board(board)
    print(f'\nPuzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print('\nSolved puzzle:')
        print(gameboard)
    else:
        print('\nThe provided puzzle is unsolvable.')
    return gameboard

# Example Sudoku puzzle
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
