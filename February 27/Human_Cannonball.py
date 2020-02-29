import math

cases = int(input())

gravity = 9.81

for test in range(cases):
    values = input()
    values = values.split()

    initial_velocity = float(values[0])
    angle = float(values[1]) * math.pi / 180
    hor_distance = float(values[2])
    min_height = float(values[3])
    max_height = float(values[4])

    time = hor_distance / (initial_velocity * math.cos(angle))

    ver_distance = initial_velocity * time * math.sin(angle) - 0.5 * gravity * time ** 2

    if min_height + 1 < ver_distance < max_height - 1:
        print("Safe")
    else:
        print("Not Safe")
