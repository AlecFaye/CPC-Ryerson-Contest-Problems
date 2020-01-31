N = int(input())

score = []
checked = False

for a in range(3, 0, -1):

    for repeat in range(3):

        for i in range(20, 0, -1):
            if N - a * i == 0 and len(score) == 2:
                N = N - a * i
                score.append((a, i))
                break
            elif N - a * i >= 0 and len(score) < 2:
                N = N - a * i
                score.append((a, i))
                break

            if i == 1 and repeat == 2 and a == 1:
                checked = True
                break

        if N == 0 or len(score) == 3 or checked:
            break

    if N == 0 or len(score) == 3 or checked:
        break

if N == 0:
    for element in score:
        if element[0] == 3:
            print("triple " + str(element[1]))
        elif element[0] == 2:
            print("double " + str(element[1]))
        else:
            print("single " + str(element[1]))
else:
    print("impossible")
