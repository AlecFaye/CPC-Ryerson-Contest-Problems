data_set = int(input())

for cases in range(data_set):

    number_of_teams = int(input())
    scores = input()
    scores = scores.split()
    scores.sort()

    performance = 0

    first_index = len(scores) // 3
    second_index = first_index * 2

    for index in range(first_index + 1, second_index + 1):
        performance += int(scores[index])

    print(performance)
