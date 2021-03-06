time = input()

zero = [["+", "-", "-", "-", "+"],
        ["|", " ", " ", " ", "|"],
        ["|", " ", " ", " ", "|"],
        ["+", " ", " ", " ", "+"],
        ["|", " ", " ", " ", "|"],
        ["|", " ", " ", " ", "|"],
        ["+", "-", "-", "-", "+"]]

one = [[" ", " ", " ", " ", "+"],
       [" ", " ", " ", " ", "|"],
       [" ", " ", " ", " ", "|"],
       [" ", " ", " ", " ", "+"],
       [" ", " ", " ", " ", "|"],
       [" ", " ", " ", " ", "|"],
       [" ", " ", " ", " ", "+"]]

two = [["+", "-", "-", "-", "+"],
       [" ", " ", " ", " ", "|"],
       [" ", " ", " ", " ", "|"],
       ["+", "-", "-", "-", "+"],
       ["|", " ", " ", " ", " "],
       ["|", " ", " ", " ", " "],
       ["+", "-", "-", "-", "+"]]

three = [["+", "-", "-", "-", "+"],
         [" ", " ", " ", " ", "|"],
         [" ", " ", " ", " ", "|"],
         ["+", "-", "-", "-", "+"],
         [" ", " ", " ", " ", "|"],
         [" ", " ", " ", " ", "|"],
         ["+", "-", "-", "-", "+"]]

four = [["+", " ", " ", " ", "+"],
        ["|", " ", " ", " ", "|"],
        ["|", " ", " ", " ", "|"],
        ["+", "-", "-", "-", "+"],
        [" ", " ", " ", " ", "|"],
        [" ", " ", " ", " ", "|"],
        [" ", " ", " ", " ", "+"]]

five = [["+", "-", "-", "-", "+"],
        ["|", " ", " ", " ", " "],
        ["|", " ", " ", " ", " "],
        ["+", "-", "-", "-", "+"],
        [" ", " ", " ", " ", "|"],
        [" ", " ", " ", " ", "|"],
        ["+", "-", "-", "-", "+"]]

six = [["+", "-", "-", "-", "+"],
       ["|", " ", " ", " ", " "],
       ["|", " ", " ", " ", " "],
       ["+", "-", "-", "-", "+"],
       ["|", " ", " ", " ", "|"],
       ["|", " ", " ", " ", "|"],
       ["+", "-", "-", "-", "+"]]

seven = [["+", "-", "-", "-", "+"],
         [" ", " ", " ", " ", "|"],
         [" ", " ", " ", " ", "|"],
         [" ", " ", " ", " ", "+"],
         [" ", " ", " ", " ", "|"],
         [" ", " ", " ", " ", "|"],
         [" ", " ", " ", " ", "+"]]

eight = [["+", "-", "-", "-", "+"],
         ["|", " ", " ", " ", "|"],
         ["|", " ", " ", " ", "|"],
         ["+", "-", "-", "-", "+"],
         ["|", " ", " ", " ", "|"],
         ["|", " ", " ", " ", "|"],
         ["+", "-", "-", "-", "+"]]

nine = [["+", "-", "-", "-", "+"],
        ["|", " ", " ", " ", "|"],
        ["|", " ", " ", " ", "|"],
        ["+", "-", "-", "-", "+"],
        [" ", " ", " ", " ", "|"],
        [" ", " ", " ", " ", "|"],
        ["+", "-", "-", "-", "+"]]

colon = [[" "],
         [" "],
         ["o"],
         [" "],
         ["o"],
         [" "],
         [" "]]

digits = [zero, one, two, three, four, five, six, seven, eight, nine]

while time != "end":
    first = int(time[0])
    second = int(time[1])
    third = int(time[3])
    fourth = int(time[4])

    for row in range(7):
        for col in range(5):
            print(digits[first][row][col], end="")
        print("", end="  ")

        for col in range(5):
            print(digits[second][row][col], end="")
        print("", end="  ")

        for col in range(1):
            print(colon[row][col][col], end="")
        print("", end="  ")

        for col in range(5):
            print(digits[third][row][col], end="")
        print("", end="  ")

        for col in range(5):
            print(digits[fourth][row][col], end="")
        print()

    print("\n")

    time = input()

print("end")
