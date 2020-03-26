test_cases = int(input())

for cases in range(test_cases):
    stores = int(input())

    location_inputs = input()
    locations = location_inputs.split()

    number_locations = []

    for store_index in range(len(locations)):
        number_locations.append(int(locations[store_index]))

    number_locations.sort()

    distance = 2 * (number_locations[-1] - number_locations[0])

    print(distance)
