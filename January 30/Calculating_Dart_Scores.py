N = int(input())

original = N

impossible = [163, 166, 169, 172, 173, 175, 176, 178, 179]

for tracker in [20, 19]:

    dart_score = []

    if tracker == 19:
        dart_score = [(3, 20)]
        N = original - 60

    for multiplier in range(3, 0, -1):

        for repeat in range(3):

            added = False

            for score in range(tracker, 0, -1):

                if len(dart_score) < 2 and N - multiplier * score >= 0:
                    dart_score.append((multiplier, score))
                    N = N - multiplier * score
                    added = True
                elif len(dart_score) == 2 and N - multiplier * score == 0:
                    dart_score.append((multiplier, score))
                    N = N - multiplier * score
                    added = True

                if added or N == 0 or len(dart_score) == 3:
                    break

            if N == 0 or len(dart_score) == 3:
                break

        if N == 0 or len(dart_score) == 3:
            break

    if N == 0:
        for element in dart_score:
            if element[0] == 3:
                print("triple " + str(element[1]))
            elif element[0] == 2:
                print("double " + str(element[1]))
            else:
                print("single " + str(element[1]))
    else:
        if tracker == 19 or original in impossible:
            print("impossible")

    if N == 0 or original in impossible:
        break
