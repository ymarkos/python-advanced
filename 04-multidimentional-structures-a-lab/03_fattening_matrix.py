num = int(input())
flattened_matrix = []
for row_index in range(num):
    row = [int(x) for x in input().split(', ')]
    for col_index in range(len(row)):
        flattened_matrix.append(row[col_index])
print(flattened_matrix)
