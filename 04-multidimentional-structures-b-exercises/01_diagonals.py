num = int(input())

matrix = []
for _ in range(num):
    matrix.append([int(el) for el in input().split(', ')])

primary_diagonal = []
secondary_diagonal = []
for row_index in range(num):
    for col_index in range(num):
        if row_index == col_index:
            primary_diagonal.append(matrix[row_index][col_index])
        if (row_index + col_index) == (num - 1):
            secondary_diagonal.append(matrix[row_index][col_index])

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)


print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {primary_sum}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {secondary_sum}')
