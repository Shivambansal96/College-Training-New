def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, row, N):
    if row == N:
        print_board(board)
        return True
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place queen
            
            if solve_n_queens(board, row + 1, N):
                return True

            board[row][col] = 0  # Remove queen (backtrack)

    return False

def n_queens(N):
    board = [[0 for rows in range(N)] for cols in range(N)]
    if not solve_n_queens(board, 0, N):
        print("No Solution found.")

n_queens(4)
