T = int(input())

for test in range(1, T + 1):
    row_col = input()
    row_col = row_col.split()

    R = int(row_col[0])
    C = int(row_col[1])

    image = []

    for num in range(R):
        row = input()
        image.append(row)

    temp = []

    for row in range(R):
        image[row] = image[row][C::-1]

    for row in range(R - 1, -1, -1):
        temp.append(image[row])

    print("Test " + str(test))

    for row in temp:
        print(row)
