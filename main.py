from typing import Tuple, List
board: List[List[int]] = [[-1]]
def valid(row: int, col: int, number: int) -> bool:
    if number in board[row]:
        return False
    for i in range(len(board)):
        if board[i][col] == number:
            return False
    return True

def row_check(row: int) -> bool:
    for i in range(1, 13):
        if i not in board[row]:
            return False
    return True

def col_check(col: int) -> bool:
    for i in range(1, 13):
        ok = False
        for row in range(len(board)):
            if board[row][col] == i:
                ok = True
                break
        if not ok:
            return False
    return True

def is_valid() -> bool:
    for row in range(len(board)):
        if not row_check(row):
            return False
    for col in range(len(board[0])):
        if not col_check(col):
            return False
    return True

def print_board() -> None:
    for i in range(len(board)):
        print(('{:>3}'*len(board[i])).format(*board[i]))

def next_pos(row, col) -> Tuple[int, int]:
    if col == len(board[row]) - 1:
        return row + 1, 0
    return row, col + 1

def solve(row, col, numbers = []):
    if row == len(board):
        print()
        if is_valid():
            print_board()
            print()
            print(numbers)
        #print()
        #print_board()
        return

    nrow, ncol = next_pos(row, col)
    if board[row][col] != 0:
        solve(nrow, ncol, numbers)
        return

    """
    print(f'row: {row} col: {col}')
    print()
    print_board()
    """

    for i in range(1, 13):
        if valid(row, col, i):
            board[row][col] = i
            solve(nrow, ncol, numbers + [i])
            board[row][col] = 0
if __name__ == '__main__':
    with open('input.in', 'r') as f:
        lines = list(f.readlines())
        print(([len(line.split(" ")) for line in lines]))
        print(len(lines))
        for i in range(len(lines)):
            lines[i] = lines[i].split(' ')
            lines[i] = list(map(str.strip, lines[i]))
            lines[i] = list(map(int, lines[i]))
        board = lines
        print_board()
        solve(0, 0)
