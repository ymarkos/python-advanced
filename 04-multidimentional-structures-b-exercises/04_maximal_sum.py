import sys

rows, cols = ([int(el) for el in input().split()])

rect_matrix = []

for _ in range(rows):
    rect_matrix.append([int(el) for el in input().split()])

max_square_matrix = []
max_sum = - sys.maxsize
for row in range(rows - 2):
    for col in range(cols - 2):
        square_matrix = [
            rect_matrix[row][col], rect_matrix[row][col+1], rect_matrix[row][col+2],
            rect_matrix[row+1][col], rect_matrix[row+1][col+1], rect_matrix[row+1][col+2],
            rect_matrix[row+2][col], rect_matrix[row+2][col+1], rect_matrix[row+2][col+2]
            ]
        sum_square = sum(square_matrix)
        if sum_square > max_sum:
            max_sum = sum_square
            max_square_matrix = square_matrix.copy()

print(f'Sum = {max_sum}')

max_square_matrix = [max_square_matrix[i:i+3] for i in range(0, len(max_square_matrix), 3)]
for row in range(len(max_square_matrix)):
    print(*max_square_matrix[row])