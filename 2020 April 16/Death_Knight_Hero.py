test = int(input())

count = int(test)

for case in range(test):
    attacks = input()

    for index in range(len(attacks) - 1):
        if attacks[index] == "C" and attacks[index + 1] == "D":
            count -= 1
            break

print(count)
