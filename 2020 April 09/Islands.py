row_col = input().split()
row_count = int(row_col[0])
col_count = int(row_col[1])

image = []

for input_row in range(row_count):
    image.append(input())


def check_area(land):
    return land


island_count = []

is_there_land = False

for row in image:
    if row.count("L") > 0:
        is_there_land = True

if is_there_land:
    for row in range(row_count):
        island = []
        count = len(island)

        for col in range(col_count):
            if image[row][col] == "L":
                if (row, col) not in island:
                    island.append((row, col))
            if len(island) != count:
                island = check_area(island)

        island_count.append(island)

if not is_there_land:
    print(0)
