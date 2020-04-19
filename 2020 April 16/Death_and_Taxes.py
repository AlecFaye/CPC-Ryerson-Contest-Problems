shares = 0
crowns = 0
sale = 0

while True:
    command = input().split()

    if command[0] == "buy":
        crowns = (crowns * shares + int(command[1]) * int(command[2])) / (shares + int(command[1]))
        shares = shares + int(command[1])

    if command[0] == "sell":
        shares = shares - int(command[1])

    if command[0] == "split":
        shares = shares * int(command[1])
        crowns = crowns / int(command[1])

    if command[0] == "merge":
        shares = shares // int(command[1])
        crowns = crowns * int(command[1])

    if command[0] == "die":
        if int(command[1]) > crowns:
            crowns = int(command[1]) - crowns
            sale = shares * (int(command[1]) - crowns * 0.3)
        else:
            sale = shares * int(command[1])
        print(sale)
        break
