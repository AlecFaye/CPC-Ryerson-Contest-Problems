import fileinput

paragraph = []

for line in fileinput.input():
    paragraph.append(line)

maximum_length = 0

for sentence in paragraph:
    if len(sentence) > maximum_length:
        maximum_length = len(sentence)

raggedness = 0

for sentence in range(len(paragraph) - 1):
    value = (maximum_length - len(paragraph[sentence])) ** 2
    raggedness += value

print(raggedness)
