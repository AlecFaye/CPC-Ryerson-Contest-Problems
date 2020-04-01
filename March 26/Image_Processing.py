HWNM = input().split()

# Image Height and Width
image_height = int(HWNM[0])
image_width = int(HWNM[1])

# Kernel Height and Width
kernel_height = int(HWNM[2])
kernel_width = int(HWNM[3])

# Matrix Height and Width
matrix_height = image_height - kernel_height + 1
matrix_width = image_width - kernel_width + 1

# Image Input
image = []

for index in range(image_height):
    row = input().split()

    for col in range(len(row)):
        row[col] = int(row[col])

    image.append(row)

# Kernel Input
kernel = []

for index in range(kernel_height):
    row = input().split()

    for col in range(len(row)):
        row[col] = int(row[col])

    kernel.append(row)

kernel.reverse()

for index in kernel:
    index.reverse()

# Matrix Output
matrix = []
matrix_sum = 0

for m_height in range(matrix_height):
    matrix_row = []

    for m_width in range(matrix_width):
        matrix_sum = 0

        for k_height in range(kernel_height):

            for k_width in range(kernel_width):
                matrix_sum += image[m_height + k_height][m_width + k_width] * int(kernel[k_height][k_width])

        matrix_row.append(matrix_sum)
    matrix.append(matrix_row)

for row in matrix:
    for index in row:
        print(str(index) + " ", end="")
    print()
