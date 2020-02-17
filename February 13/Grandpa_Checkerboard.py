board_size = int(input())

board = []

for num in range(board_size):
    board.append(input())

row_equal = True
col_equal = True
consecutive_colour = False

for row in range(board_size):
    white = 0
    black = 0

    for col in range(board_size):
        if board_size > 2 and col < board_size - 3:
            if board[row][col] == board[row][col + 1] == board[row][col + 2]:
                consecutive_colour = True

        if board[row][col] == "W":
            white += 1
        else:
            black += 1

    if black != white:
        row_equal = False

for col in range(board_size):
    white = 0
    black = 0

    for row in range(board_size):
        if board_size > 2 and row < board_size - 3:
            if board[row][col] == board[row + 1][col] == board[row + 2][col]:
                consecutive_colour = True

        if board[row][col] == "W":
            white += 1
        else:
            black += 1

    if black != white:
        col_equal = False

if row_equal and col_equal and not consecutive_colour:
    print(1)
else:
    print(0)
