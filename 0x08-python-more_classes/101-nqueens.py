import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the same diagonal (left-top to right-bottom)
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the same diagonal (right-top to left-bottom)
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row):
    if row == N:
        print_solution(board)
    else:
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve_nqueens(board, row + 1)
                board[row] = -1

def print_solution(board):
    solution = []
    for i in range(N):
        row_string = '.' * board[i] + 'Q' + '.' * (N - board[i] - 1)
        solution.append(row_string)
    print('\n'.join(solution))
    print()

def nqueens(N):
    if not N.isdigit():
        print('N must be a number')
        sys.exit(1)
    N = int(N)
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)
    board = [-1] * N
    solve_nqueens(board, 0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    nqueens(sys.argv[1])

