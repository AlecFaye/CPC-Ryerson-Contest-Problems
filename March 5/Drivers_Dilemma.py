CXM = input()

CXM = CXM.split()

capacity = float(CXM[0])
leak_rate = float(CXM[1])
distance = float(CXM[2])

efficiency_table = []

for manual in range(6):
    mph_mpg = input()
    mph_mpg = mph_mpg.split()
    efficiency_table.append((float(mph_mpg[0]), float(mph_mpg[1])))

efficiency_table.reverse()

successful = False
margin = 10**-6

for eff in efficiency_table:
    speed = eff[0]
    efficiency = eff[1]

    time = distance / speed
    leak_total = leak_rate * time
    fuel_left = capacity / 2 - leak_total

    travel = efficiency * fuel_left

    if travel - distance > margin:
        successful = True

    if successful:
        print("YES " + str(int(speed)))
        break

if not successful:
    print("NO")
