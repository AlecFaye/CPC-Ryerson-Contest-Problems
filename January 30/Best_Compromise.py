T = int(input())

for test in range(T):
    row_col = input()
    row_col = row_col.split()

    M = int(row_col[0])
    N = int(row_col[1])

    arr = []

    for x in range(M):
        num = input()
        arr.append(num)

    compromise = ""
    zero = True

    for col in range(N):
        zero = True

        for row in range(M):
            if arr[row][col] == "1":
                zero = not zero
        if zero:
            compromise += "0"
        else:
            compromise += "1"

    print(compromise)
