NPM = input().split()

num_participants = int(NPM[0])
points_to_win = int(NPM[1])
lines = int(NPM[2])

scores = {}
winners = []

for names in range(num_participants):
    scores[input()] = 0

for score in range(lines):
    name_points = input().split()
    name = name_points[0]
    point = int(name_points[1])

    scores[name] += point

    if scores[name] >= points_to_win and name not in winners:
        winners.append(name)

if len(winners) == 0:
    print("No winner!")
else:
    for name in winners:
        print(name + " wins!")
