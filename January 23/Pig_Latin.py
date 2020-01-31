import fileinput

for line in fileinput.input():

    sentence = line.split()

    vowels = "aeiouy"
    vowel_exists = False

    new_sentence = ""

    for word in sentence:

        vowel_exists = False

        for letter in vowels:

            if letter in word[0]:
                vowel_exists = True
                break;

        if vowel_exists:
            new_sentence += word + "yay "
        else:
            while word[0] not in vowels:
                word = word[1: len(word)] + word[0]
            new_sentence += word + "ay "

    print(new_sentence)
