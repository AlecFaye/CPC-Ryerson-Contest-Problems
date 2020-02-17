# Set of possible knight moves
possible_moves = [(-2, -1), (-2, 1),
                  (-1, -2), (-1, 2),
                  (1, -2), (1, 2),
                  (2, -1), (2, 1)]

N = int(input())

b = []

empty = "."
blocked = "#"
knight = "K"

for x in range(N):
    b.append(input())

original_board = []
pos_k = (0, 0)

for row in range(N):
    index = []

    for col in range(N):
        # Gets the position of the knight
        if b[row][col] == knight:
            pos_k = (row, col)

        # Appends the string at the spot to the index's array
        index.append(b[row][col])

    # Appends the index row to the original board
    original_board.append(index)

knight_positions = [pos_k]


def check_moves(count):

    placed = False
    finished = False

    new_moves = []

    for position in knight_positions:

        for moves in possible_moves:
            x_move = position[0] + moves[0]
            y_move = position[1] + moves[1]

            # Checks if the move is within the board
            if 0 <= x_move < N and 0 <= y_move < N:

                # Checks if the move doesn't hit a blocked spot and the knight has not been in that position before
                if original_board[x_move][y_move] != blocked and (x_move, y_move) not in knight_positions:
                    new_moves.append((x_move, y_move))
                    original_board[x_move][y_move] = str(count)  # Gives me an idea of what the board would look like
                    placed = True

                # If the move gets the knight to (0, 0) the method breaks out
                if x_move == 0 and y_move == 0:
                    finished = True

            if finished:
                break

        if finished:
            break

    knight_positions.extend(new_moves)

    return placed, finished


added = True
done = False

index = 0

while added and not done:
    index = index + 1
    added, done = check_moves(index)

if not done:
    print(-1)
else:
    print(index)


def print_board():
    global row, index
    for row in original_board:
        for index in row:
            print(index, end=" ")
        print()
