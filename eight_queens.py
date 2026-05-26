n = 8

board = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    board.append(row)

def is_safe(row, col):

    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1

    i = row
    j = col

    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j - 1

    return True

def solve(col):

    if col >= n:
        return True

    for i in range(n):

        if is_safe(i, col):

            board[i][col] = 1

            if solve(col + 1):
                return True

            board[i][col] = 0

    return False

solve(0)

for i in range(n):
    for j in range(n):
        print(board[i][j], end=" ")
    print()