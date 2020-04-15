test = int(input())

for case in range(test):
    num_of_guests = int(input())
    invitations = input().split()

    code_count = {}

    for invitation_code in invitations:
        if invitation_code not in code_count:
            code_count[invitation_code] = 1
        else:
            code_count[invitation_code] += 1

    for code in code_count:
        if code_count[code] == 1:
            print("Case #" + str(case + 1) + ": " + code)
