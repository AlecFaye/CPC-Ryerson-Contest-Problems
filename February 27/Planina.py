N = int(input())

base = 2

for iteration in range(N):
    base = (base * 2) - 1

print(base * base)
