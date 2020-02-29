blimps = []

for blimp_index in range(1, 5 + 1):
    current_blimp = input()

    for registration_index in range(len(current_blimp) - 2):
        if current_blimp[registration_index: registration_index + 3] == "FBI":
            blimps.append(blimp_index)

if len(blimps) == 0:
    print("HE GOT AWAY!")
else:
    for blimp_index in blimps:
        print(blimp_index, end=" ")
