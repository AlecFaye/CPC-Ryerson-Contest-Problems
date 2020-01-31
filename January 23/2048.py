arr = []

for num in range(4):
    row = input()
    row = row.split()
    arr.append(row)

for i in range(4):
    for j in range(4):
        arr[i][j] = int(arr[i][j])

direction = int(input())


def rotate_array(rotate):
    new_arr = [[0 for a in range(4)] for b in range(4)]

    for x in range(4):
        for y in range(4):
            new_arr[x][y] = rotate[y][3 - x]

    return new_arr


for num in range(direction):
    arr = rotate_array(arr)


for row in range(4):
    for repeat in range(3):
        for col in range(1 + repeat, 4):
            merge = True

            if arr[row][repeat] == arr[row][col]:
                if col - repeat > 1:
                    for num in range(repeat + 1, col):
                        if arr[row][num] != 0:
                            merge = False

                if merge:
                    arr[row][repeat] = arr[row][repeat] * 2
                    arr[row][col] = 0
                    break

    for repeat in range(3):
        if arr[row][repeat] == 0:
            for col in range(1 + repeat, 4):
                if arr[row][col] != 0:
                    arr[row][repeat] = arr[row][col]
                    arr[row][col] = 0
                    break

for num in range(4 - direction):
    arr = rotate_array(arr)

for row in range(4):
    for col in range(4):
        print(arr[row][col], end=" ")
    print()
