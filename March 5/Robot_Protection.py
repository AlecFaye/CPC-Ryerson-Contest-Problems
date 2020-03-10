import fileinput


def calculate_area():
    pass


coordinates = []
area = 0

for line in fileinput.input():

    if line == "0":
        break

    line = line.split()

    if len(line) == 1:
        calculate_area()
        coordinates = []
        area = 0
    else:
        coordinates.append((line[0], line[1]))


