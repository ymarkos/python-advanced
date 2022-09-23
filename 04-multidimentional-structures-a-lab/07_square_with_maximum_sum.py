import sys
rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split(', ')])

max_sum = - sys.maxsize
max_sum_matrix = []

for row_index in range(rows-1):
    for colon_index in range(cols - 1):
        sub_matrix = [matrix[row_index][colon_index], matrix[row_index][colon_index+1],
                      matrix[row_index+1][colon_index], matrix[row_index+1][colon_index+1]]
        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_matrix = sub_matrix.copy()

print(max_sum_matrix[0], max_sum_matrix[1])
print(max_sum_matrix[2], max_sum_matrix[3])
print(max_sum)