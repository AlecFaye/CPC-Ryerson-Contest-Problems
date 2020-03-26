frosh_count = int(input())

courses_array = []
count = 0
same = False

for frosh in range(frosh_count):

    courses = input()
    courses = courses.split()
    courses.sort()

    for frosh_courses in courses_array:

        same = True

        for index in range(5):
            if frosh_courses[index] != courses[index]:
                same = False

        if same:
            break

    if not same:
        courses_array.append(courses)
        count += 1

print(count)
