N = int(input())
M = int(input())

n = str(N)
m = str(M)

digits_1 = []
digits_2 = []

while N > 0:
    digits_1.append(N % 10)
    N = N // 10

while M > 0:
    digits_2.append(M % 10)
    M = M // 10

while len(digits_1) > len(digits_2):
    digits_2.append(0)

while len(digits_2) > len(digits_1):
    digits_1.append(0)

digits_1.reverse()
digits_2.reverse()

digits_3 = []
digits_4 = []

for index in range(len(digits_1)):
    if digits_1[index] > digits_2[index]:
        digits_3.append(digits_1[index])

    elif digits_1[index] < digits_2[index]:
        digits_4.append(digits_2[index])

    else:
        digits_3.append(digits_1[index])
        digits_4.append(digits_2[index])

num_1 = ""
num_2 = ""

if len(digits_3) == 0:
    print("YODA")
else:
    for num in digits_3:
        num_1 += str(num)
    print(int(num_1))

if len(digits_4) == 0:
    print("YODA")
else:
    for num in digits_4:
        num_2 += str(num)
    print(int(num_2))
