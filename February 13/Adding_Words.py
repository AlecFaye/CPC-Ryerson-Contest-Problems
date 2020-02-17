import fileinput

words = {}

for line in fileinput.input():

    command = line.split()

    if len(command) <= 0:
        break

    if command[0] == "clear":
        break

    if command[0] == "def":
        words[command[1]] = int(command[2])

    unknown = False
    word_sum = None

    if command[0] == "calc":
        for variable in range(len(command)):
            if command[variable] != "calc":
                if command[variable] not in words \
                        and command[variable] != "+" and command[variable] != "-" and command[variable] != "=":
                    unknown = True
                else:
                    if word_sum is None:
                        word_sum = words[command[variable]]
                    else:
                        if command[variable] == "+":
                            if command[variable + 1] in words:
                                word_sum += words[command[variable + 1]]
                            else:
                                unknown = True
                        elif command[variable] == "-":
                            if command[variable + 1] in words:
                                word_sum -= words[command[variable + 1]]
                            else:
                                unknown = True

            if unknown:
                break

        for instruction in command:
            if instruction != "calc":
                print(instruction, end=" ")

        if unknown:
            print("unknown")
        else:
            found_word = False

            for find_word, word_value in words.items():
                if word_value == word_sum:
                    print(find_word)
                    found_word = True

            if not found_word:
                print("unknown")
