def permutations(dig):

    if len(dig) == 0:
        return []

    if len(dig) == 1:
        return [dig]

    lst = []

    for i in range(len(dig)):
        m = dig[i]

        remain = dig[:i] + dig[i + 1:]

        for j in permutations(remain):
            lst.append([m] + j)

    return lst


X = int(input())

digits = []
number = X

while X > 0:
    digits.append(X % 10)
    X = X // 10

all_numbers = []

for num in permutations(digits):
    all_numbers.append(num)

whole_numbers = []

for num in all_numbers:
    a = 0
    for digit in range(len(num), 0, -1):
        a = a + num[len(num) - digit] * 10 ** (digit - 1)
    whole_numbers.append(a)

whole_numbers.sort()

nothing = True

for num in whole_numbers:
    if num > number:
        print(num)
        nothing = False
        break

if nothing:
    print(0)
