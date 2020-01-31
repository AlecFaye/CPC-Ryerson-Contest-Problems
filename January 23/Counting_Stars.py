import fileinput


def count_stars(dimensions, space, case):

    dimensions = dimensions.split()

    row = dimensions[0]
    col = dimensions[1]

    stars_coordinates = []
    num_of_stars = 0
    star = '-'

    def find_stars(a, b, star_count):

        stars_coordinates.append((a, b))

        added = True

        while added:

            added = False

            for index in range(len(stars_coordinates)):

                coord = stars_coordinates[index]

                if coord[0] - 1 >= 0:
                    if space[coord[0] - 1][coord[1]] == star and (coord[0] - 1, coord[1]) not in stars_coordinates:
                        stars_coordinates.append((coord[0] - 1, coord[1]))
                        added = True

                if coord[0] + 1 < row:
                    if space[coord[0] + 1][coord[1]] == star and (coord[0] + 1, coord[1]) not in stars_coordinates:
                        stars_coordinates.append((coord[0] + 1, coord[1]))
                        added = True

                if coord[1] - 1 >= 0:
                    if space[coord[0]][coord[1] - 1] == star and (coord[0], coord[1] - 1) not in stars_coordinates:
                        stars_coordinates.append((coord[0], coord[1] - 1))
                        added = True

                if coord[1] + 1 < col:
                    if space[coord[0]][coord[1] + 1] == star and (coord[0], coord[1] + 1) not in stars_coordinates:
                        stars_coordinates.append((coord[0], coord[1] + 1))
                        added = True

            if added:
                star_count += 1

        return stars_coordinates

    for x in range(row):
        for y in range(col):
            if space[x][y] == star and (x, y) not in stars_coordinates:
                stars_coordinates, num_of_stars = find_stars(x, y, num_of_stars)

    print("Case " + str(case) + ": " + str(num_of_stars))


row_col = []
space_out = []

for line in fileinput.input():
    if line[0].isdigit():
        row_col.append(line)
    else:
        space_out.append(line)

for case in range(len(row_col)):
    count_stars(row_col[case], space_out[case], case)
