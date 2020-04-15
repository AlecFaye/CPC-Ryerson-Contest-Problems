ants = input().split()

total_ants = int(ants[0]) + int(ants[1])

ants_left = input()[::-1]
ants_right = input()

seconds = int(input())

ant_group = []

for index in range(len(ants_left)):
    ant_group.append(ants_left[index])

for index in range(len(ants_right)):
    ant_group.append(ants_right[index])

for loop in range(seconds):
    index = 0
    while index < total_ants - 1:
        if ant_group[index] in ants_left and ant_group[index + 1] in ants_right:
            temp = ant_group[index]
            ant_group[index] = ant_group[index + 1]
            ant_group[index + 1] = temp
            index += 2
        else:
            index += 1

for ant in ant_group:
    print(ant, end="")
