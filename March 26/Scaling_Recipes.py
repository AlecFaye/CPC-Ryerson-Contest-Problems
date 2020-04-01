test = int(input())

for cases in range(test):
    rpd = input().split()

    num_ingredients = int(rpd[0])
    num_portions = int(rpd[1])
    num_desired_portions = int(rpd[2])

    ingredients = []

    for index in range(num_ingredients):
        ingredients.append(input().split())

    scale = 0

    for ingredient in ingredients:
        if float(ingredient[2]) == 100:
            scale = (num_desired_portions / num_portions) * float(ingredient[1])

    print("Recipe # " + str(cases + 1))

    for ingredient in ingredients:
        weight = float(ingredient[2]) / 100 * scale
        print(ingredient[0] + " " + str(round(weight, 1)))

    print("----------------------------------------")
