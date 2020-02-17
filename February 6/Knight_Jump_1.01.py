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

for row in range(N):
    index = []

    for col in range(N):
        # Gets the position of the knight
        if b[row][col] == knight:
            starting_position = (row, col)

        # Appends the string at the spot to the index's array
        index.append(b[row][col])

    # Appends the index row to the original board
    original_board.append(index)

print(starting_position)
