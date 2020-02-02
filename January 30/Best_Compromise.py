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

    for col in range(N):
        zero = 0
        one = 0

        for row in range(M):
            if arr[row][col] == "0":
                zero += 1
            else:
                one += 1
        if zero > one:
            compromise += "0"
        else:
            compromise += "1"

    print(compromise)
