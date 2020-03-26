def find_hiss(word):

    for letters in range(len(word) - 1):
        if word[letters: letters + 2] == "ss":
            return True
    return False


line = input()

if find_hiss(line):
    print("hiss")
else:
    print("no hiss")
