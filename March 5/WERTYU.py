sentence = input()

keyboard = {"Q": "Q",
            "W": "Q",
            "E": "W",
            "R": "E",
            "T": "R",
            "Y": "T",
            "U": "Y",
            "I": "U",
            "O": "I",
            "P": "O",
            "[": "P",
            "{": "P",
            "}": "{",
            "\\": "}",
            "A": "A",
            "S": "A",
            "D": "S",
            "F": "D",
            "G": "F",
            "H": "G",
            "J": "H",
            "K": "J",
            "L": "K",
            ":": "L",
            ";": "L",
            "'": ":",
            "Z": "Z",
            "X": "Z",
            "C": "X",
            "V": "C",
            "B": "V",
            "N": "B",
            "M": "N",
            ",": "M",
            "<": "M",
            ".": ",",
            ">": ",",
            "/": ".",
            "?": ".",
            " ": " "}

back_one_sentence = ""

for letter in sentence:
    back_one_sentence += keyboard.get(letter)

print(back_one_sentence)
