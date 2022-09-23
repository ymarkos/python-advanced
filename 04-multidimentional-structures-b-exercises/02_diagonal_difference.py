square_side = int(input())

matrix = []
for _ in range(square_side):
    matrix.append([int(el) for el in input().split()])

primary_sum = 0
secondary_sum = 0
for row_index in range(square_side):
    for col_index in range(square_side):
        if row_index == col_index:
            primary_sum += matrix[row_index][col_index]
        if (row_index + col_index) == square_side - 1:
            secondary_sum += matrix[row_index][col_index]
difference = abs(primary_sum - secondary_sum)

print(difference)
