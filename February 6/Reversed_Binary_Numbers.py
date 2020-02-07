N = int(input())

number = N
binary = ""

while number > 0:
    if number % 2 == 0:
        binary += "0"
    else:
        binary += "1"
    number = number // 2

reversed_number = 0

for bit in range(len(binary) - 1, -1, -1):
    if binary[bit] == "1":
        reversed_number = reversed_number + 2 ** (len(binary) - 1 - bit)

print(reversed_number)
