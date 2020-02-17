T = int(input())

for test in range(T):
    N = int(input())

    warehouse_dict = {}
    number_of_shipments = 0

    for n in range(N):
        shipment = input()
        shipment = shipment.split()

        if shipment[0] not in warehouse_dict:
            warehouse_dict[shipment[0]] = int(shipment[1])
            number_of_shipments += 1
        else:
            warehouse_dict[shipment[0]] += int(shipment[1])

    warehouse_arr = []

    for item in warehouse_dict:
        warehouse_arr.append((item, warehouse_dict[item]))

    sorted_by_item_name = sorted(warehouse_arr, key=lambda tup: (tup[1], tup[0]))
    sorted_by_item_name.reverse()

    sorted_by_item_count = sorted(sorted_by_item_name, key=lambda tup: tup[1])
    sorted_by_item_count.reverse()

    print(number_of_shipments)

    for item in sorted_by_item_count:
        print(item[0] + " " + str(item[1]))
