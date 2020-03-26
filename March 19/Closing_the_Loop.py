import re


def key(s):
    num, letters = re.match(r'(\d*)(.*)', s).groups()
    return float(num or 'inf'), letters


test_cases = int(input())

for cases in range(test_cases):

    segment = int(input())
    ropes = input().split()

    red_ropes = []
    blue_ropes = []

    for rope in ropes:
        if rope[-1] == "R":
            red_ropes.append(rope)
        else:
            blue_ropes.append(rope)

    red_ropes_sorted = sorted(red_ropes, key=key)
    blue_ropes_sorted = sorted(blue_ropes, key=key)

    red_ropes_sorted.reverse()
    blue_ropes_sorted.reverse()

    print(red_ropes_sorted)
    print(blue_ropes_sorted)

    if len(red_ropes_sorted) == 1 and len(blue_ropes_sorted) == 0:
        print(0)
    elif len(blue_ropes_sorted) == 1 and len(red_ropes_sorted) == 0:
        print(0)
